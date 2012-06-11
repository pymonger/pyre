#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


"""
Exercise max reductions
"""


def test():
    # access the package
    import mpi
    # get the world communicator
    world = mpi.world
    # and its structure
    rank = world.rank
    size = world.size
    # set up a root for the reduction
    root = int(size / 2)
    # create a value
    number = rank**2
    # perform the reduction
    largest = world.max(item=number, root=root)
    # check it
    if rank == root:
        assert largest == (size-1)**2
    # all done
    return


# main
if __name__ == "__main__":
    test()


# end of file 
