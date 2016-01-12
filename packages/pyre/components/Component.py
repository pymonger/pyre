# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2016 all rights reserved
#


# externals
import itertools
from .. import tracking
# superclass
from .Configurable import Configurable
# metaclass
from .Actor import Actor


# class declaration
class Component(Configurable, metaclass=Actor, internal=True):
    """
    The base class for all components
    """


    # types
    from .PublicInventory import PublicInventory
    from .PrivateInventory import PrivateInventory
    from ..constraints.exceptions import ConstraintViolationError


    # framework data
    pyre_inventory = None # my inventory management strategy
    pyre_implements = None # my protocol
    pyre_isComponent = True

    # introspection
    @property
    def pyre_key(self):
        """
        Look up my key
        """
        # get my inventory
        inventory = self.pyre_inventory
        # and ask it for my key; if i don't have one bail
        return inventory.key if inventory is not None else None


    @property
    def pyre_name(self):
        """
        Look up my name
        """
        # get my inventory
        inventory = self.pyre_inventory
        # and ask it for my name; if i don't have one bail
        return inventory.name if inventory is not None else None


    @classmethod
    def pyre_family(cls):
        """
        Deduce my family name
        """
        # get my inventory
        inventory = cls.pyre_inventory
        # ask it for my name; if i don't have one, bail
        return inventory.name if inventory is not None else None


    @property
    def pyre_spec(self):
        """
        Build my configuration specification
        """
        # get my name
        name = self.pyre_name or "<none>"
        # and my family name
        family = self.pyre_family() or "<none>"
        # build the spec and return it
        return "{} # {}".format(family, name)


    @classmethod
    def pyre_package(cls):
        """
        Deduce my package name
        """
        # get my inventory to answer this
        return cls.pyre_inventory.package


    @classmethod
    def pyre_isPublicClass(cls):
        """
        Check whether this component class is public
        """
        # depends on what kind of inventory i have; if I have a public one
        if isinstance(cls.pyre_inventory, cls.PublicInventory):
            # i am public
            return True
        # if my inventory is  private
        if isinstance(cls.pyre_inventory, cls.PrivateInventory):
            # i am not public
            return False
        # oops, this is a bug
        import journal
        # complain
        raise journal.firewall('pyre.components').log('unknown component class type')


    # framework notifications
    def pyre_registered(self):
        """
        Hook that gets invoked by the framework after the component instance has been
        registered but before any configuration events
        """
        return self


    def pyre_configured(self):
        """
        Hook that gets invoked by the framework after the component instance has been
        configured but before the binding of any of its traits
        """
        # return the list of errors encountered while checking the configuration
        return []


    def pyre_initialized(self):
        """
        Hook that gets invoked by the framework right before the component is put into
        action. The component is now in a known good state, with all configurable traits fully
        bound and validated. This is the place where the component should acquire whatever
        further resources it requires.
        """
        # return the list of errors encountered while checking the instance state and acquiring
        # resources
        return []


    def pyre_finalized(self):
        """
        Hook that gets invoked by the framework right before the component is decommissioned.
        The instance should release all acquired resources.
        """
        return self


    # introspection
    @classmethod
    def pyre_getExtent(cls):
        """
        Return the extent of this class, i.e. the set of its instances
        """
        # the registrar knows
        return cls.pyre_registrar.components[cls]


    def pyre_slot(self, attribute):
        """
        Return the slot associated with {attribute}
        the locator of the component
        """
        # find the trait
        trait = self.pyre_trait(alias=attribute)
        # look up the slot associated with this trait and return it
        return self.pyre_inventory[trait]


    def pyre_where(self, attribute=None):
        """
        Return the locator associated with {attribute}; if no attribute name is given, return
        the locator of the component
        """
        # if no name is given, return my locator
        if attribute is None: return self.pyre_locator
        # otherwise, find the slot
        slot = self.pyre_slot(attribute=attribute)
        # and return its locator
        return slot.locator


    # meta methods
    def __new__(cls, name, locator, **kwds):
        # build the instance; in order to accommodate components with non-trivial constructors,
        # we have to swallow any extra arguments passed to {__new__}; unfortunately, this
        # places some restrictions on how components participate in class hierarchies: no
        # ancestor of a user component can implement a {__new__} with non-trivial signature,
        # since it will never get its arguments. Sorry...

        # NYI: a possible work-around is to introduce a dummy class in the ancestry whose only
        # job is to swallow all extra arguments; this class can be injected automatically at
        # the end of the list of bases by {Actor}, making this entire process transparent to
        # the user
        instance = super().__new__(cls)

        # record the locator
        instance.pyre_locator = locator
        # deduce the visibility of this instance
        visibility = cls.PrivateInventory if name is None else cls.PublicInventory
        # invoke it to initialize the instance and collect configuration errors
        instance.pyre_configurationErrors = list(
            visibility.initializeInstance(instance=instance, name=name)
            )

        # all done
        return instance


    def __init__(self, name, locator, **kwds):
        # only needed to swallow the extra arguments
        super().__init__(**kwds)
        # all done
        return


    def __str__(self):
        # accumulate the name fragments here
        fragments = []
        # get my name
        name = self.pyre_name
        # if i have one:
        if name is not None:
            # use it
            fragments.append('component {!r}'.format(name))
        # get my family name
        family = self.pyre_family()
        # if i have one
        if family:
            # use it
            fragments.append('an instance of {!r}'.format(family))
        # otherwise
        else:
            # leave a marker
            fragments.append('an instance of {!r}'.format(type(self).__name__))
        # assemble
        return ', '.join(fragments)


    def __getattr__(self, name):
        """
        Trap attribute lookup errors and attempt to resolve the name in my inventory's name
        map. This makes it possible to get the value of a trait by using any of its aliases.
        """
        # attempt to
        try:
            # normalize the name
            normal = self.pyre_namemap[name]
        # if it's not one of my traits
        except KeyError:
            # get someone else to do the work
            raise AttributeError("{} has no attribute {!r}".format(self, name)) from None

        # if the normalized name is the same as the original
        if normal == name:
            # nothing further to do but complain: this is almost certainly a framework bug;
            # build an error message
            error = self.TraitNotFoundError(configurable=self, name=name)
            # get the journal
            import journal
            # complain
            raise journal.firewall('pyre.components').log(str(error))

        # if we got this far, restart the attribute lookup using the canonical name
        # N.B.: don't be smart here; let {getattr} do its job, which involves invoking the
        # trait descriptors if necessary
        return getattr(self, normal)


    def __setattr__(self, name, value):
        """
        Trap attribute assignment and attempt to normalize the name before making the assignment
        """
        # with {__setattr__} defined, all assignments come through here; therefore, there is no
        # need for the trait descriptors to define {__set__}: it would never get called unless
        # we chain up here after normalizing the name. this might ok, if it weren't for the
        # fact that it is impossible to guarantee that the locator will be correct in all cases

        # attempt to
        try:
            # normalize the name
            canonical = self.pyre_namemap[name]
        # if the name is not in the name map
        except KeyError:
            # this must a non-trait attribute
            return super().__setattr__(name, value)

        # find the trait
        trait = self.pyre_traitmap[canonical]
        # record the location of the caller
        locator = tracking.here(level=1)
        # set the priority
        priority = self.pyre_executive.priority.explicit()
        # set the value
        self.pyre_inventory.setTrait(trait=trait, factory=trait.instanceSlot,
                                     value=value, priority=priority, locator=locator)

        # all done
        return


    # compatibility check
    @classmethod
    def pyre_isCompatible(cls, spec, fast=True):
        """
        Check whether {cls} is assignment compatible with {spec}, i.e. whether it provides at
        least the properties and behaviors specified by {spec}
        """
        # print("CP: me={}, other={}".format(cls, spec))
        # chain up
        report = super().pyre_isCompatible(spec=spec, fast=fast)
        # if an incompatibility were detected and we are not interested in the full picture
        if fast and not report.isClean:
            # print(' ** early exit: {}'.format(report.incompatibilities))
            # we are done
            return report

        # if {spec} is not a protocol
        if not spec.pyre_isProtocol:
            # we are done
            return report

        # grab my protocol
        protocol = cls.pyre_implements
        # if i don't have one, or i'm checking my own
        if not protocol or protocol == spec:
            # we are done
            return report

        # now, check that my protocol and {spec} are type compatible
        if not protocol.pyre_isTypeCompatible(spec):
            # build an error description
            error = cls.ProtocolCompatibilityError(configurable=cls, protocol=spec)
            # add it to the report
            report.incompatibilities[spec].append(error)
            # bail out if we are in fast mode
            if fast: return report

        # all done
        return report


# end of file
