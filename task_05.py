#!usr/bin/env python
# -*- coding: utf-8 -*-
"""New function for task 5."""


def defaults(my_required, my_optional=True):
    """Does comparison of two arguments.

    Args:
        my_required (mixed): Arg to be compared with my_optional,
        my_optional (bool, mixed): Arg to be compared with my_required. Defult:
        True.

    Returns:
        bool: if my_optional and my_required are identical.

    Examples:
        >>> defaults(True)
        True
        >>> defaults(True, False)
        False
        >>> defaults(1, 1)
        True  """
    return my_optional is my_required
