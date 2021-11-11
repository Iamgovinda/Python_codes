#one object behaving in various way....i.e,,, one thing and multiple forms
# okay....if theres a bird which is walking like a duck,  quackking like a duck and swimming like a duck and that bird is duck.


class pycharm:
    def execute(self):
        print("Compiling..")
        print("Running...")
        print("In pycharm...")

class owneditor:
    def execute(self):
        print("Spell check.")
        print("Convention check.") 
        print("Compiling..")
        print("Running......")
        print("In my own editor\n\n")

class laptop:
    def code(self,ide):
        ide.execute()

ide1=owneditor()
ide2=pycharm()
lap1=laptop()

lap1.code(ide1)
lap1.code(ide2)
#a method can behave in different way....which is from different class as well.
