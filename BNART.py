"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Azmat Alvi
ID: 190563060
Email: alvi3060@mylaurier.ca
__updated__ = "2023-10-22"
-------------------------------------------------------
"""
import math
import random

def actions(node, graph):
    return [(neighbor, cost) for neighbor, cost in graph[node].items()]

def goal_test(node, destination):
    return node == destination

def simulated_annealing(graph, start, destination, initial_temp, cooling_rate, max_iterations=1000):
    current_state = start  
    temperature = initial_temp
    
    print(f"Starting at node: {current_state}")
    
    for iteration in range(max_iterations):
        if temperature <= 0:
            print("Temperature is zero, exiting.")
            break  
        
        available_actions = actions(current_state, graph)
        print(f"Available actions from {current_state}: {available_actions}")  
        
        if not available_actions:
            print(f"No available actions from {current_state}, exiting.")
            break  
        
        action, cost = random.choice(available_actions)
        
        cost_diff = cost - random.randint(1, 10)  # Simulating a dynamic cost difference
        
        if cost_diff < 0 or random.uniform(0, 1) < math.exp(-cost_diff / temperature):
            print(f"Moving from {current_state} to {action} with cost difference: {cost_diff}")
            current_state = action
        
        print(f"Temperature: {temperature}")  
        temperature *= cooling_rate  
        
        if goal_test(current_state, destination):
            print(f"Reached the destination {destination}, exiting.")
            break  
    
    return current_state  

# Graph representation
graph = {
    'A': {'B': 1, 'E': 3},
    'B': {'A': 1, 'C': 5, 'F': 2},
    'C': {'B': 5},
    'E': {'A': 3, 'F': 1},
    'F': {'B': 2, 'E': 1},
}

initial_temp = 1000  
cooling_rate = 0.99  

best_solution = simulated_annealing(graph, 'A', 'C', initial_temp, cooling_rate)