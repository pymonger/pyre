# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# externals
import os
import pyre


# superclasses
from .Spell import Spell


# declaration
class AssetManager(Spell):
    """
    Attempt to classify a folder as an asset container and add it to the project
    """


    # class interface
    # interface
    @pyre.export
    def main(self, *args, **kwds):
        """
        This is the action of the spell
        """
        # check
        try:
            # whether this project is initialized
            project = self.vfs['project']
        # if it isn't
        except self.vfs.NotFoundError:
            # complain
            return self.error.log("not a merlin project; did you forget to cast 'merlin init'?")
        # get hold of my local filesystem
        local = self.vfs['/local']
        # dump it
        # local.dump()
        # the first argument is supposed to be a subdirectory of the current directory
        target = args[0] if args else '.'
        # the first argument is supposed to be a subdirectory of the current directory
        names = tuple(filter(None, target.split(local.separator))) if args else ()
        # starting with the current directory
        folder = local
        # drill down until we reach the target folder
        for name in names: 
            # attempt to
            try:
                # populate the current folder
                folder.discover(levels=1)
                # access a sub folder under {name}
                folder = folder.contents[name]
            # if not there
            except KeyError:
                # build an error message
                error = local.NotFoundError(
                    filesystem=local, node=folder, uri=target, fragment=name)
                # notify the user
                return self.error.log(str(error))
            # if not a folder
            except AttributeError:
                # build an error message
                error = local.FolderError(
                    filesystem=local, node=folder, uri=target, fragment=folder.uri)
                # notify the user
                return self.error.log(str(error))
        # if it is a folder
        if folder.isFolder:
            # make sure it is fully populated
            folder.discover()

        # compute the root of the asset
        root, name = os.path.split(folder.uri)
        # run the target through the asset classifiers to extract the contained assets
        assets = filter(
            None,
            (classifier.classify(root=root, node=folder)
             for classifier in self.merlin.assetClassifiers))

        # iterate over the returned assets and persist them
        for asset in assets: 
            self.merlin.curator.saveAsset(asset)

        # all done
        return


    @pyre.export
    def help(self, **kwds):
        """
        Generate the help screen associated with this spell
        """
        # all done
        return


# end of file 
