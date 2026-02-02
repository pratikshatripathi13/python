class Vehicle:
    def __init__(self, name):
        self.name = name

    def show_vehicle(self):
        print("Vehicle Name:", self.name)


class Car(Vehicle):
    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels

    def drive(self):
        print("Driving on road with", self.wheels, "wheels")


class Boat(Vehicle):
    def __init__(self, name, engine_type):
        super().__init__(name)
        self.engine_type = engine_type

    def sail(self):
        print("Sailing on water with", self.engine_type, "engine")


class AmphibiousVehicle(Car, Boat):
    def __init__(self, name, wheels, engine_type):
        Car.__init__(self, name, wheels)
        Boat.__init__(self, name, engine_type)

    def show_all(self):
        self.show_vehicle()
        self.drive()
        self.sail()


# Object
av = AmphibiousVehicle("Amphi-X", 4, "Jet")
av.show_all()
