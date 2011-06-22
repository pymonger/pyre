# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


# access to the pyre package
import pyre


# my interface
from .Stationery import Stationery


class Banner(pyre.component, family="pyre.weaver.banner", implements=Stationery):
    """
    The base component for content generation
    """

    width = pyre.properties.int(default=100)
    width.doc = "the preferred width of the generated text"

    author = pyre.properties.str(default="{pyre.user.name}")
    author.doc = "the name of the entity to blame for this content"

    affiliation = pyre.properties.str(default="{pyre.user.affiliation}")
    affiliation.doc = "the author's institutional affiliation"

    copyright = pyre.properties.str()
    copyright.doc = "the copyright note"

    license = pyre.properties.str()
    license.doc = "the license"

    footer = pyre.properties.str()
    footer.doc = "the marker to drop at the bottom of the document"


# end of file 
