#!/usr/bin/env python3
"""Convert Jekyll posts to Hugo format."""

import re
import os

SRC_DIR = "/Users/jackgindi/Projects/personal_site/_posts"
DST_DIR = "/Users/jackgindi/Projects/personal_site_examples/texify3/content/posts"

FILES = [
    "2017-01-25-file-comp.md",
    "2017-02-25-check-matmul.md",
    "2017-03-15-linalg-deriv.md",
    "2017-04-05-hotel.md",
    "2017-04-26-inapprox-tsp.md",
    "2017-05-26-euler-basel.md",
    "2017-07-26-sqrt-2.md",
    "2017-08-26-memory.md",
    "2017-09-27-alternating.md",
    "2017-10-27-cantor-set.md",
    "2017-12-2-ftoa.md",
    "2018-01-01-euler-identity.md",
    "2018-01-10-dht.md",
    "2018-02-21-puzzles.md",
    "2018-05-22-mvt.md",
]

def convert_frontmatter(fm_text):
    """Convert Jekyll frontmatter to Hugo format."""
    lines = fm_text.strip().split('\n')
    new_lines = []
    skip_keys = {'use_math', 'layout', 'icon', 'order', 'toc', 'categories'}

    for line in lines:
        # Check key
        match = re.match(r'^(\w+)\s*:', line)
        if match:
            key = match.group(1)
            if key in skip_keys:
                continue

            if key == 'title':
                # Ensure title is double-quoted
                # Extract value
                val_match = re.match(r'^title\s*:\s*(.*)', line)
                if val_match:
                    val = val_match.group(1).strip()
                    # Remove existing quotes if any
                    if (val.startswith('"') and val.endswith('"')) or \
                       (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    new_lines.append(f'title: "{val}"')
                    continue

            elif key == 'tags':
                # Convert [tag1, tag2] to ["tag1", "tag2"]
                val_match = re.match(r'^tags\s*:\s*(.*)', line)
                if val_match:
                    val = val_match.group(1).strip()
                    # Remove inline comments (# ...)
                    val = re.sub(r'\s*#.*$', '', val).strip()
                    # Check if it's array format [...]
                    arr_match = re.match(r'^\[(.*)\]$', val)
                    if arr_match:
                        inner = arr_match.group(1)
                        tags = [t.strip().strip('"\'') for t in inner.split(',')]
                        tags = [t for t in tags if t]
                        quoted = ', '.join(f'"{t}"' for t in tags)
                        new_lines.append(f'tags: [{quoted}]')
                        continue

            elif key == 'date':
                # Keep date as-is (remove any trailing comments)
                val_match = re.match(r'^date\s*:\s*(.*)', line)
                if val_match:
                    val = re.sub(r'\s*#.*$', '', val_match.group(1)).strip()
                    new_lines.append(f'date: {val}')
                    continue

        # For any other lines, keep if no skip key
        new_lines.append(line)

    return '\n'.join(new_lines)


def convert_math_divs(content):
    """Convert <div>...\begin{...}...\end{...}...</div> and <div>$$...$$</div>."""

    # Case A: <div> wrapping LaTeX environments (\begin{...}...\end{...})
    def replace_env(m):
        inner = m.group(1).strip()
        return f'$$\n{inner}\n$$'

    content = re.sub(
        r'<div>\s*(\\begin\{[^}]+\}.*?\\end\{[^}]+\})\s*</div>',
        replace_env,
        content,
        flags=re.DOTALL
    )

    # Case B: <div> wrapping $$...$$
    def replace_display(m):
        inner = m.group(1).strip()
        return inner

    content = re.sub(
        r'<div>\s*(\$\$.*?\$\$)\s*</div>',
        replace_display,
        content,
        flags=re.DOTALL
    )

    return content


def fix_image_paths_cantor(content):
    """Fix image paths in cantor-set post."""
    # Replace bare image references with prefixed ones
    content = re.sub(
        r'!\[([^\]]*)\]\(cantor_set\.jpg\)',
        r'![\1](/posts/cantor-set/cantor_set.jpg)',
        content
    )
    # Also handle any other bare image refs (just in case)
    content = re.sub(
        r'<img\s+src=["\']cantor_set\.jpg["\']',
        '<img src="/posts/cantor-set/cantor_set.jpg"',
        content
    )
    return content


def convert_post(filename):
    src_path = os.path.join(SRC_DIR, filename)
    dst_path = os.path.join(DST_DIR, filename)

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_raw = parts[1]
            body = parts[2]
            fm_converted = convert_frontmatter(fm_raw)
            new_content = f'---\n{fm_converted}\n---{body}'
        else:
            new_content = content
    else:
        new_content = content

    # Convert math divs
    new_content = convert_math_divs(new_content)

    # Fix image paths for cantor-set
    if 'cantor-set' in filename:
        new_content = fix_image_paths_cantor(new_content)

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Converted: {filename}")
    return dst_path


def main():
    os.makedirs(DST_DIR, exist_ok=True)

    for filename in FILES:
        convert_post(filename)

    print("\nAll done!")


if __name__ == '__main__':
    main()
