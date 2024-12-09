class Event:
    def __init__(self, time, action, *args, **kwargs):
        self.time = time
        self.action = action
        self.args = args
        self.kwargs = kwargs

class Simulation:
    def __init__(self):
        self.events = []
        self.current_time = 0
        self.inventory = {}

    def run(self):
        while self.events:
            event = self.events.pop(0)
            self.current_time = event.time
            event.action(self, *event.args, **event.kwargs)

    def schedule_event(self, event):
        self.events.append(event)
        self.events.sort(key=lambda x: x.time)

    def update_inventory(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity

def receive_shipment(simulation, product, quantity):
    simulation.update_inventory(product, quantity)

# Create a simulation instance
sim = Simulation()

# Schedule events
sim.schedule_event(Event(10, receive_shipment, 'ProductA', 100))
sim.schedule_event(Event(5, receive_shipment, 'ProductB', 200))

# Run the simulation
sim.run()

# Print the final inventory
print(sim.inventory)
