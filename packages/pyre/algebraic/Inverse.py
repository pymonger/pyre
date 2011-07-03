# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Unary import Unary


class Inverse(Unary):
    """
    A representation of the inverse of a node
    """


    # interface
    def pyre_apply(self, op):
        # return its inverse
        return 1/op


    # meta methods
    def __str__(self):
        return "(1/{0.op})".format(self)


# end of file 
