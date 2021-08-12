# -*- coding: utf-8 -*-
import json
import random

from blns.big_list_of_naughty_strings.naughtystrings import naughty_strings

blns_list = naughty_strings()

def all():
    """Get all blns in an array"""
    return blns_list


def one(min_len=0):
    """One Random String"""
    while(True):
        nl = random.choice(all())
        if(nl.__len__() >= min_len):
            return nl



