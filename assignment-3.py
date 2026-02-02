 #Create a base class Device. Derive Camera and Phone from it. 
#    Then create SmartGadget that inherits from both Camera and Phone 
#    and performs multitasking operations.
class Device:
    def __init__(self, name):
        self.name = name

    def show_device(self):
        print("Device Name:", self.name)


class Phone(Device):
    def __init__(self, name, storage):
        Device.__init__(self, name)
        self.storage = storage

    def show_storage(self):
        print("Storage:", self.storage)


class Camera(Device):
    def __init__(self, name, pixel):
        Device.__init__(self, name)
        self.pixel = pixel

    def show_pixel(self):
        print("Pixel:", self.pixel)


class SmartGadget(Phone, Camera):
    def __init__(self, name, storage, pixel):
        Phone.__init__(self, name, storage)
        Camera.__init__(self, name, pixel)

    def show_all(self):
        self.show_device()
        self.show_storage()
        self.show_pixel()


av = SmartGadget("Ino-X", 256, 500)
av.show_all()
