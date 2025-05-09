# BoBiAC Book

## How to use it:

- Clone this repository.

- Create a fresh environment.

- Move into the cloned directory.

- Install the requirements:
    - `pip install -r requirements.txt`
    - `NOTE`: if to use on eof your notebook you require a specific pacckage, make sure to add it to the `requirements.txt` file.

- To build the book:
    - Move into the `bobiac-book` directory.
    - run the command:
        - `sphinx-build . -b html _build/html`
        - `NOTE`: if you want to start fresh and make sure that the `_build` directory is empty, you can use the `-a` flag:
            - `sphinx-build -a . -b html _build/html`
        - `NOTE`: if you get some error, I suggest to manually delete the `_build` directory and run the command again.
    - a `_build/html` directory will be created in the root directory; inside you can find the html files that you can open in a browser.
