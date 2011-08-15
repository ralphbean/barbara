#!/usr/bin/env python
""" Drop to shell to use espeak.

PyTTSx exists and rocks but it can't write to file.  Therefore, we have to be
lame.

"""

import sys
import subprocess as sp

if __name__ == '__main__':
    print "Processing."
    words = sys.argv[-1].split()

    something = sp.Popen(['espeak', '-w', 'test.wav'] + words)
    print something


