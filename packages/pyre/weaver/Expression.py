# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#

# access the operator module
import operator


class Expression:
    """
    This mill mix-in builds textual representations of expression trees built out of
    {pyre.algebraic.Node} subclasses
    """


    # types
    from .. import algebraic


    # interface
    def expression(self, root, **kwds):
        """
        Build a representation of {node}, assumed to be an instance of a {pyre.algebraic.Node}
        subclass
        """
        return self._renderers[root.__class__](root, **kwds)


    # meta methods
    def __init__(self, nodeType=None, **kwds):
        super().__init__(**kwds)

        # make sure we can hold of the type hierarchy
        if nodeType is None:
            from ..algebraic.Node import Node as nodeType
        # build the symbol table
        self._symbols = self._newSymbolTable()
        # initialize the table of renderers
        self._renderers = self._newRenderingStrategyTable(nodeType=nodeType)

        return


    # implementation details
    def _newSymbolTable(self):
        """
        Build a table mapping all {pyre.algebraic} operators to their 'default' symbols

        This table is built by considering the python representation of the operator to be its
        default. Other mills can build their own tables, or start with this one and modify it as
        needed
        """
        # build the symbol table
        symbols = {
            # support for {Number}
            operator.add: "+",
            operator.sub: "-",
            operator.mul: "*",
            operator.truediv: "/",
            operator.floordiv: "//",
            operator.mod: "%",
            operator.pow: "**",
            operator.neg: "-",
            operator.abs: "abs",
            # support for {Boolean}
            operator.and_: "and",
            operator.or_: "or",
            # support for {Ordering}
            operator.eq: "==",
            operator.ne: "!=",
            operator.le: "<=",
            operator.ge: ">=",
            operator.lt: "<",
            operator.gt: ">",
            }
        # and return it
        return symbols


    def _newRenderingStrategyTable(self, nodeType):
        """
        Build a table that maps {pyre.algebraic} operators to rendering strategies
        """
        # grab the types that handles literal values and operations
        # pardon the weirdness: {literal} and {operation} are property descriptors in {nodeType}
        literal = nodeType.literal.fget(None)
        variable = nodeType.variable.fget(None)
        operation = nodeType.operator.fget(None)
        # build the symbol table
        handlers = {
            # nodes
            literal: self._literalRenderer,
            variable: self._literalRenderer,
            operation: self._operatorRenderer,
            # operators
            # arithmetic
            operator.add: self._binaryOperatorRenderer,
            operator.sub: self._binaryOperatorRenderer,
            operator.mul: self._binaryOperatorRenderer,
            operator.truediv: self._binaryOperatorRenderer,
            operator.floordiv: self._binaryOperatorRenderer,
            operator.mod: self._binaryOperatorRenderer,
            operator.pow: self._binaryOperatorRenderer,
            operator.abs: self._absoluteRenderer,
            operator.neg: self._oppositeRenderer,
            # comparisons
            operator.eq: self._binaryOperatorRenderer,
            operator.ne: self._binaryOperatorRenderer,
            operator.le: self._binaryOperatorRenderer,
            operator.ge: self._binaryOperatorRenderer,
            operator.lt: self._binaryOperatorRenderer,
            operator.gt: self._binaryOperatorRenderer,
            # logical
            operator.and_: self._binaryOperatorRenderer,
            operator.or_: self._binaryOperatorRenderer,
            }

        # and return it
        return handlers


    def _literalRenderer(self, node, **kwds):
        """
        Render {node} as a literal
        """
        # return the literal representation
        return str(node.value)


    def _operatorRenderer(self, node, **kwds):
        """
        Render {node} assuming it is an operation of some kind
        """
        # get the operator
        op = node._operator
        # lookup the operator specific handler
        handler = self._renderers[op]
        # and invoke it
        return handler(node, **kwds)


    def _binaryOperatorRenderer(self, node, **kwds):
        """
        Render {node} assuming it is an operator
        """
        # extract the operands
        left, right = node._operands
        # render the left operand
        op1 = self._renderers[type(left)](node=left, **kwds)
        # render the right operand
        op2 = self._renderers[type(right)](node=right, **kwds)
        # look up the operator symbol
        symbol = self._symbols[node._operator]
        # put it all together
        return "({}) {} ({})".format(op1, symbol, op2)


    def _unaryOperatorRenderer(self, node, **kwds):
        """
        Render {node} assuming it is an operator
        """
        # get the operand: unpack as a tuple to catch mistakes
        operand, = node._operands
        # render it
        op = self._renderers[type(operand)](node=operand, **kwds)
        # look up the operator symbol
        symbol = self._symbols[node._operator]
        # put it all together
        return "{}({})".format(symbol, op)


    def _absoluteRenderer(self, node, **kwds):
        """
        Render the absolute value of {node}
        """
        # get the operand: unpack as a tuple to catch mistakes
        operand, = node._operands
        # render it
        op = self._renderers[type(operand)](node=operand, **kwds)
        # decorate and return
        return "{}({})".format(self._symbols[node._operator], op)


    def _oppositeRenderer(self, node, **kwds):
        """
        Render the absolute value of {node}
        """
        # get the operand: unpack as a tuple to catch mistakes
        operand, = node._operands
        # render it
        op = self._renderers[type(operand)](node=operand, **kwds)
        # decorate and return
        return "-({})".format(op)


# end of file 
