class Animal:
    name = ""

    def __init__(self, name):
        self.name = name
        print(f"\n----{self.name} Is in the creation process.----\n")

    def walk(self):
        """
        Walk a tiny bit
        """
        print(f"{self.name} is walking...")

    def __del__(self):
        print(f"\n----{self.name} Is in the destruction process.-----\n")


duck = Animal("Duck")
duck.walk()
duck.walk()
duck.walk()
print(type(duck))

pig = Animal("Pig")
pig.walk()
pig.walk()
pig.walk()
pig.walk()