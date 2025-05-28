import nbformat
import sys
from pathlib import Path

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
            # clear rthe cell content
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

        cleaned_cells.append(cell)

    nb.cells = cleaned_cells
    nbformat.write(nb, output_path)

if __name__ == "__main__":
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    update_notebooks(src, dest)