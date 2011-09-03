# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


# access to the node algebra
from .Number import Number
from .Ordering import Ordering
from .Boolean import Boolean

# declaration
class Node(Number, Ordering, Boolean):
    """
    This is the base class for hierarchies that implement the algebraic protocol

    The base classes {Number}, {Ordering} and {Boolean} overload the methods that are invoked
    by the evaluation of expressions involving python operators. The implementation of these
    methods expect {Node} to provide access to two subclasses, {Literal} and {Operator}, that
    are used to build a representation of the python expression. {Literal} is used to
    encapsulate objects that are foreign to the {Node} class hierarchy, e.g. integers, and
    {Operation} encodes the operator encountered and its operands. This access must be provided
    through two {Node} properties, {literal} and {operation}, which provide an extra layer of
    abstraction by hiding the actual {Node} subclasses.
    """


    # types
    # hooks for implementing the expression graph construction
    # the default implementation provided by this package uses the classes defined here
    @property
    def literal(self):
        """
        Grant access to the subclass used to encapsulate foreign values
        """
        # important: must return a type, not an instance
        from .Literal import Literal
        return Literal


    @property
    def operator(self):
        """
        Grant access to the subclass used to encapsulate operators
        """
        # important: must return a type, not an instance
        from .Operator import Operator
        return Operator


    # public data
    @property
    def value(self):
        """
        Compute and return my value
        """
        raise NotImplementedError(
            "class {.__class__.__name__!r} must implement 'value'".format(self))


    @property
    def variables(self):
        """
        Traverse my expression graph and return an iterable with all the variables I depend on

        Variables are reported as many times as they show up in my graph. Clients that are
        looking for the set unique dependencies have to prune the results themselves.
        """
        raise NotImplementedError(
            "class {.__class__.__name__!r} must implement 'variables'".format(self))


    # interface
    def substitute(self, replacements):
        """
        Replace variables in my graph that are present in {replacements} with the indicated node
        """
        raise NotImplementedError(
            "class {.__class__.__name__!r} must implement 'substitute'".format(self))


# end of file 
