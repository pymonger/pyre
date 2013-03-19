# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


PROJECT = pyre
PACKAGE = framework
PROJ_DISTCLEAN = $(EXPORT_MODULEDIR)/$(PACKAGE)


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    Client.py \
    Executive.py \
    Externals.py \
    FileServer.py \
    Linker.py \
    NameServer.py \
    Package.py \
    Priority.py \
    Pyre.py \
    Slot.py \
    exceptions.py \
    __init__.py

export:: export-package-python-modules

# end of file 
