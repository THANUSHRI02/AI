def is_goal_state(state, target):
    return state[0] == target or state[1] == target

def get_next_states(state, capacities):
    next_states = []
    
    max_capacity_a, max_capacity_b = capacities
    
    # Fill jug A
    next_state_fill_a = (max_capacity_a, state[1])
    if next_state_fill_a != state:
        next_states.append(next_state_fill_a)
    
    # Fill jug B
    next_state_fill_b = (state[0], max_capacity_b)
    if next_state_fill_b != state:
        next_states.append(next_state_fill_b)
    
    # Empty jug A
    next_state_empty_a = (0, state[1])
    if next_state_empty_a != state:
        next_states.append(next_state_empty_a)
    
    # Empty jug B
    next_state_empty_b = (state[0], 0)
    if next_state_empty_b != state:
        next_states.append(next_state_empty_b)
    
    # Pour from A to B
    pour_amount = min(state[0], max_capacity_b - state[1])
    next_state_pour_a_to_b = (state[0] - pour_amount, state[1] + pour_amount)
    if next_state_pour_a_to_b != state:
        next_states.append(next_state_pour_a_to_b)
    
    # Pour from B to A
    pour_amount = min(state[1], max_capacity_a - state[0])
    next_state_pour_b_to_a = (state[0] + pour_amount, state[1] - pour_amount)
    if next_state_pour_b_to_a != state:
        next_states.append(next_state_pour_b_to_a)
    
    return next_states

def dfs(start_state, target, capacities):
    visited = set()
    stack = [(start_state, [])]  
    
    while stack:
        state, path = stack.pop()
        
        if is_goal_state(state, target):
            return path  
        
        visited.add(state)
        
        next_states = get_next_states(state, capacities)
        for next_state in next_states:
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))
                
def get_solution_info(solution, target):
    jug = "A" if solution[-1][0] == target else "B"
    num_moves = len(solution) - 1
    return jug, num_moves

# User Input
num_test_cases = int(input("Enter the number of test cases: "))

for case in range(num_test_cases):
    print(f"\nTest Case {case+1}:")
    
    print("Enter the initial amount in jug A:")
    start_state_a = int(input())
    
    print("Enter the initial amount in jug B:")
    start_state_b = int(input())
    
    print("Enter the target amount:")
    target = int(input())
    
    jug_capacities = (start_state_a, start_state_b)
    start_state = (start_state_a, start_state_b)

    solution = dfs(start_state, target, jug_capacities)
    
    if solution:
        print("\nPossible Solutions to measure {} liters:".format(target))
        for state in solution:
            print("A: {}, B: {}".format(state[0], state[1]))

        target_jug, num_moves = get_solution_info(solution, target)
        print("\nTarget amount of {} liters is in Jug {}, reached in {} moves.".format(target, target_jug, num_moves))
    else:
        print("Target amount not reachable.")
