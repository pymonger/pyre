# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


class Accessor:
    """
    Descriptor that provides access to a record item
    """


    # public data
    index = None # the index of my value in the data tuple
    entry = None # the entry with the meta data


    # meta methods
    def __init__(self, index, entry, **kwds):
        super().__init__(**kwds)
        self.index = index
        self.entry = entry
        return


    # descriptor interface
    def __get__(self, record, cls):
        """
        Retrieve the value of my entry from {record}
        """
        try:
            return record[self.index]
        except TypeError:
            return self.entry


    def __set__(self, record, value):
        """
        Store {value} in my {record} entry
        """
        # get the {record} to assign the value at the right spot
        record[self.index] = value
        # all done
        return


# end of file 
