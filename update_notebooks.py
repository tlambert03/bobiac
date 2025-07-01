import nbformat
import sys
import re
from pathlib import Path
from update_styles_data import H2_STYLE, H3_STYLE, EXAMPLE_STYLE, EXERCISE_STYLE

# When building the Jupyter Book, the links in the intro_to_python_II notebook
# need to be updated when converting to a Jupyter Notebook or they will not work.
# This is a mapping of the links in the book to the links that should be updated
# in the notebook.
map_03_python_II_boke_to_notebook = {
    "#commenting-printing": "#0.-Commenting-&-Printing",
    "#data-types": "#1.-Data-Types",
    "#variables": "#2.-Variables",
    "#operators": "#3.-Operators",
    "#data-structures": "#4.-Data-Structures",
    "#data-structures-lists": "#5.-Data-Structures:-Lists",
    "#data-structures-tuples": "#6.-Data-Structures:-Tuples",
    "#data-structures-dictionaries": "#7.-Data-Structures:-Dictionaries",
    "#data-structures-sets": "#8.-Data-Structures:-Sets",
    "#for-loops": "#9.-For-Loops",
    "#if-statements": "#10.-If-Statements",
    "#functions": "#11.-Functions",
}


def update_notebooks(input_path: str | Path, output_path: str | Path) -> None:
    nb = nbformat.read(input_path, as_version=4)
    cleaned_cells = []

    for i, cell in enumerate(nb.cells):
        tags = cell.get("metadata", {}).get("tags", [])

        # remove buttons from the first cell and keep only the title
        if i == 0 and cell.cell_type == "markdown":
            lines = cell.source.splitlines()
            cell.source = lines[0] if lines else ""

        # clear the cell input if it has the 'teacher' tag (it is an exercise)
        if "teacher" in tags:
            # remove the tag
            tags.remove("teacher")
            # clear the cell content
            cell.source = ""
            # clear the cell output if any
            if cell.cell_type == "code":
                cell.outputs = []
                cell.execution_count = None

        # remove entire cell if it contains certain tags
        if any(tag in tags for tag in ["remove-input", "remove-output", "remove-cell"]):
            continue

        # remove 'skip-execution' tag if present
        if "skip-execution" in tags:
            tags.remove("skip-execution")
            cell["metadata"]["tags"] = tags

        # Replace links in intro_to_python_II.ipynb
        if (
            Path(input_path).name == "intro_to_python_II.ipynb"
            and cell.cell_type == "markdown"
        ):
            # Sort by length (descending) to process longer patterns first
            # This prevents partial matches from breaking longer patterns
            sorted_mappings = sorted(
                map_03_python_II_boke_to_notebook.items(),
                key=lambda x: len(x[0]),
                reverse=True,
            )
            for old_link, new_link in sorted_mappings:
                cell.source = cell.source.replace(old_link, new_link)

        # Apply styling to markdown headers
        if cell.cell_type == "markdown":
            content = cell.source
            lines = content.split("\n")
            modified = False

            for i, line in enumerate(lines):
                # Check for ## headers (apply TITLE_STYLE)
                if match := re.match(r"^(##\s+)(.+)$", line):
                    prefix, title = match[1], match[2]
                    lines[i] = f'{prefix}<p style="{H2_STYLE}">{title}</p>'
                    modified = True

                elif match := re.match(r"^(###\s+)(.+)$", line):
                    prefix, title = match[1], match[2]
                    title_lower = title.lower()

                    # Determine style based on content
                    if "exercise" in title_lower:
                        style = EXERCISE_STYLE
                    elif "example" in title_lower:
                        style = EXAMPLE_STYLE
                    else:
                        style = H3_STYLE

                    lines[i] = f'{prefix}<p style="{style}">{title}</p>'
                    modified = True

            if modified:
                cell.source = "\n".join(lines)

        cleaned_cells.append(cell)

    nb.cells = cleaned_cells
    nbformat.write(nb, output_path)


if __name__ == "__main__":
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    update_notebooks(src, dest)
