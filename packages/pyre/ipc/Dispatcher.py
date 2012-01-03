# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis, leif strand
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# externals
import pyre


# declaration
class Dispatcher(pyre.interface, family="pyre.ipc.dispatchers"):
    """
    Interface definition for components that monitor communication channels and invoke handlers
    when activity is detected
    """ 


    # default implementation
    @classmethod
    def default(cls):
        """
        The suggested implementation of the {Dispatcher} interface
        """
        # {Selector} is the only choice currently
        from .Selector import Selector
        return Selector


    # interface
    @pyre.provides
    def watch(self):
        """
        Enter an indefinite loop of monitoring all registered event sources and invoking the
        registered event handlers
        """

    @pyre.provides
    def stop(self):
        """
        Stop monitoring all communication channels
        """

    # event scheduling
    @pyre.provides
    def alarm(self, interval, handler):
        """
        Schedule {handler} to be invoked after {interval} elapses. {interval} is expected to be
        a dimensional quantity from {pyre.units} with units of time
        """

    @pyre.export
    def notifyOnReadReady(self, fd, handler):
        """
        Add {handler} to the list of routines to call when {fd} is ready to be read
        """

    @pyre.export
    def notifyOnWriteReady(self, fd, handler):
        """
        Add {handler} to the list of routines to call when {fd} is ready to be written
        """

    @pyre.export
    def notifyOnException(self, fd, handler):
        """
        Add {handler} to the list of routines to call when something exceptional has happened
        to {fd}
        """


# end of file 