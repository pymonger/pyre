#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


"""
Verify that the trait defaults get bound correctly
"""


def test():
    import pyre

    # declare a component
    class base(pyre.component):
        """the base component"""
        positive = pyre.properties.int(default=0)
        positive.validators = (pyre.constraints.isGreaterEqual(value=0), )

        interval = pyre.properties.int(default=0)
        interval.validators = (
            pyre.constraints.isGreaterEqual(value=-1), pyre.constraints.isLess(value=1))

    # instantiate
    b = base(name="b")
    # make an assignment that violates the constraint
    try:
        b.positive = -1
        assert False
    except b.ConstraintViolationError:
        pass

    # and another
    try:
        b.interval = 1
        assert False
    except b.ConstraintViolationError:
        pass

    return


# main
if __name__ == "__main__":
    test()


# end of file 