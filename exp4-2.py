from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def successors(state):
    successors = []
    if state.boat == 'left':
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.missionaries - m, state.cannibals - c, 'right')
                    if 0 <= new_state.missionaries <= 3 and 0 <= new_state.cannibals <= 3 and (new_state.missionaries >= new_state.cannibals or new_state.missionaries == 0) and ((3 - new_state.missionaries) >= (3 - new_state.cannibals) or new_state.missionaries == 3):
                        successors.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.missionaries + m, state.cannibals + c, 'left')
                    if 0 <= new_state.missionaries <= 3 and 0 <= new_state.cannibals <= 3 and (new_state.missionaries >= new_state.cannibals or new_state.missionaries == 0) and ((3 - new_state.missionaries) >= (3 - new_state.cannibals) or new_state.missionaries == 3):
                        successors.append(new_state)
    return successors

def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()
        if state == goal_state:
            return actions
        if state not in visited:
            visited.add(state)
            for successor in successors(state):
                queue.append((successor, actions + [successor]))

    return None

def main():
    initial_state = State(3, 3, 'left')  # Initial state of the missionaries and cannibals
    goal_state = State(0, 0, 'right')  # Goal state to reach

    solution = bfs(initial_state, goal_state)
    if solution:
        print("Solution:")
        for action in solution:
            print(f"Move {action.missionaries} missionaries and {action.cannibals} cannibals to the {action.boat}.")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
