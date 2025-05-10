# BoBiAC Book

## How to use it:

- Clone this repository.

- Create a fresh environment.

- Move into the cloned directory.

- Install the requirements:
    - `pip install -r requirements.txt`
    - `NOTE`: if to use on eof your notebook you require a specific pacckage, make sure to add it to the `requirements.txt` file.

- To build the book (on Mac/Linux):
    - run the command:
        - `./build_local.sh`
        - `NOTE`: if you get a permission error, run `chmod +x build_local.sh` one time to make the script executable.
    - the generated `index.html` will be opened in your browser.
