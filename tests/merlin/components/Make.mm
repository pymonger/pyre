# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


PROJECT = pyre

#--------------------------------------------------------------------------
#

all: test

test: sanity merlin

sanity:
	${PYTHON} ./sanity.py

merlin:
	${PYTHON} ./merlin-shell.py
	${PYTHON} ./merlin-spell.py
	${PYTHON} ./merlin-curator.py


# end of file 
