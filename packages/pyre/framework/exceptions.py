# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


class PyreError(Exception):
    """
    Base class for all pyre related errors
    """

    def __init__(self, description, **kwds):
        super().__init__(**kwds)
        self.description = description
        return

    def __str__(self):
        return self.description


class FrameworkError(PyreError):
    """
    Base class for all framework exceptions

    Useful when you are trying to catch any and all pyre framework errors
    """


class BadResourceLocatorError(FrameworkError):
    """
    Exception raised when a URI is not formed properly
    """

    def __init__(self, uri, reason, **kwds):
        self.uri = uri
        self.reason = reason
        super().__init__(description="{0.uri}: {0.reason}".format(self), **kwds)
        return


class SymbolNotFoundError(FrameworkError):

    def __init__(self, shelf, symbol, **kwds):
        msg = "symbol {!r} not found".format(symbol)
        super().__init__(description=msg, **kwds)
        self.symbol = symbol
        return
                 

# end of file 
