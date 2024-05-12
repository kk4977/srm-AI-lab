from queue import PriorityQueue
class PuzzleState:
    def __init__(self, puzzle, parent=None, move="Initial", cost=0):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.cost = cost
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash(str(self.puzzle))

    def h(self):
        return sum([1 if self.puzzle[i][j] != self.goal_state[i][j] else 0 for i in range(3) for j in range(3)])

    def get_successors(self):
        successors = []
        empty_row, empty_col = self.find_empty_tile()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_puzzle = [row[:] for row in self.puzzle]
                new_puzzle[empty_row][empty_col], new_puzzle[new_row][new_col] = \
                    new_puzzle[new_row][new_col], new_puzzle[empty_row][empty_col]
                successors.append(PuzzleState(new_puzzle, self, "Move", self.cost + 1))

        return successors

    def find_empty_tile(self):
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i, j

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put(initial_state)
    explored = set()

    while not frontier.empty():
        current_state = frontier.get()
        if current_state.puzzle == current_state.goal_state:
            return current_state

        explored.add(current_state)
        for successor in current_state.get_successors():
            if successor not in explored:
                frontier.put(successor)

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found")
    else:
        path = []
        current_state = solution
        while current_state.parent:
            path.append((current_state.move, current_state.puzzle))
            current_state = current_state.parent
        path.append(("Initial", current_state.puzzle))

        path.reverse()
        for move, puzzle in path:
            print(move)
            print_puzzle(puzzle)

def print_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()

# Example usage:
initial_state = PuzzleState([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
solution = a_star_search(initial_state)
print_solution(solution)