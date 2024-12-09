Working on this simulation thing for modeling supply chain logistics using events, but something's not right. The events aren't updating the inventory levels correctly or maybe they're not triggering at the right time? I can't figure it out. Here's the code snippet that's causing me headaches: class Event: def init(self, time, action, *args, **kwargs): self.time = time self.action = action self.args = args self.kwargs = kwargs

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
sim = Simulation()

def receive_shipment(product, quantity): sim.update_inventory(product, quantity)

sim.schedule_event(Event(10, receive_shipment, 'ProductA', 100)) sim.schedule_event(Event(5, receive_shipment, 'ProductB', 200))

sim.run() print(sim.inventory) When I run this, it doesn't print the inventory correctly. I feel like I'm missing something silly but can't put my finger on it.Any thoughts on what's going wrong here?

