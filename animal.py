class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print (self.name)
        print (self.age) 
hippo=Animal("Harry",4)  
elephant=Animal("Elise",5)
sloth=Animal("Suzie",2)
ocelot=Animal("Oscar",1)
hippo.description()
             #elephant.description()
print (hippo.health)
print (sloth.health)
print (ocelot.health)
