from abc import ABC, abstractmethod

class pen(ABC):

    @abstractmethod
    def write(self):
        pass

class signpen(pen):
    def write(self):
        print("Signpen is working.")

pen1=signpen()
pen1.write()
