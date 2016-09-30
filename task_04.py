#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Function with three parameters."""

def too_many_kittens(kittens, litterboxes, catfood):
    """This function counts litterboxes.

        Arg:
            kittens(int) = Just a random number.
            litterboxes (int) = Just a random number.
            catfood (bool) = Arg to take True or False.

        Returns:

            Bool: True if there is enough litterboxes and catfood for kittens.
            False if there is not enough litterboxes and catfood for kittens.

        Example:

            >>>too_many_kittens(12, 12, False)
            True
        
            >>>too_many_kittens(13, 12, True)
            True
     """
    return not (litterboxes >= kittens and catfood)
