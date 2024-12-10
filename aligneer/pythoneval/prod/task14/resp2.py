import numpy as np
import random

# Flocking Behavior
class Agent:
    def __init__(self, position, velocity):
        self.position = np.array(position)  # position is a NumPy array [x, y]
        self.velocity = np.array(velocity)  # velocity is a NumPy array [vx, vy]

class FlockingSwarm:
    def __init__(self, n_agents, bounds):
        self.agents = []
        self.bounds = bounds
        
        for _ in range(n_agents):
            position = np.random.uniform(0, bounds, 2)
            velocity = np.random.uniform(-1, 1, 2)
            self.agents.append(Agent(position, velocity))
    
    def update(self):
        alignment_weight = 1.0
        cohesion_weight = 1.0
        separation_weight = 1.5
        perception_radius = 5.0
        
        for agent in self.agents:
            neighbors = self._get_neighbors(agent, perception_radius)
            
            if neighbors:
                # Alignment: match velocity of neighbors
                alignment = np.mean([n.velocity for n in neighbors], axis=0)
                
                # Cohesion: move toward center of neighbors
                cohesion = np.mean([n.position for n in neighbors], axis=0) - agent.position
                
                # Separation: avoid crowding neighbors
                separation = np.zeros(2)
                for n in neighbors:
                    diff = agent.position - n.position
                    if np.any(diff):
                        separation += diff / np.linalg.norm(diff)
                
                # Update velocity
                agent.velocity += (alignment_weight * alignment +
                                 cohesion_weight * cohesion +
                                 separation_weight * separation)
                
                # Limit velocity magnitude
                speed = np.linalg.norm(agent.velocity)
                if speed > 2.0:
                    agent.velocity = agent.velocity / speed * 2.0
            
            # Update position
            agent.position += agent.velocity
            
            # Wrap around boundaries
            agent.position = agent.position % self.bounds
    
    def _get_neighbors(self, agent, radius):
        return [a for a in self.agents if a != agent and
                np.linalg.norm(a.position - agent.position) < radius]

# Ant Colony Optimization (ACO)
class Ant:
    def __init__(self, start_node):
        self.current_node = start_node
        self.path = [start_node]
        self.total_distance = 0

def initialize_pheromones(num_nodes):
    return np.ones((num_nodes, num_nodes))

def update_pheromones(pheromones, ants, decay=0.1):
    pheromones *= (1 - decay)
    for ant in ants:
        for i in range(len(ant.path) - 1):
            pheromones[ant.path[i], ant.path[i + 1]] += 1 / ant.total_distance

def choose_next_node(ant, pheromones, distances, alpha=1, beta=2):
    current_node = ant.current_node
    probabilities = []
    for next_node in range(len(distances)):
        if next_node not in ant.path:
            pheromone = pheromones[current_node, next_node] ** alpha
            heuristic = (1 / distances[current_node, next_node]) ** beta
            probabilities.append(pheromone * heuristic)
        else:
            probabilities.append(0)
    probabilities = np.array(probabilities)
    probabilities /= probabilities.sum()
    return np.random.choice(range(len(distances)), p=probabilities)

def run_aco(num_nodes, num_ants, num_iterations, distances):
    pheromones = initialize_pheromones(num_nodes)
    best_path = None
    best_distance = float('inf')

    for _ in range(num_iterations):
        ants = [Ant(start_node=np.random.randint(num_nodes)) for _ in range(num_ants)]
        for ant in ants:
            while len(ant.path) < num_nodes:
                next_node = choose_next_node(ant, pheromones, distances)
                ant.total_distance += distances[ant.current_node, next_node]
                ant.current_node = next_node
                ant.path.append(next_node)
            ant.total_distance += distances[ant.path[-1], ant.path[0]]  # Return to start

            if ant.total_distance < best_distance:
                best_distance = ant.total_distance
                best_path = ant.path

        update_pheromones(pheromones, ants)

    return best_path, best_distance

# Example Usage
bounds = 100.0

# Flocking simulation
swarm = FlockingSwarm(n_agents=100, bounds=bounds)
for _ in range(100):  # Simulation loop
    swarm.update()

# ACO simulation
num_nodes = 10
distances = np.random.rand(num_nodes, num_nodes) * 100
best_path, best_distance = run_aco(num_nodes, num_ants=10, num_iterations=100, distances=distances)

print("Best path (ACO):", best_path)
print("Best distance (ACO):", best_distance)
