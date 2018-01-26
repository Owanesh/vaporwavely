import string
import random

from utils import dictionary, alphabet



def vaporize(payload):
    for k, v in alphabet.items():
        payload = payload.replace(k, v)
    return payload


def vaporipsum(number_of_paragraph=1):
    vaporipsum_final= " "
    for _ in range(number_of_paragraph):
        paragraph = random.sample(dictionary, len(dictionary))
        vaporipsum_final += " ".join(paragraph) + '\n\n'

    return vaporipsum_final
