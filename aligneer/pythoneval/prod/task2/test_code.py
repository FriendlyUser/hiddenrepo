class Event:
    def init(self, time, action, *args, **kwargs):
        self.time = time
        self.action = action
        self.args = args
        self.kwargs = kwargs


class Simulation:
    def init(self):
        self.events = []
        self.current_time = 0
        self.inventory = {}

    def run(self):
        while self.events:
            event = self.events.pop(0)
            self.current_time = event.time
            event.action(*event.args, **event.kwargs)

    def schedule_event(self, event):
        self.events.append(event)
        self.events.sort(key=lambda x: x.time)

    def update_inventory(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity


# Initialize the simulation
sim = Simulation()

# Define an action for receiving shipments
def receive_shipment(product, quantity):
    sim.update_inventory(product, quantity)

# Schedule events
sim.schedule_event(Event(10, receive_shipment, 'ProductA', 100))
sim.schedule_event(Event(5, receive_shipment, 'ProductB', 200))

# Run the simulation
sim.run()

# Print the inventory
print(sim.inventory)
