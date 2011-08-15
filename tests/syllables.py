#!/usr/bin/env python
""" Syllable counting.

Run like:

    $ ./syllables.py "Barbara Streisand"
    Between 4 and 5 syllables in barbara streisand

"""


print "Loading...",
import itertools
import string
import sys

from curses.ascii import isdigit
from nltk.corpus import cmudict

d = cmudict.dict()


def nsyl(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]

def count_syllables(words):
    # Sanitize input
    if type(words) is not list:
        words = [words]

    # Strip punctuation
    exclude = set(string.punctuation)
    words = [''.join(ch for ch in word if ch not in exclude) for word in words]

    # Count syllables of each word.
    try:
        results = [nsyl(word) for word in words]
    except KeyError as e:
        print "** Unrecognized word.", str(e)
        sys.exit(1)

    # Upper and lower bound
    upper = sum([max(r) for r in results])
    lower = sum([min(r) for r in results])
    return [lower, upper]


if __name__ == '__main__':
    print "Processing."
    words = sys.argv[-1].split()

    lower, upper = count_syllables(words)
    if upper is not lower:
        print "Between", lower, "and", upper, "syllables in", " ".join(words)
    else:
        print upper, "syllables in", " ".join(words)
