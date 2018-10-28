import random
from .utils import dictionary


def vaporize(payload):
    alphabet_distance = ord('Ａ') - ord('A')
    # 65248, a distance between alphabets
    # ^- count difference from first char of normal alphabet
    # and first char of vaporwave alphabet
    new_payload = ''
    for char in payload:
        pos_norm_char = ord(char)  # define position of actual char
        if ord('!') <= pos_norm_char <= ord('~'):
            # these two char are limit of alphabet
            char = chr(pos_norm_char + alphabet_distance)
        #shift payload char from normal alphabet to vaporwave alphabet
        new_payload += char
    return new_payload
    # thanks to https://github.com/jonesmartins/vapyrwave/
    # for better implementation of vaporwave alphabet


def vaporipsum(number_of_paragraph=1):
    #defaults to 1 paragraph
    vaporipsum_final = ' '
    for _ in range(number_of_paragraph):
        #generate paragraph
        paragraph = random.sample(dictionary, len(dictionary))
        #join paragraphs separated by new lines
        vaporipsum_final += ' '.join(paragraph) + '\n\n'

    return vaporipsum_final
