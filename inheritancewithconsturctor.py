class A:

    def __init__(self):
        print("In A init.")

    def feature1(self):
        print("Feature1 working.")
    
    def feature2(self):
        print("Feature2 working.")

class B:
    
    def __init__(self):
        print("In B init.")

    def feature3(self):
        print("Feature3 working.")
    
    def feature4(self):
        print("Feature4 working.")

class C(B,A):

    def __init__(self):
        super().__init__() #Due to MRO->Method resolution order the A class init will be called first
        print("In C init")

obj1=C()



