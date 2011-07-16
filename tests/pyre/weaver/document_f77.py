#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


"""
Exercise a Fortran77 weaver
"""


def test():
    # get the package
    import pyre.weaver
    # instantiate a weaver
    weaver = pyre.weaver.newWeaver(name="sanity")
    weaver.language = "f77"

    text = list(weaver.weave())
    assert text == [
        'c -*- Fortran -*-',
        'c',
        'c Michael A.G. Aïvázis',
        'c California Institute of Technology',
        'c (c) 1998-2011 All Rights Reserved',
        'c',
        '',
        '',
        'c end of file',
        ]

    return


# main
if __name__ == "__main__":
    test()


# end of file 