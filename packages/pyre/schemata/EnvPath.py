# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2018 all rights reserved
#


# externals
import os
# superclass
from .List import List
# my schema
from .Path import Path


# declaration
class EnvPath(List):
    """
    A list of paths whose default value is tied to the value of an environment variable
    """


    # constants
    typename = 'envpath' # the name of my type


    # meta-methods
    def __init__(self, variable, **kwds):
        # attempt to
        try:
            # get the value of the environment variable
            default = os.environ[variable]
        # if the variable is not defined
        except KeyError:
            # the default is an empty list
            default = []
        # otherwise
        else:
            # split it using the path separator
            default = list(filter(None, default.split(os.pathsep)))

        # chain up
        super().__init__(schema=Path(), default=default, **kwds)

        # save the variable name
        self.envvar = variable
        # all done
        return


    # implementation details
    def _coerce(self, value, **kwds):
        """
        Convert {value} into an iterable
        """
        # all we have to do is split strings using the path separator
        if isinstance(value, str):
            # do the split
            value = value.split(os.pathsep)
        # everything else is handled by my superclass
        return super()._coerce(value=value, **kwds)


# end of file
