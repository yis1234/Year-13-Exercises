class Bus:
    bus_list = []
    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        Bus.bus_list.append(self)

    def display_info(self):
        for bus in Bus.bus_list:
            if bus == self:
                print(f"Bus number: {self.number}")
                print(f"Route: {self.route}")
                print(f"Driver: {self.driver}")


b1 = Bus(2010, "P", "Bob")
b2 = Bus(2020, "Y", "Bill")
b3 = Bus(1999, "130", "Ben")

# Print information
for bus in Bus.bus_list:
    bus.display_info()

for bus in range(len(Bus.bus_list)):
    Bus.display_info(Bus.bus_list[bus])
