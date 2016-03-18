# letter_game.py

Python-based hangman style game, created for the [Python Basics](https://teamtreehouse.com/library/python-basics) course from [Treehouse](https://teamtreehouse.com).

## Setup

1. Create a text file (preferably in the same directory as this script)
2. Put individual words (a-z characters only) on each line
3. Save and run the script (see Usage below)

:information_source: see animals.txt for an example

## Usage

### Command line

Pass the path to the word list file as an argument when running the script:

```terminal
python letter_game.py words.txt
```

### Python shell/REPL

1. Open a Python shell
    ```terminal
    python
    ```

2. Import the script
    ```py
    >>> import letter_game
    ```

3. Enter a path to the word list file when prompted
    ```terminal
    Please provide the path to a text file with a list of single words separated by new lines:
    (or type 'quit' to exit)                                                                  
    > words.txt       
    ```