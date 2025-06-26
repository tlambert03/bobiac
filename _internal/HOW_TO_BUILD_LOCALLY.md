# BoBiAC Book

## How to use it

- Clone this repository.

- Move into the cloned directory.

- Create a fresh environment.

- Install the requirements:
  - `pip install -r requirements.txt`
  - `NOTE`: if to use on of your notebook you require a specific package, make sure to add it to the `requirements.txt` file.
  - I added the `pre-commit` package to the requirements that also checks for typing errors using `typos` and formatting issues, so after installing the `requirements.txt` file, run `pre-commit install` in th eterminal to set it up. I recommend running `pre-commit run --all-files` in the terminal after you stage the changes in VSCode to see what it will do before committing them (it should automatically run when you click on `commit` in VSCode anyway).
  - `NOTE`: if `typos` tries to change words that are not supposed to be changed (e.g. `nd2` -> `and2`), add the word to the `_typos.toml` file in the root directory of the repository.

- To build the book (on Mac/Linux):
  - run the command:
    - `./build_local.sh -r`
  - `NOTE`: if you get a permission error, run `chmod +x build_local.sh` one time to make the script executable.
  - `NOTE`: the first time you can also use the `-l` flag (`./build_local.sh -r -l`) and the book will be automatically opened in your browser (otherwise open the `index.html` file in the generated `_build/html` folder)
