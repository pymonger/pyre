#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


"""
Verify direct access to the namespace
"""


def test():
    # access the package
    import pyre
    # and the nameserver
    nameserver = pyre.executive.nameserver

    # create some assignments
    nameserver["sample.user.name"] = "Michael Aïvázis"
    nameserver["sample.user.name"] = "michael aïvázis"
    nameserver["sample.user.email"] = "michael.aivazis@caltech.edu"
    nameserver["sample.user.affiliation"] = "california institute of technology"
    nameserver["sample.user.alias"] = "{sample.user.name}"

    # dump the contents of the model
    # nameserver.dump()

    # check the variable bindings
    assert nameserver["sample.user.name"] == "michael aïvázis"
    assert nameserver["sample.user.email"] == "michael.aivazis@caltech.edu"
    assert nameserver["sample.user.affiliation"] == "california institute of technology"
    assert nameserver["sample.user.alias"] == nameserver["sample.user.name"]

    # and return the managers
    return nameserver


# main
if __name__ == "__main__":
    test()


# end of file 