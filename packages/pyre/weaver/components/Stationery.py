# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


# packages
import pyre


# declaration
class Stationery(pyre.interface, family="pyre.weaver.layouts"):
    """
    The interface that layout strategies must implement
    """


    # traits
    author = pyre.properties.str()
    author.doc = "the name of the entity to blame for this content"

    affiliation = pyre.properties.str()
    affiliation.doc = "the author's institutional affiliation"

    copyright = pyre.properties.str()
    affiliation.doc = "the author's institutional affiliation"


    # utilities
    @classmethod
    def default(cls):
        """
        Choose a layout as the default
        """
        # the current default is {Banner}
        from .Banner import Banner
        return Banner


# end of file 