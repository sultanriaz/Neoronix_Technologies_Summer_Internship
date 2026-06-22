class Dog:
    species= "canine"
    def __init__(self, name, age, color):
        self.name=name
        self.age=age
        self.color= color
        
dog1=Dog("tommy", 3, "No")
print(dog1.name)
print(dog1.age)
dog2=Dog("tom ", 10, "red")
print(dog2.color)