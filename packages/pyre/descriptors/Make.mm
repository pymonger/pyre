# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


PROJECT = pyre
PACKAGE = descriptors
PROJ_CLEAN += $(EXPORT_MODULEDIR)/$(PACKAGE)


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    Converter.py \
    Decorator.py \
    Descriptor.py \
    Normalizer.py \
    Processor.py \
    Public.py \
    Typed.py \
    Validator.py \
    exceptions.py \
    __init__.py


export:: export-package-python-modules

# end of file 