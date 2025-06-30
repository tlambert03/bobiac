import nbformat
import sys

TAG = "style"
CELL_STYLE_INLINE = """
background-color: rgb(157, 243, 137);
padding: 0px 5px;
border-radius: 5px;
"""


def process_styled_cells(notebook_path):
    """
    Process notebook markdown cells with 'style' tag and add CSS styling.
    Also adds a CSS cell at the beginning if styled cells are found.
    """
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    modified = False

    # Remove any existing CSS cells at the beginning (no longer needed with inline styles)
    if (
        len(nb.cells) > 0
        and nb.cells[0].cell_type in ["raw", "markdown"]
        and "styled-cell" in nb.cells[0].source
    ):
        nb.cells.pop(0)
        modified = True
        print("  🧹 Removed old CSS cell (using inline styles now)")

    # Process markdown cells with style tag
    for cell in nb.cells:
        if (
            cell.cell_type == "markdown"
            and "tags" in cell.metadata
            and TAG in cell.metadata.get("tags", [])
        ):
            # Remove existing styled-cell wrapper if present
            if cell.source.startswith(
                '<div class="styled-cell">'
            ) and cell.source.endswith("</div>"):
                # Extract content between the div tags
                content = cell.source[
                    len('<div class="styled-cell">') : -len("</div>")
                ].strip()
                cell.source = content
                print("  🧹 Removed existing styling from markdown cell")

            # Also remove inline styled divs
            if cell.source.startswith("<div style=") and cell.source.endswith("</div>"):
                # Extract content between the div tags - more complex parsing needed
                start_idx = cell.source.find(">") + 1
                end_idx = cell.source.rfind("</div>")
                if start_idx > 0 and end_idx > start_idx:
                    content = cell.source[start_idx:end_idx].strip()
                    cell.source = content
                    print("  🧹 Removed existing inline styling from markdown cell")

            # Add fresh inline styling wrapper
            cell.source = (
                f'<div style="{CELL_STYLE_INLINE}">\n\n{cell.source}\n\n</div>'
            )
            modified = True
            print(f"  ✅ Added inline styling to markdown cell with '{TAG}' tag")

    # Save if modified
    if modified:
        with open(notebook_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
        print(f"  💾 Updated {notebook_path}")
    else:
        print(f"  ⏭️  No styled cells found in {notebook_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_notebooks_style.py <notebook_path>")
        sys.exit(1)

    process_styled_cells(sys.argv[1])
