import math
import random
# Define the initial state
def initial_state(vehicle):
    return vehicle.current_position  # Assuming vehicle object has current position attribute

# Define the actions function
def actions(node, G, A, dead_ends):
    return [move_to(m) for m in neighbors(node) if m not in A and m not in dead_ends]

# Define the transition model
def transition_model(node, action):
    return action  # if action is the next node or apply action to node if it's a function

# Define the goal test
def goal_test(node, destination):
    return node == destination

# Define the path cost
def path_cost(path, G):
    if isinstance(path, str):  # if path is a single state (string)
        return 0
    return sum(normalized(T_traffic(n, m) + distance(n, m)) for n, m in zip(path, path[1:]))


def simulated_annealing(G, E, W, Dv, A, initial_temp, cooling_rate, max_iterations=1000):
    current_state = W  
    total_cost = 0  
    temperature = initial_temp
    
    print(f"Starting at node: {current_state}")
    
    for iteration in range(max_iterations):
        if temperature <= 0:
            print("Temperature is zero, exiting.")
            break  
        
        available_actions = actions(current_state, G, A, E)
        print(f"Available actions from {current_state}: {available_actions}")  # Debugging line
        
        if not available_actions:
            print(f"No available actions from {current_state}, exiting.")
            break  
        
        action = random.choice(list(available_actions))
        new_state = result(current_state, action)
        cost_diff = path_cost([new_state], G) - path_cost([current_state], G)
        
        if cost_diff < 0 or random.uniform(0, 1) < math.exp(-cost_diff / temperature):
            print(f"Moving from {current_state} to {new_state} with cost difference: {cost_diff}")
            current_state = new_state
            total_cost += path_cost([new_state], G)  # Corrected total cost update
        
        print(f"Temperature: {temperature}")  # Debugging line
        temperature *= cooling_rate  
        
        if goal_test(current_state, Dv):
            print(f"Reached the destination {Dv}, exiting.")
            break  
    
    print(f"Total path cost: {total_cost}")
    return current_state  


# Assumptions and simple definitions for missing functions
def neighbors(node):
    return {
        'A': ['B', 'E'],
        'B': ['A', 'C', 'F', 'G', 'H'],
        'C': ['B'],
        'E': ['A', 'F'],
        'F': ['B', 'E'],
        'G': ['B', 'H'],
        'H': ['B', 'G']
    }[node]

def move_to(m): return m


def T_traffic(n, m): return random.randint(1, 10)


def distance(n, m): return 1


def normalized(value): return value


def result(state, action): return action


# Test Graph and parameters
initial_temp = 1000  # Adjusted initial temperature
cooling_rate = 0.99  # Adjusted cooling rate

#Graph 
#Nodes: A,B,C,D
#Edges: A->B, B->C, C->D, D->A
G4 = (['A', 'B', 'C', 'E', 'F', 'G', 'H'], [('A', 'B'), ('A', 'E'), ('E', 'F'), ('B', 'F'), ('B', 'C'), ('B', 'G'), ('B', 'H'), ('G', 'H')])

# Parameters
E4 = ['H']  # H is a dead end
W4 = 'A'  # Starting at A
Dv4 = 'C'  # Destination C
A4 = ['A', 'B', 'C', 'E', 'F', 'G']  # Allowed nodes

# Running the algorithm
best_solution_4 = simulated_annealing(G4, E4, W4, Dv4, A4, initial_temp, cooling_rate)
print("Best solution for Test Case 4:", best_solution_4)

