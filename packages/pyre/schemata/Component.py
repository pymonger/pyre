# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2016 all rights reserved
#


# superclass
from .Schema import Schema


# declaration
class Component(Schema):
    """
    A type declarator for components
    """


    # types
    from . import uri

    # constants
    default = object()
    typename = 'component' # the name of my type

    # public data
    protocol = None


    # interface
    def coerce(self, value, **kwds):
        """
        Attempt to convert {value} into a component class compatible with my protocol
        """
        # get my protocol
        protocol = self.protocol
        # which knows the actor type
        actor = protocol.actor
        # the component type
        component = protocol.component
        # and the factory of its default value
        default = protocol.pyre_default

        # if {value} is my protocol's {pyre_default} classmethod
        if value == default:
            # evaluate it
            value = value()
            # and if it's none, we are done
            if value is None: return None

        # give {value} a try
        if isinstance(value, actor) or isinstance(value, component): return value

        # the only remaining case that i can handle is {value} being a string; if it's not
        if not isinstance(value, str):
            # build an error message
            msg = 'could not convert {0.value} into a component'
            # and complain
            raise self.CastingError(value=value, description=msg) from None

        # ok, we have a string; strip it
        value = value.strip()
        # check for none
        if value.lower() == "none":
            # and do as instructed
            return None

        # ask the protocol
        try:
            # to have a pass at resolving the uri into a compatible component; this handles
            # both uris that point to a retrievable component and uris that point to existing
            # instances known to the executive
            return protocol.pyre_resolveSpecification(spec=value, **kwds)
        # if that fails
        except protocol.ResolutionError:
            # no worries; more to try
            pass

        # another valid possibility is a specification like
        #
        #   --facility=#name
        #
        # this is interpreted as a request to instantiate the default facility value with the
        # given name

        # convert the {value} into a uri; if the conversion is not successful, the {uri} schema
        # will complain
        uri = self.uri().coerce(value)
        # extract the fragment, which we use as the instance name; it's ok if it's {None}
        instanceName = uri.fragment
        # extract the address, which we use as the component specification; it's ok if it's {None}
        componentSpec = uri.address

        # if we have an instance name but no component specification
        if instanceName and not componentSpec:
            # get my default value
            factory = self.default
            # if it is the protocol default method
            if factory == default:
                # invoke it
                factory = factory()
            # now, if it is a component constructor
            if isinstance(factory, actor):
                # use it to build a component instance
                candidate = factory(name=instanceName)
                # and return it
                return candidate

        # out of ideas; build an error message and complain
        raise protocol.ResolutionError(protocol=protocol, value=value) from None


    # meta-methods
    def __init__(self, protocol, default=default, **kwds):
        # chain up
        super().__init__(default=default, **kwds)
        # save my protocol
        self.protocol = protocol
        # all done
        return


# end of file
