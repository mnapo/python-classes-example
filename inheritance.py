class Animal:
  kind = "animal"
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  kind = "dog"

puppy = Dog("LilDog")
print(puppy.kind)
print(puppy.name)
