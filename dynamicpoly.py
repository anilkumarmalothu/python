class vehicle:
    def __init__(self):
        print('vehicle')
    def drive(self):
        print("driving vehicle")
class car(vehicle):
    def __init__(self):
        print("car")
    def drive(self):
        print("driving a car")
vobj=vehicle()
cobj=car()                        
for my_vehicle in (vobj,cobj):
    my_vehicle.drive()