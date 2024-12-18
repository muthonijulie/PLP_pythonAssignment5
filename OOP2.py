class Animal:
    def __init__(self,name,age,gender,habitat):
        self.name=name
        self.age=age
        self.gender=gender
        self.habitat=habitat
    def move(self):
        print("All animals move")
class Dog(Animal):
    def move(self):
        print(self.name,"locomote")
    def eat(self):
        print(self.name," do well in the ",self.habitat,"environment")
class Birds(Animal):
    def move(self):#polymorphism
        print(self.name," fly")
    def build(self):
        print("The ",self.gender,self.name," take care of their young ones")
class Fish(Animal):
    def move(self):
        print(self.name," swim in water")
    def live(self):
        print(self.name," lives in ",self.habitat)
class Cats(Animal):
    pass

dog=Dog("Dog","2yrs","male","tropical")
dog.eat()
bird=Birds("Eagles","3yrs","female","tropical")
bird.build()
fish=Fish("Tilapia","1yr","female","water")
fish.live()
cat=Cats("Brown cat","4yrs","male","tropical")
for x in(dog,bird,fish,cat):
    
    x.move()