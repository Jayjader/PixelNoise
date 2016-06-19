#! /usr/local/bin/python3
import sys
import math

from pyknon.genmidi import Midi
from pyknon.music import Note
from pyknon.music import Rest
from pyknon.music import NoteSeq

from PIL import Image

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
def pix2note(pixel):
    """
    Converts an RGB pixel into a PyKnon Note

    Red -> duration
    Green -> octave
    Blue -> exact note
    Overall Brightness -> volume

    Use:
        pix2note(pixel)

    Arguments:
        pixel: a 3-uple representing the RGB values of the pixel
    """
    letters = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    print(pixel)
    r, g, b = pixel

    # Red is the duration in beats, a full red value (of 255) will last 16
    # beats, or 4 measures of 4:4
    duration = r / 16

    # Green is the octave number, it is calculated assuming 8 octaves (from 0
    # to 7)
    octave = g // 32 + 1

    # Blue is the note letter
    letter = letters[math.floor(b // (256 / 12))]

    # Overall Brightness is the volume
    volume = 0.375*r + 0.5*g + 0.125*b

    return Note(letter + str(octave), duration)


def pix2noteseq(pixelmap, width, height):
    """
    Convert a PIL pixel map to a PyKnon NoteSeq

    Use:
        pix2noteseq(pixelmap)

    Arguemnts:
        pixelmap: the PIL pixel map of the image
        width: the width in pixels
        height: height in pixels

    This function presumes the pixel map is in RGB and correct behavior when
    otherwise is not at all guaranteed.
    """
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

    filepath = sys.argv[2]

    if mode == '-i':
        image = Image.open(filepath)
        width, height = image.size
        pixels = image.load()

        # Main Loop, generates notes from pixel RGB values
        notes = pix2noteseq(pixels, width, height)

    elif mode == '-m':
        # TODO
        pass
