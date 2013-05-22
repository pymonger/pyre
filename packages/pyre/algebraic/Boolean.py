# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


import operator


# declaration
class Boolean:
    """
    This is a mix-in class that traps the boolean operators

    The point is to redirect boolean operations among instances of subclasses of {Boolean} to
    methods defined in these subclasses. These methods then build and return representations of
    the corresponding operators and their operands.

    {Boolean} expects its subclasses to define two class methods: {literal} and
    {operator}. The former is used to encapsulate operands that are not {Boolean}
    instances. The latter is used to construct the operator representations
    """


    # logical operations
    def __and__(self, other):
        # if {other} is not a node
        if not isinstance(other, Boolean):
            # promote it
            other = self.literal(value=other)
        # build a representation of the equality test
        return self.operator(evaluator=operator.and_, operands=[self, other])


    def __or__(self, other):
        # if {other} is not a node
        if not isinstance(other, Boolean):
            # promote it
            other = self.literal(value=other)
        # build a representation of the equality test
        return self.operator(evaluator=operator.or_, operands=[self, other])


    # the reflections
    def __rand__(self, other):
        # if {other} is not a node
        if not isinstance(other, Boolean):
            # promote it
            other = self.literal(value=other)
        # build a representation of the equality test
        return self.operator(evaluator=operator.rand, operands=[other, self])


    def __ror(self, other):
        # if {other} is not a node
        if not isinstance(other, Boolean):
            # promote it
            other = self.literal(value=other)
        # build a representation of the equality test
        return self.operator(evaluator=operator.ror, operands=[other, self])


    # in-place
    def __iand__(self, other):
        # if {other} is not a node
        if not isinstance(other, Boolean):
            # promote it
            other = self.literal(value=other)
        # build a representation of the equality test
        return self.operator(evaluator=operator.iand, operands=[self, other])


    def __ior(self, other):
        # if {other} is not a node
        if not isinstance(other, Boolean):
            # promote it
            other = self.literal(value=other)
        # build a representation of the equality test
        return self.operator(evaluator=operator.ior, operands=[self, other])


# end of file 
