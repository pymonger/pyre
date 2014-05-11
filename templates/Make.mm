# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#


PROJECT = pyre

TEMPLATES = \
    class.c++ \
    class.python \
    project

#
all: export

#
TEMPLATE_DIR = $(EXPORT_ROOT)/templates
export::
	@$(RM_RF) $(TEMPLATE_DIR)
	@$(MKDIR) $(MKPARENTS) $(TEMPLATE_DIR)
	@$(CP_R) $(TEMPLATES) $(TEMPLATE_DIR)


# end of file 
