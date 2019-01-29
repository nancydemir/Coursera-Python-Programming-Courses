
class Car(object):
        #init gets called whenever we create a new instance ofa         #class
    def __init__(self, model, color, mpg):
        #an object keeps track of itself internally with the           #keyword "self"
        self.model = model
        self.color = color
        self.mpg = mpg
        self.condition="new"
        #member variable named condition gets assigned to              #my_car oncemy_car  is created.   
        #my_car is an instance of the class 
        #you don't need "self" ,since it gets added automat by         #the class #def.
    def display_car(self):
        print "This is a %s" %my_car.color,my_car.model,"with %s" %my_car.mpg,"mpg"
    def drive_car(self): 
        self.condition="used"
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type="molten salt"
my_car = Car("DeLorean", "silver", 88)   
print (my_car.condition)
my_car.drive_car()
print (my_car.condition)
my_car=ElectricCar("GTO","red",66,"molten salt")
print (my_car.battery_type)
print (my_car.model)
