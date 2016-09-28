#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean."""


def know_what_i_mean(wink, numwink=2):
    """Does some string opertions and returns a string.

    Arg:
        wink(str): Arg to be multiplied with whitespace removed.
        numwink (int): Just a random number. Defult: 2.

    Returns:
        str: Formated string with whitespace removed.

    Examples:

        >>>know_what_i_mean(wink='poke ')
        'Know what I mean? poke poke, nudge nudge'

        >>>know_what_i_mean(wink='ring ')
        'Know what I mean? ring ring, nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
