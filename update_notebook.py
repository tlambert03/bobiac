import nbformat
import sys
from pathlib import Path

def update_notebook(input_path: str | Path, output_path: str | Path) -> None:
    nb = nbformat.read(input_path, as_version=4)
    cleaned_cells = []

    for cell in nb.cells:
        tags = cell.get("metadata", {}).get("tags", [])

        # Remove entire cell if it contains certain tags
        if any(tag in tags for tag in ["remove-input", "remove-output", "remove-cell"]):
            continue

        # Remove 'skip-execution' tag if present
        if "skip-execution" in tags:
            tags.remove("skip-execution")
            cell["metadata"]["tags"] = tags

        # Keep only the first line of markdown cells (the title) and remove the rest
        if cell.cell_type == "markdown":
            lines = cell.source.splitlines()
            cell.source = lines[0] if lines else ""

        cleaned_cells.append(cell)

    nb.cells = cleaned_cells
    nbformat.write(nb, output_path)

if __name__ == "__main__":
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    update_notebook(src, dest)