#!/usr/bin/env python3
"""
Port Jekyll blog posts to Hugo format.
"""

import re
import os

SOURCE_DIR = "/Users/jackgindi/Projects/personal_site/_posts"
DEST_DIR = "/Users/jackgindi/Projects/personal_site_examples/texify3/content/posts"

FILES = [
    "2021-05-09-regularization.md",
    "2021-09-01-interp.md",
    "2022-01-12-solving-wordle.md",
    "2022-05-18-stpete.md",
    "2022-09-11-data-stream.md",
    "2023-01-03-dalle.md",
    "2023-04-06-fast-lm-inf.md",
    "2023-07-14-series-rearrangement.md",
    "2023-12-22-ransac.md",
    "2024-03-08-sim-ann.md",
    "2024-07-17-self-supervision.md",
    "2024-09-02-exist-vs-construct.md",
    "2024-11-17-sorting-bound.md",
    "2024-12-09-paper-rec-experience.md",
    "2025-02-15-multimodality.md",
    "2025-11-26-logistic-regression.md",
]

# Image path prefixes per file
IMAGE_PREFIXES = {
    "2021-09-01-interp.md": "/posts/interp/",
    "2023-01-03-dalle.md": "/posts/dalle/",
    "2023-07-14-series-rearrangement.md": "/posts/series-rearrangement/",
    "2023-12-22-ransac.md": "/posts/ransac/",
    "2024-07-17-self-supervision.md": "/posts/self-supervision/",
    "2024-09-02-exist-vs-construct.md": "/posts/exist-vs-construct/",
    "2024-11-17-sorting-bound.md": "/posts/sorting-bound/",
    "2025-11-26-logistic-regression.md": "/posts/logistic-regression/",
    "2025-02-15-multimodality.md": "/posts/multimodality/",
}

# Fields to remove from frontmatter
REMOVE_FIELDS = {"use_math", "layout", "icon", "order", "toc", "categories"}


def convert_frontmatter(fm_text):
    """Convert Jekyll frontmatter to Hugo format."""
    lines = fm_text.split("\n")
    output_lines = []

    for line in lines:
        # Skip lines that are comments-only or empty
        stripped = line.strip()

        # Check if this line starts a field we want to remove
        field_match = re.match(r'^(\w+)\s*:', line)
        if field_match:
            field_name = field_match.group(1)
            if field_name in REMOVE_FIELDS:
                continue

        # Handle title: ensure it's quoted with double quotes
        title_match = re.match(r'^title:\s*(.*)', line)
        if title_match:
            title_val = title_match.group(1).strip()
            # Remove existing quotes if present
            if (title_val.startswith('"') and title_val.endswith('"')) or \
               (title_val.startswith("'") and title_val.endswith("'")):
                title_val = title_val[1:-1]
            # Escape any internal double quotes
            title_val = title_val.replace('"', '\\"')
            output_lines.append(f'title: "{title_val}"')
            continue

        # Handle tags: convert [tag1, tag2] to ["tag1", "tag2"]
        tags_match = re.match(r'^tags:\s*\[(.*)\]', line)
        if tags_match:
            tags_content = tags_match.group(1)
            # Strip trailing comment
            tags_content = re.sub(r'\s*#.*$', '', tags_content)
            tags = [t.strip().strip('"\'') for t in tags_content.split(',')]
            quoted_tags = ', '.join(f'"{t}"' for t in tags if t)
            output_lines.append(f'tags: [{quoted_tags}]')
            continue

        # Remove inline comments from other lines (like "# TAG names should always be lowercase")
        # Only strip trailing comments on non-tags lines if they appear
        line = re.sub(r'\s+#\s+TAG names.*$', '', line)

        output_lines.append(line)

    return "\n".join(output_lines)


def convert_math_blocks(body):
    """Convert <div>...</div> wrapped math to Hugo/KaTeX format."""

    # Case A: <div>\begin{...}...\end{...}</div>  -> $$\n\begin{...}...\end{...}\n$$
    def replace_begin_end(m):
        inner = m.group(1).strip()
        return f"$$\n{inner}\n$$"

    body = re.sub(
        r'<div>\s*(\\begin\{.*?\\end\{[^}]+\})\s*</div>',
        replace_begin_end,
        body,
        flags=re.DOTALL
    )

    # Case B: <div>\n$$...$$\n</div> -> just $$...$$
    def replace_display_math(m):
        inner = m.group(1).strip()
        return inner

    body = re.sub(
        r'<div>\s*(\$\$.*?\$\$)\s*</div>',
        replace_display_math,
        body,
        flags=re.DOTALL
    )

    # Case C: <div><img .../></div>  -> just <img .../>  (image wrapped in div, not math)
    def replace_img_div(m):
        inner = m.group(1).strip()
        return inner

    body = re.sub(
        r'<div>\s*(<img\b[^>]*/?>)\s*</div>',
        replace_img_div,
        body,
        flags=re.DOTALL
    )

    return body


def update_image_paths(body, prefix):
    """Update image paths to use the given prefix."""

    # Handle markdown image syntax: ![alt](filename.ext) or ![alt](path/filename.ext)
    # We want to prepend prefix to bare filenames (no leading /)
    def replace_md_img(m):
        alt = m.group(1)
        path = m.group(2)
        # Only update if path doesn't already have a prefix/URL
        if not path.startswith('/') and not path.startswith('http'):
            # Strip any existing directory prefix, keep just filename
            filename = os.path.basename(path)
            path = prefix + filename
        return f"![{alt}]({path})"

    body = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_md_img, body)

    # Handle <img src="filename.ext"> tags
    def replace_img_src(m):
        before = m.group(1)
        path = m.group(2)
        after = m.group(3)
        if not path.startswith('/') and not path.startswith('http'):
            filename = os.path.basename(path)
            path = prefix + filename
        return f'{before}{path}{after}'

    body = re.sub(r'(<img\s+[^>]*src=")([^"]+)(")', replace_img_src, body)

    return body


def port_file(filename):
    src_path = os.path.join(SOURCE_DIR, filename)
    dst_path = os.path.join(DEST_DIR, filename)

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter from body
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        print(f"WARNING: Could not parse frontmatter in {filename}")
        return

    fm_text = fm_match.group(1)
    body = fm_match.group(2)

    # Convert frontmatter
    new_fm = convert_frontmatter(fm_text)

    # Convert math blocks
    new_body = convert_math_blocks(body)

    # Update image paths if needed
    if filename in IMAGE_PREFIXES:
        new_body = update_image_paths(new_body, IMAGE_PREFIXES[filename])

    # Reconstruct file
    new_content = f"---\n{new_fm}\n---\n{new_body}"

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Ported: {filename}")


def main():
    os.makedirs(DEST_DIR, exist_ok=True)

    for filename in FILES:
        src_path = os.path.join(SOURCE_DIR, filename)
        if not os.path.exists(src_path):
            print(f"MISSING source: {filename}")
            continue
        port_file(filename)

    print("\nDone.")


if __name__ == "__main__":
    main()
