#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


"""
Instantiate a script
"""


def test():
    # externals
    import pyre # access the framework

    # declare a trivial application
    class application(pyre.application, family='shells.application'):
        """a sample application"""

        @pyre.export
        def main(self, **kwds):
            print("Hello")
            return 0

    # instantiate it
    app = application(name='κάστωρ')
    # check that its shell was configured correctly
    assert app.shell.pyre_name == 'λήδα'

    # if it is in debugging mode
    if app.shell.debug:
        print("in debugging mode")
        # launch it
        status = app.run()
        # check it
        assert status == 0
        # and return the app
        return app

    # otherwise, launch it and get the channels to the child
    stdout, stderr = app.run()

    # make sure we can read its output correctly
    assert stdout.read(10) == b"Hello\n"

    # and return the app
    return app


# main
if __name__ == "__main__":
    test()


# end of file 
