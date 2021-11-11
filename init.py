class computer:
  def __init__(self,name,ram):
    self.name=name
    self.ram=ram
computer1 = computer("Macbook","8GB")
computer2 = computer("Acer", "16 GB")

print(computer1.name)
print(computer1.ram)
print(computer2.name)
print(computer2.ram)