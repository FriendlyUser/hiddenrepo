class Event:
    def __init__(self, time, action, *args, **kwargs):
        """
        Initialize an Event object.
        
        Parameters:
        - time: When the event should occur
        - action: Function to execute
        - *args, **kwargs: Arguments to pass to the action function
        """
        self.time = time
        self.action = action
        self.args = args
        self.kwargs = kwargs

class Simulation:
    def __init__(self):
        """Initialize the simulation with empty events list and inventory."""
        self.events = []
        self.current_time = 0
        self.inventory = {}

    def run(self):
        """Execute all scheduled events in chronological order."""
        while self.events:
            event = self.events.pop(0)
            self.current_time = event.time
            # Pass self as the first argument to the action
            event.action(self, *event.args, **event.kwargs)

    def schedule_event(self, event):
        """Add an event to the schedule and sort by time."""
        self.events.append(event)
        self.events.sort(key=lambda x: x.time)

    def update_inventory(self, product, quantity):
        """Update inventory levels for a given product."""
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity

def receive_shipment(simulation, product, quantity):
    """
    Handle receiving a shipment.
    
    Parameters:
    - simulation: The Simulation instance
    - product: Product identifier
    - quantity: Amount received
    """
    simulation.update_inventory(product, quantity)

# Create and run the simulation
def main():
    # Create a new simulation instance
    sim = Simulation()
    
    # Schedule events
    sim.schedule_event(Event(10, receive_shipment, 'ProductA', 100))
    sim.schedule_event(Event(5, receive_shipment, 'ProductB', 200))
    
    # Run the simulation
    sim.run()
    
    # Print final inventory
    print(sim.inventory)

if __name__ == "__main__":
    main()