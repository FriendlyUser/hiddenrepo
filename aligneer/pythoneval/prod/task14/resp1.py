import numpy as np
import random

# Flocking Behavior
class Agent:
    def __init__(self, position, velocity):
        self.position = np.array(position)  # 2D vector [x, y]
        self.velocity = np.array(velocity)  # 2D vector [vx, vy]

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
class AntColony:
    def __init__(self, n_ants, bounds, n_points=10):
        self.ants = []
        self.bounds = bounds
        self.pheromone = np.zeros((n_points, n_points))
        self.points = np.random.uniform(0, bounds, (n_points, 2))
        
        for _ in range(n_ants):
            start_point = np.random.randint(0, n_points)
            self.ants.append({
                'position': self.points[start_point].copy(),
                'path': [start_point],
                'distance': 0.0
            })
    
    def update(self):
        alpha = 1.0  # pheromone importance
        beta = 2.0   # distance importance
        evaporation = 0.1
        Q = 1.0      # pheromone deposit factor
        
        # Move ants
        for ant in self.ants:
            if len(ant['path']) < len(self.points):
                current = ant['path'][-1]
                # Calculate probabilities for next point
                unvisited = [i for i in range(len(self.points)) 
                           if i not in ant['path']]
                
                if unvisited:
                    probabilities = []
                    for j in unvisited:
                        distance = np.linalg.norm(
                            self.points[current] - self.points[j])
                        pheromone = self.pheromone[current, j]
                        prob = (pheromone ** alpha) * ((1.0 / distance) ** beta)
                        probabilities.append(prob)
                    # remove nan values from probabilities
                    probabilities = [p for p in probabilities if not np.isnan(p)]
                    probabilities = np.array(probabilities)
                    probabilities = probabilities / probabilities.sum()
                    next_point = np.random.choice(unvisited, p=probabilities)

                    
                    # Update ant's position and path
                    ant['position'] = self.points[next_point].copy()
                    ant['path'].append(next_point)
                    ant['distance'] += np.linalg.norm(
                        self.points[current] - self.points[next_point])
        
        # Update pheromone trails
        self.pheromone *= (1.0 - evaporation)
        
        for ant in self.ants:
            if len(ant['path']) > 1:
                for i in range(len(ant['path']) - 1):
                    current = ant['path'][i]
                    next_point = ant['path'][i + 1]
                    self.pheromone[current, next_point] += Q / ant['distance']
                    self.pheromone[next_point, current] = self.pheromone[current, next_point]

# Usage
bounds = 100.0

# Flocking simulation
swarm = FlockingSwarm(n_agents=100, bounds=bounds)
for _ in range(100):  # Simulation loop
    swarm.update()

# ACO simulation
colony = AntColony(n_ants=50, bounds=bounds)
for _ in range(100):  # Simulation loop
    colony.update()
