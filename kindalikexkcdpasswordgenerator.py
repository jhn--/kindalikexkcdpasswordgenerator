#! /usr/bin/env python3

from random import randrange
import argparse
import requests

_ALPHABET = {}

_PASSWORD = []

_WORD_LIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"


def get_words(word_set: set, num_of_letters: int) -> dict:
    """Accepts a set() of alphabets and populates the _global_ dictionary, `_ALPHABET` 
    with words from `_WORD_LIST_URL` that start with the alphabets with letter cound not more than 
    the maximum number of letters defined by `num_of_letters`.

    Args: 
        word_set (set): A set() of alphabets split from word.
        num_of_letters (int): Number of letters new random words can have up to.
    """
    try:
        r = requests.get(_WORD_LIST_URL)
    except Exception as e:
        raise e
    else:
        for letter in word_set:
            _ALPHABET[letter] = [word for word in r.text.split(
                '\r\n') if word[0] == letter and len(word) <= num_of_letters]


def check_num_of_letters(num_of_letters: int) -> int:
    """Accepts `num_of_letters` to check if it is less than 3.
    If `num_of_letters` is greater than or equals to 3, return `num_of_letters` as-is. 
    Otherwise, return `num_of_letters` with the value of 6.

    Args: 
        num_of_letters (int)

    Returns: 
        num_of_letters (int)
    """
    if num_of_letters < 3:
        print("Number of letters defined by user is less than 3. Using default value of 6.")
        return 6
    else:
        return num_of_letters


def main(word: str, count: int) -> list:
    """Main function. 
    Converts string `word` to a set() to remove duplicate alphabets in `word`.
    Forwards `count` to `check_num_of_letters()` to check if value less than 3.
    Passes `word_set` and `num_of_letters` to get_words() to list of words in dictionary `_ALPHABET`.
    Randomly select words that starts with the alphabets in set() and populate into global `_PASSWORD`.

    Args:
        word (str): Word to split up into alphabets, after which alphabets are used as starting letter for a new random word.
        count (int): Number of alphabets new random word should have at most.
    """
    word_set = set(word)
    num_of_letters = check_num_of_letters(count)

    get_words(word_set, num_of_letters)

    for i in word:
        _PASSWORD.append(_ALPHABET[i][randrange(len(_ALPHABET[i]))])

    print(f'Password generated: {(" ").join(_PASSWORD)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word", type=str, help="Word to break up and convert into xkcd style password.")
    parser.add_argument(
        "-c", "--count", type=int, help="Maximum number of alphabets you want each component to be. \
            Default set at 6. Program will set value at 6 if any user input value is lesser than 3.", default=6)
    args = parser.parse_args()

    main(args.word, args.count)
