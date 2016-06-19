#! /usr/local/bin/python3
import sys

from pyknon.genmidi import Midi
from pyknon.music import Note
from pyknon.music import Rest
from pyknon.music import NoteSeq

# TODO: 
#   * add commandline argument support (ie *i for image *> midi, *m for midi *>
#   image)
#
#   * add error handling
#
#   * implement auxilary functions:
#       - pix2noteseq:
#           - pix2note:
#               - blue -> note letter
#               - green -> octave
#               - red -> length
#               - brightness -> volume
#       - note -> pixel:
#           /!\ Important prerequisite: figure out how to open & read a midi
#           file in python /!\
#           - note -> R
#           - note -> G
#           - note -> B
#           - note -> etc...

if __name__ == "__main__":

    # mode == '-i' | '-m'
    modes = ['-i', '-m']
    mode = sys.argv[1]
    if mode not in modes:
        raise Exception('wrong mode')

    filepath = sys.argv[1]

    if mode == '-i':
        image = Image.open(filepath)
        pixels = image.load()

        # Main Loop, generates notes from pixel RGB values
        notes = pix2noteseq(pixels)

    elif mode == '-m':
        # TODO
        pass
