# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# declaration
class Evaluator:
    """
    A strategy for pulling data from a stream, and performing evaluations and coercions as
    indicated by the field descriptors
    """


    # meta methods
    def __call__(self, record, source, **kwds):
        """
        Pull values from {source}, perform the calculation encoded in the derivation expression
        graphs, walk values through coercions, and make the results available to the caller
        """
        # in the presence of derivations, we must cache the values of fields that have been
        # converted previously; set up a cache
        cache = {}
        # go through the fields in {record}
        for field in record.pyre_fields:
            # and ask it to dispatch to the appropriate field handler, which will perform all
            # necessary evaluations and conversions
            value = field.identify(authority=self, cache=cache, source=source)
            # update the cache (only for descriptors that actually appear in the record)
            cache[field] = value
            # make the value available
            yield value
        # all done
        return


    # implementation details
    def onDescriptor(self, source, cache, descriptor):
        """
        Handler for measures
        """
        # if i have been asked for the value of this {descriptor} before
        try:
            # get it
            value = cache[descriptor]
        # if not
        except KeyError:
            # grab one from the data stream
            value = next(source)
            # coerce
            value = descriptor.coerce(value)
        # and make it available
        return value


    def onOperator(self, source, cache, descriptor):
        """
        Handler for operators
        """
        # if I have been asked for the value of this {descriptor} before
        try:
            # get it
            value = cache[descriptor]
        # if not
        except KeyError:
            # compute the values of each of its operands
            values = tuple(
                # by converting
                op.identify(authority=self, cache=cache, source=source)
                # each operand
                for op in descriptor.operands)
            # compute the raw value of this descriptor by applying its evaluator
            value = descriptor.evaluator(*values)
            # coerce the value
            value = descriptor.coerce(value)
        # and make it available
        return value


    def onLiteral(self, source, cache, descriptor):
        """
        Handler for descriptors that encapsulate foreign values
        """
        # not much to do
        return descriptor._value


# end of file