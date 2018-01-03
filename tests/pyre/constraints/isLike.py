#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2018 all rights reserved
#


"""
Exercise "isLike"
"""


def test():
    import pyre.constraints

    phone = r"(\+\d+\s+)?\(?\d{3}\)?(.|\s+)\d{3}[-.]\d{4}"
    constraint = pyre.constraints.isLike(regexp=phone)

    constraint.validate("(877) 877-0987")
    constraint.validate("(877) 877.0987")
    constraint.validate("877.877.0987")
    constraint.validate("+1 877.877.0987")

    stranger = "(877) 877-097"
    try:
        constraint.validate(stranger)
    except constraint.ConstraintViolationError as error:
        assert error.constraint == constraint
        assert error.value == stranger
        # print(error)

    return constraint


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file
