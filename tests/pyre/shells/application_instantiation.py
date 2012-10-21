#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


"""
Sanity check: verify that the application component is accessible
"""


def test():
    # get access to the framework
    import pyre

    # declare a trivial application
    class application(pyre.application, family="sample"):
        """A trivial pyre application"""
    
    # instantiate
    return application(name="app")


# main
if __name__ == "__main__":
    test()


# end of file 