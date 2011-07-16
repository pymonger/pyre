# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


# access to the framework
import pyre


# declaration
class PackageManager(pyre.component, family="merlin.packages"):
    """
    The component that manages the package archive
    """


    # properties
    hostname = pyre.properties.str()
    hostname.doc = "the name of this machine"


    # interface
    def find(self, uri):
        """
        Locate the package using {uri} as its address
        """
        executive = self.pyre_executive
        # ask the executive to locate the spell factory
        shelf = executive.retrieveComponentDescriptor(uri=uri, context=self)
        print(shelf)



    def shelves(self, name, folder):
        """
        Iterate over the contents of {folder} and return candidate shelves
        """
        # go through the entire contents
        for shelf in folder.contents:
            # everybody is a candidate, for now
            yield folder.join(name, shelf)
        # all done
        return


    # meta methods
    def __init__(self, **kwds):
        super().__init__(**kwds)

        # figure out the hostname
        if not self.hostname:
            import platform
            self.hostname = platform.node()

        return

# end of file 