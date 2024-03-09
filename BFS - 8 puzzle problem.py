from collections import deque

# Class to represent the puzzle
class PuzzleNode:
    def __init__(self, puzzle_state, parent=None, move=None):
        self.puzzle_state = puzzle_state
        self.parent = parent
        self.move = move

    def get_children(self):
        children = []
        zero_index = self.puzzle_state.index(0)
        rows, cols = 3, 3

        # Move the blank tile left
        if zero_index % cols > 0:
            child_state = self.puzzle_state[:]
            child_state[zero_index], child_state[zero_index - 1] = child_state[zero_index - 1], child_state[zero_index]
            children.append(PuzzleNode(child_state, self, 'left'))

        # Move the blank tile right
        if zero_index % cols < cols - 1:
            child_state = self.puzzle_state[:]
            child_state[zero_index], child_state[zero_index + 1] = child_state[zero_index + 1], child_state[zero_index]
            children.append(PuzzleNode(child_state, self, 'right'))

        # Move the blank tile up
        if zero_index >= cols:
            child_state = self.puzzle_state[:]
            child_state[zero_index], child_state[zero_index - cols] = child_state[zero_index - cols], child_state[zero_index]
            children.append(PuzzleNode(child_state, self, 'up'))

        # Move the blank tile down
        if zero_index < (rows - 1) * cols:
            child_state = self.puzzle_state[:]
            child_state[zero_index], child_state[zero_index + cols] = child_state[zero_index + cols], child_state[zero_index]
            children.append(PuzzleNode(child_state, self, 'down'))

        return children

    def is_goal_state(self):
        return self.puzzle_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __repr__(self):
        return str(self.puzzle_state)

def breadth_first_search(initial_state):
    queue = deque()
    visited = set()
    root = PuzzleNode(initial_state)
    queue.append(root)
    node_count = 0  # Initialize the node count

    while queue:
        node = queue.popleft()
        node_count += 1  # Increment node count for each visited node

        if node.is_goal_state():
            return node, node_count

        visited.add(tuple(node.puzzle_state))
        children = node.get_children()

        for child in children:
            if tuple(child.puzzle_state) not in visited:
                queue.append(child)
                visited.add(tuple(child.puzzle_state))

    return None, node_count

# Function to convert a list to a matrix form
def list_to_matrix(lst):
    return [lst[i:i + 3] for i in range(0, len(lst), 3)]

def main():
    num_test_cases = int(input("Enter the number of test cases: "))
    
    for case in range(num_test_cases):
        print(f"\nTest Case {case+1}:")
        print("Enter the initial state of the puzzle (0 for the blank tile):")
        initial_state = []
        for i in range(3):
            row = input(f"Enter row {i + 1}: ").split()
            initial_state.extend([int(num) for num in row])

        result, total_nodes = breadth_first_search(initial_state)

        if result is None:
            print("The goal state is not reachable")
        else:
            path = []
            node = result
            while node is not None:
                path.append(node)
                node = node.parent

            path.reverse()
            print("The goal state is reachable")
            print("\nPath to the goal state:")
            for i, node in enumerate(path[1:], 1):  # Skip the initial state as it has no move
                print(f"Node {i}: Move {node.move}")
                matrix_form = list_to_matrix(node.puzzle_state)
                for row in matrix_form:
                    print(row)
                print()

            print("Total Nodes Expanded:", total_nodes)

if __name__ == "__main__":
    main()
