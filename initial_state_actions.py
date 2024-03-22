# Define the initial state
def initial_state(vehicle):
    return vehicle.current_position  # Assuming vehicle object has current position attribute

# Define the actions function
def actions(node, traversed_nodes, dead_ends):
    return {move_to(m) for m in neighbors(node) if m not in traversed_nodes and m not in dead_ends}
