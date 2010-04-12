# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


import pyre.tracking


class CommandLine(object):
    """
    Support for parsing the application command line

    The general form of a command line configuration event is
        --key=value
    which creates a configuration event that will bind {key} to {value}.

    This implementation supports the following constructs:
        --key
            set key to None
        --key=value
        --key.subkey=value
            key may have an arbitrary number of period delimited levels
        --(key1,key2)=value
            equivalent to --key1=value and --key2=value; an arbitrary number of comma separated
            key names are allowed
        --key.(key1,key2)=value
        --key.(key1,key2).key3=value
            as above; this form is supported at any level of the hierarchy

    By default, instances of the command line parser use the following literals
        '-': introduces a configuration command
        '=': indicates an assignment
        '.': the separator for multi-level keys
        '(' and ')': the start and end of a key group
        ',': the separator for keys in a group

    If you want to change any of this, you can instantiate a command line parse, modify any of
    its public data, and invoke "buildScanners" to recompute the associated regular expression
    engines
    """


    # public data
    prefix = '-'
    assignment = '='
    fieldSeparator = '.'
    groupStart = '('
    groupSeparator = ','
    groupEnd = ')'

    assignmentScanner = None
    locator = staticmethod(pyre.tracking.newCommandLocator)


    # interface
    def decode(self, configurator, argv):
        """
        Harvest the configuration events in {argv} and store them in {configurator}

        parameters:
            {argv}: a container of strings of the form "--key=value"
            {configurator}: a pyre.config.Configurator compatible instance
        """
        for index,arg in enumerate(argv):
            # look for an assignment
            match = self.assignmentScanner.match(arg)
            # process it if it matches
            if match:
                # get the tokens from the scanner
                key = match.group("key")
                value = match.group("value")
                if key:
                    # if a key were specified
                    self._processAssignments(configurator, key,value, self.locator(arg=index))
                else:
                    # we ran in to a '-' or '--' that signals the end of configuration options
                    self._processArguments(configurator, *argv[index+1:])
                    break
            # else it must be a regylar command line argument
            else:
                self._processArguments(configurator, arg)
        # all done; return the configurator
        return configurator


    def buildScanners(self):
        """
        Build the command line recognizers that are used to detect the supported command line
        argunent syntactical forms
        """
        import re

        # the assignment recognizer regular expression
        regex = []
        # add the prefix
        if self.prefix:
            regex.append(r'(?P<prefix>' + self.prefix + r'{1,2})')
        # and the 'key=value' form
        regex += [
            # the key
            r'(?P<key>[^', self.assignment, r']*)',
            # the optional assignment symbol
            self.assignment, r'?',
            # and the optional value
            r'(?P<value>.+)?'
            ]
        # compile this pattern
        self.assignmentScanner = re.compile("".join(regex))

        # all done
        return
                    

    # meta methods
    def __init__(self, **kwds):
        super().__init__(**kwds)
        # build the scanners
        self.buildScanners()
        # all done
        return


    # implementation details
    def _processAssignments(self, configurator, key, value, locator):
        """
        Handler for command line arguments that were interpreted as assignments

        Look for the supported shorthands and unfold them into canonical forms.
        """


    def _processArguments(self, configurator, *args):
        """
        Interpret {args} as application commands and store them in {configurator}
        """


# end of file 
