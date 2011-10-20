# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


PROJECT = pyre

#--------------------------------------------------------------------------
#

working: queries

all: test

test: sanity tables queries

sanity:
	${PYTHON} ./sanity.py

tables:
	${PYTHON} ./table_declaration.py
	${PYTHON} ./table_inheritance.py
	${PYTHON} ./table_instantiation.py
	${PYTHON} ./table_create.py
	${PYTHON} ./table_references.py
	${PYTHON} ./table_annotations.py
	${PYTHON} ./table_insert.py
	${PYTHON} ./table_delete.py
	${PYTHON} ./table_update.py

queries:
	${PYTHON} ./query_star.py


# end of file 
