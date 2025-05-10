import nbformat
import sys
from pathlib import Path

def clean_notebook(input_path: str | Path, output_path: str | Path) -> None:
    """
    Cleans a Jupyter notebook by removing cells based on specific rules.
    - Cells tagged with "delete" are removed.
    - Cells tagged with "show" and "remove-cell" have the "remove-cell" tag removed.
    """

    nb = nbformat.read(input_path, as_version=4)
    cleaned_cells = []

    for cell in nb.cells:
        tags = cell.get("metadata", {}).get("tags", [])

        # delete cell if it the word "remove-..." is in the tags
        if "remove-input" in tags or "remove-output" in tags or "remove-cell" in tags:
            continue

        # if the tag has "skip-execution" in it, remove the tag
        if "skip-execution" in tags:
            tags.remove("skip-execution")
            cell["metadata"]["tags"] = tags

        cleaned_cells.append(cell)

    nb.cells = cleaned_cells
    nbformat.write(nb, output_path)

if __name__ == "__main__":
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    clean_notebook(src, dest)