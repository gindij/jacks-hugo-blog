#!/usr/bin/env python3
"""
Port Jekyll blog posts (batch 1: 2018-2021 early posts) to Hugo format.
"""
import re
import os

SRC_DIR = "/Users/jackgindi/Projects/personal_site/_posts"
DST_DIR = "/Users/jackgindi/Projects/personal_site_examples/texify3/content/posts"

FILES = [
    "2018-05-24-monty-hall.md",
    "2018-05-28-birthday.md",
    "2018-08-02-bin-pois.md",
    "2018-09-16-two-approaches.md",
    "2018-10-11-eigvals.md",
    "2018-11-04-markov-chebyshev.md",
    "2018-12-31-lln.md",
    "2019-09-23-mse.md",
    "2019-10-13-fib-diff-eq.md",
    "2020-04-05-cantors-thm.md",
    "2020-09-04-cvx-opt.md",
    "2020-10-27-fib-lin-alg.md",
    "2020-11-27-anniversary-math.md",
    "2020-12-27-qr.md",
    "2021-03-08-finding-eigvals.md",
    "2021-03-10-first-pub.md",
    "2021-04-11-sudoku-lp.md",
]

# Posts with image path corrections: filename -> prefix
IMAGE_PREFIX_MAP = {
    "2018-05-24-monty-hall.md": "/posts/monty-hall/",
    "2018-09-16-two-approaches.md": "/posts/two-approaches/",
    "2020-09-04-cvx-opt.md": "/posts/cvx-opt/",
    "2021-04-11-sudoku-lp.md": "/posts/sudoku-lp/",
}

# Frontmatter fields to remove entirely
REMOVE_FIELDS = {"use_math", "layout", "icon", "order", "toc", "categories", "pin"}


def convert_frontmatter(fm_text):
    """Convert Jekyll frontmatter to Hugo format."""
    lines = fm_text.split("\n")
    result = []
    for line in lines:
        # Check if this line starts a field we should remove
        field_match = re.match(r'^(\w+)\s*:', line)
        if field_match:
            field_name = field_match.group(1)
            if field_name in REMOVE_FIELDS:
                continue

        # Ensure title is double-quoted
        title_match = re.match(r'^title:\s*(.*)', line)
        if title_match:
            title_val = title_match.group(1).strip()
            # Remove any existing quotes
            if len(title_val) >= 2 and \
               ((title_val[0] == '"' and title_val[-1] == '"') or
                    (title_val[0] == "'" and title_val[-1] == "'")):
                title_val = title_val[1:-1]
            result.append(f'title: "{title_val}"')
            continue

        # Convert tags array format: tags: [tag1, tag2] -> tags: ["tag1", "tag2"]
        # Handle optional trailing inline comment
        tags_match = re.match(r'^(tags\s*:\s*)\[([^\]]*)\]', line)
        if tags_match:
            prefix = tags_match.group(1)
            tags_content = tags_match.group(2)
            tags = [t.strip().strip('"\'') for t in tags_content.split(",") if t.strip()]
            quoted_tags = ", ".join(f'"{t}"' for t in tags)
            result.append(f"{prefix}[{quoted_tags}]")
            continue

        result.append(line)

    return "\n".join(result)


def convert_math_divs(body):
    """
    Convert Jekyll-style <div>...</div> math blocks to Hugo/KaTeX format.

    Only matches bare <div> tags (no attributes) to avoid altering
    structural divs like <div align='center'>.

    Case A: <div>\\begin{...}...\\end{...}</div>  ->  $$\\n...\\n$$
    Case B: <div>$$...$$</div>  ->  $$...$$  (just strip div wrappers)
    """
    # Case A: bare <div> containing \begin{...}...\end{...}
    def replace_begin_end(m):
        inner = m.group(1).strip()
        return f"$$\n{inner}\n$$"

    body = re.sub(
        r'<div>\s*(\\begin\{.*?\\end\{[^}]+\})\s*</div>',
        replace_begin_end,
        body,
        flags=re.DOTALL
    )

    # Case B: bare <div> containing $$...$$
    def replace_dollar_dollar(m):
        inner = m.group(1).strip()
        return inner

    body = re.sub(
        r'<div>\s*(\$\$.*?\$\$)\s*</div>',
        replace_dollar_dollar,
        body,
        flags=re.DOTALL
    )

    return body


def fix_image_paths(body, prefix):
    """
    Update image paths to use the given prefix.
    Only updates bare filenames (no leading / or http).

    Handles:
      ![alt](filename.ext)          ->  ![alt](/posts/slug/filename.ext)
      <img src="filename.ext" ...>  ->  <img src="/posts/slug/filename.ext" ...>
    """
    # Markdown images
    def replace_md_image(m):
        alt = m.group(1)
        path = m.group(2)
        if not path.startswith("/") and not path.startswith("http"):
            return f"![{alt}]({prefix}{path})"
        return m.group(0)

    body = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_md_image, body)

    # HTML img src attributes
    def replace_html_src(m):
        before = m.group(1)
        src = m.group(2)
        after = m.group(3)
        if not src.startswith("/") and not src.startswith("http"):
            return f"{before}{prefix}{src}{after}"
        return m.group(0)

    body = re.sub(r'(<img\s+[^>]*src=")([^"]+)(")', replace_html_src, body)

    return body


def port_post(filename):
    src_path = os.path.join(SRC_DIR, filename)
    dst_path = os.path.join(DST_DIR, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split frontmatter from body
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        print(f"WARNING: Could not parse frontmatter in {filename}")
        return False

    fm_text = fm_match.group(1)
    body = fm_match.group(2)

    # Transform frontmatter
    fm_converted = convert_frontmatter(fm_text)

    # Transform math divs in body
    body_converted = convert_math_divs(body)

    # Fix image paths if needed
    if filename in IMAGE_PREFIX_MAP:
        prefix = IMAGE_PREFIX_MAP[filename]
        body_converted = fix_image_paths(body_converted, prefix)

    # Reassemble
    output = f"---\n{fm_converted}\n---\n{body_converted}"

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"  Ported: {filename}")
    return True


def main():
    os.makedirs(DST_DIR, exist_ok=True)

    success = 0
    for filename in FILES:
        src_path = os.path.join(SRC_DIR, filename)
        if not os.path.exists(src_path):
            print(f"  ERROR: Source not found: {src_path}")
            continue
        if port_post(filename):
            success += 1

    print(f"\nDone. {success}/{len(FILES)} files ported.")


if __name__ == "__main__":
    main()
