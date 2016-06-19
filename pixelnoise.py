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

def pix2noteseq(pixelmap):
    """
    Convert a PIL pixel map to a PyKnon NoteSeq

    Use:
        pix2noteseq(pixelmap)

    Arguemnts:
        pixelmap: the PIL pixel map of the image

    This function presumes the pixel map is in RGB and correct behavior when
    otherwise is not at all guaranteed.
    """
    width, height = pixelmap.size
    notes = NoteSeq()
    
    # Iterate over the pixels, starting at the top left and working
    # colomn by colomn
    for y in range(height):
        for x in range(width):
            notes.append(pix2note(pixelmap[x,y]))

    return notes

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
