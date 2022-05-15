class Zoo:

    __animal = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "bird":
            self.birds.append(name)
        elif species == "fish":
            self.fishes.append(name)

        Zoo.__animal += 1

    def get_info(self, species):
        if species == "mammal":
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animal}"
        elif species == "bird":
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animal}"
        elif species == "fish":
            return f"{species.capitalize()}es in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animal}"


zoo_name = input()
zoo = Zoo(zoo_name)
number_of_animals = int(input())

for i in range(number_of_animals):
    command = input().split()
    species = command[0]
    animal = command[1]
    zoo.add_animals(species, animal)

info = input()
print(zoo.get_info(info))
