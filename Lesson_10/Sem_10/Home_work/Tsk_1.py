class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None
        
    def get_spec(self):
        return self.spec
    
    def get_info(self):
        return f'{__class__} name: {self.name}, age: {self.age}, spec: {self.get_spec()}'
    
class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
        
    def get_info(self):
        return f'{__class__} name: {self.name}, age: {self.age}, spec: {self.get_spec()}'
        
class Bird(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
        
    def get_info(self):
        return f'{__class__} name: {self.name}, age: {self.age}, spec: {self.get_spec()}'
        
class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

    def get_info(self):
        return f'{__class__} name: {self.name}, age: {self.age}, spec: {self.get_spec()}'
        
class Horse(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

    def get_info(self):
        return f'{__class__} name: {self.name}, age: {self.age}, spec: {self.get_spec()}'
        
class Animal_Factory(Dog, Cat, Bird, Horse):
    def __init__(self, type_animal, *args):
        super().__init__(args)
        self.type_animal = type_animal
        
    def create_animal(type_a, *args):
        name, age, spec = args
        match type_a:
            case 'dog':
                new_animal = Dog(name, age, spec)
            case 'cat':
                new_animal = Cat(name, age, spec)
            case 'bird':
                new_animal = Bird(name, age, spec)
            case 'horse':
                new_animal = Horse(name, age, spec)
            case _:
                new_animal = Animal(name, age)
            
        return new_animal

animal_1 = Animal_Factory.create_animal('dog', 'Bobik', 3, 'Gaw-gaw')
animal_2 = Animal_Factory.create_animal('cat', 'Murka', 6, 'Meuw-meuw')
animal_3 = Animal_Factory.create_animal('fox', 'Red Hut', 1, 'Fyr-fyr')
animal_4 = Animal_Factory.create_animal('horse', 'Sugar', 5, 'I-go-go')
animal_5 = Animal_Factory.create_animal('bird', 'Grey sparrow 1', 3, 'Chik-chirik')
for pet in [animal_1, animal_2, animal_3, animal_4, animal_5]:
    print(pet.get_info())
    
            
