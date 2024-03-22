# Define the transition model
def transition_model(node, action):
    return action  # if action is the next node or apply action to node if it's a function

# Define the goal test
def goal_test(node, destination):
    return node == destination

# Define the path cost
def path_cost(path, G):
    return sum(normalized(T_traffic(n, m) + distance(n, m)) for n, m in zip(path, path[1:]))
