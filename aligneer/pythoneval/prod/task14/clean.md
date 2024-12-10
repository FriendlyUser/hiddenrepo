I am working on a simulation for swarm intelligence where agents exhibit flocking behavior. Here's the code I've been using:

```python
import random

class Agent:
    def __init__(self, position, velocity):
        self.position = position  # position is a dict with 'x' and 'y'
        self.velocity = velocity  # velocity is a dict with 'x' and 'y'

def update_agents(agents):
    for agent in agents:
        # Compute new velocity based on neighboring agents
        # Alignment, cohesion, and separation behaviors
        # ...
        pass

agents = []
for _ in range(100):
    position = {'x': random.uniform(0, 100), 'y': random.uniform(0, 100)}
    velocity = {'x': random.uniform(-1, 1), 'y': random.uniform(-1, 1)}
    agents.append(Agent(position, velocity))

update_agents(agents)
```

I feel like using ant colony optimization might be a better fit for what I'm trying to achieve, but I'm not sure how to adapt this code accordingly. Also, managing agent states with a list of dictionaries containing nested keys is getting messy.  

Should I be structuring my data differently? Maybe you could provide an ant colony optimization implementation for agent movement in Python and perhaps suggest a more efficient way to handle the agent data?  

I'm curious to see how the two approaches compare.  
