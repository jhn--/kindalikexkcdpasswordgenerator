#! /usr/bin/env python3

import sys
from random import randrange

_ALPHABET = {
    "a":[],
    "b":[],
    "c":[],
    "d":[],
    "e":[],
    "f":[],
    "g":[],
    "h":[],
    "i":[],
    "j":[],
    "k":[],
    "l":[],
    "m":[],
    "n":[],
    "o":[],
    "p":[],
    "q":[],
    "r":[],
    "s":[],
    "t":[],
    "u":[],
    "v":[],
    "w":[],
    "x":[],
    "y":[],
    "z":[]
}

_PASSWORD = []

class Error(Exception):
    pass

class YouNeedAWordError(Error):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'

def get_words():
    with open('./words_alpha.txt', 'r') as fp:
        words = fp.readlines()
        for i in _ALPHABET.keys():
            _ALPHABET[i] = [x.strip('\n') for x in words if x[0] == i and len(x) <= 6]

def main(w):
    # print(f'{w}')

    get_words()

    # for i in _ALPHABET.keys():
    #     print(f'{len(_ALPHABET[i])}')
    
    for i in w:
        _PASSWORD.append(_ALPHABET[i][randrange(len(_ALPHABET[i]))])
    
    print(f'Password generated: {(" ").join(_PASSWORD)}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        wordd = sys.argv[1]
        main(wordd)
    else:
        raise YouNeedAWordError("BRO, ENTER A WORD! Can't do what I need to do without a word broooooo!")
