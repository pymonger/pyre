#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


"""
Check that interfaces with properties havethe expected layout
"""


def test():
    import pyre

    # declare
    class interface(pyre.interface):
        """a trivial interface"""
        p = pyre.property()

    # check the basics
    assert interface.__name__ == "interface"
    assert interface.__bases__ == (pyre.interface,)
    # check the layout
    assert interface.pyre_name == "interface"
    assert interface.pyre_state == "registered"
    assert interface.pyre_namemap == {'p': 'p'}
    assert interface.pyre_pedigree == (interface, pyre.interface)
    # traits
    localNames = ['p']
    localTraits = tuple(map(interface.pyre_getTraitDescriptor, localNames))
    assert interface.pyre_localTraits == localTraits
    assert interface.pyre_inheritedTraits == ()
    allNames = localNames + []
    allTraits = tuple(map(interface.pyre_getTraitDescriptor, allNames))
    assert tuple(interface.pyre_getTraitDescriptors()) == allTraits
    
    return interface


# main
if __name__ == "__main__":
    test()


# end of file 
