#10. Create a base class Transport. Derive BusService and TrainService from it. # Then create SmartTransport that inherits from both BusService and TrainService # and controls both services
class Transport:
    def __init__(self, system):
        self.system = system

    def show_system(self):
        print("Transport System:", self.system)


class BusService(Transport):
    def __init__(self, system):
        Transport.__init__(self, system)

    def control_bus(self):
        print("Bus service running")


class TrainService(Transport):
    def __init__(self, system):
        Transport.__init__(self, system)

    def control_train(self):
        print("Train service running")


class SmartTransport(BusService, TrainService):
    def __init__(self, system):
        BusService.__init__(self, system)
        TrainService.__init__(self, system)

    def control_all(self):
        self.show_system()
        self.control_bus()
        self.control_train()


s = SmartTransport("Metro Control")
s.control_all()
