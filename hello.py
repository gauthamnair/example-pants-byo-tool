import os

# The .flake8 config ignores unused import errors
# A long line that flake8 will complain about unless we change max line length to >=86


def hello_world():
    print("Hello world")  # change this to single quotes for black to change it.


def move_up_to_make_it_too_close_for_flake8():
    return 42
