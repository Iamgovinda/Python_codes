#multiple form of a class of a objects

#but lets do ducktypings here

#if a thing walks like a duck, swims like a duck and eat like a duck than this thing is duck....
#that means doesnt matter how you looks like, your behaviour defines who you are.



class pycharm:

    def execute(self):
        print("Code is compiling")
        print("Code is running")


class myowntexteditor:

    def execute(self):
        print("the code is running")
        print("the code is compiling")
        print("power of myowntexteditor.")



class laptop:

    def code(self,ide):
        ide.execute()


ide=myowntexteditor()
lap=laptop()
lap.code(ide)



