import json
import random


def blns():
    """Get all blns in an array"""
    with open('blns.json') as data_file:
        blns = json.load(data_file)
    return blns


def naughty_string():
    """One Random String"""
    return random.choice(blns())
