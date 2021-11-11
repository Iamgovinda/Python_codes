class cat:
    def sound(self):
        print("A cat is meaowing...")
    
class dog:
    def sound(self):
        print("A dog is barking.")

def check_polymorphism(obj):
    obj.sound()

cat1=cat()
dog1=dog()

check_polymorphism(cat1)
check_polymorphism(dog1)