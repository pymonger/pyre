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

test: sanity evaluators resolution model hierarchical

sanity:
	${PYTHON} ./sanity.py
	${PYTHON} ./exceptions.py
	${PYTHON} ./node.py

evaluators:
	${PYTHON} ./explicit.py
	${PYTHON} ./probe.py
	${PYTHON} ./reference.py
	${PYTHON} ./sum.py
	${PYTHON} ./aggregators.py
	${PYTHON} ./reductors.py
	${PYTHON} ./operations.py
	${PYTHON} ./algebra.py
	${PYTHON} ./expression.py

resolution:
	${PYTHON} ./patch.py

model:
	${PYTHON} ./model.py

hierarchical:
	${PYTHON} ./hierarchical.py
	${PYTHON} ./hierarchical_patch.py
	${PYTHON} ./hierarchical_alias.py
	${PYTHON} ./hierarchical_group.py


# end of file 
