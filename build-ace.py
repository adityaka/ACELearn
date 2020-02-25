from abc import ABCMeta, abstractmethod

class ACEBuilder(object):
    __metaclass__ =ABCMeta

    def __init__(self, ace_root):
        pass

    @property
    def platform(self):
        raise NotImplemented()

    @abstractmethod
    def build():
        pass

class ACELinuxBuilder(ACEBuilder):
    def build():
        print("Building on a Linux System")
        # TODO: write the build logic for linux 
