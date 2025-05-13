# BoBiAC Book

## How to use it

- Clone this repository.

- Move into the cloned directory.

- Create a fresh environment.

- Install the requirements:
  - `pip install -r requirements.txt`
  - `NOTE`: if to use on of your notebook you require a specific package, make sure to add it to the `requirements.txt` file.

- To build the book (on Mac/Linux):
  - run the command:
    - `./build_local.sh -r`
  - `NOTE`: if you get a permission error, run `chmod +x build_local.sh` one time to make the script executable.
  - `NOTE`: the first time you can also use the `-l` flag (`./build_local.sh -r -l`) and the book will be automatically opened in your browser (otherwise open the `index.html` file in the generated `_build/html` folder)
