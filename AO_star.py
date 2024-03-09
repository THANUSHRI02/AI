# Cost to find the AND and OR path
def Cost(H, condition, weight=1):
    cost = {}
    if 'AND' in condition:
        AND_nodes = condition['AND']
        Path_A = ' AND '.join(AND_nodes)
        PathA = sum(H[node] + weight for node in AND_nodes)
        cost[Path_A] = PathA

    if 'OR' in condition:
        OR_nodes = condition['OR']
        Path_B = ' OR '.join(OR_nodes)
        PathB = min(H[node] + weight for node in OR_nodes)
        cost[Path_B] = PathB
    return cost

# Update the cost
def update_cost(H, Conditions, weight=1):
    Main_nodes = list(Conditions.keys())
    Main_nodes.reverse()
    least_cost = {}
    for key in Main_nodes:
        condition = Conditions[key]
        c = Cost(H, condition, weight)
        if c:
            H[key] = min(c.values())
        least_cost[key] = c
    return least_cost

# Print the shortest path
def shortest_path(Start,Updated_cost, H):
	Path = Start
	if Start in Updated_cost.keys():
		Min_cost = min(Updated_cost[Start].values())
		key = list(Updated_cost[Start].keys())
		values = list(Updated_cost[Start].values())
		Index = values.index(Min_cost)
		
		# FIND MINIMIMUM PATH KEY
		Next = key[Index].split()
		# ADD TO PATH FOR OR PATH
		if len(Next) == 1:

			Start =Next[0]
			Path += ' = ' +shortest_path(Start, Updated_cost, H)
		# ADD TO PATH FOR AND PATH
		else:
			Path +='=('+key[Index]+') '

			Start = Next[0]
			Path += '[' +shortest_path(Start, Updated_cost, H) + ' + '

			Start = Next[-1]
			Path += shortest_path(Start, Updated_cost, H) + ']'

	return Path
# Get user input for node heuristic values
def get_node_heuristics():
    H = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for i in range(num_nodes):
        node_name = input(f"Enter the name of node {i + 1}: ")
        node_cost = int(input(f"Enter the heuristic cost for node {node_name}: "))
        H[node_name] = node_cost
    return H

# Get user input for conditions
def get_conditions():
    Conditions = {}
    num_conditions = int(input("Enter the number of conditions: "))
    for i in range(num_conditions):
        node_name = input(f"Enter the name of the node for condition {i + 1}: ")
        and_nodes = input("Enter the AND nodes separated by spaces (if any, otherwise press Enter): ").split()
        or_nodes = input("Enter the OR nodes separated by spaces (if any, otherwise press Enter): ").split()
        condition = {}
        if and_nodes:
            condition['AND'] = and_nodes
        if or_nodes:
            condition['OR'] = or_nodes
        Conditions[node_name] = condition
    return Conditions

if __name__ == "__main__":
    # Get user input for node heuristic values
    H1 = get_node_heuristics()

    # Get user input for conditions
    Conditions = get_conditions()

    # weight
    weight = 1

    # Print initial cost of all nodes
    print("Initial Cost:")
    for node, cost in H1.items():
        print(f"{node}: {cost}")

    # Updated cost
    print("*" * 75)
    print("Updated Cost:")
    Updated_cost = update_cost(H1, Conditions, weight=1)
    for node, cost in H1.items():
        print(f"{node}: {cost}")

    print("*" * 75)
    print("Shortest Path:\n", shortest_path('A', Updated_cost, H1))
