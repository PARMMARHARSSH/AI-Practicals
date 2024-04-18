from collections import deque

class State:
    def __init__(self, jugs):
        self.jugs = jugs

    def __eq__(self, other):
        return self.jugs == other.jugs

    def __hash__(self):
        return hash(tuple(self.jugs))

def successors(state, jug_sizes):
    successors = []
    for i in range(len(state.jugs)):
        for j in range(len(state.jugs)):
            if i != j:
                pour_amount = min(state.jugs[i], jug_sizes[j] - state.jugs[j])
                if pour_amount > 0:
                    new_jugs = list(state.jugs)
                    new_jugs[i] -= pour_amount
                    new_jugs[j] += pour_amount
                    successors.append(State(tuple(new_jugs)))
    return successors

def bfs(initial_state, goal, jug_sizes):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()
        if state == goal:
            return actions
        if state not in visited:
            visited.add(state)
            for successor in successors(state, jug_sizes):
                queue.append((successor, actions + [successor]))

    return None

def main():
    jug_sizes = (5, 3)  # Jug sizes (e.g., (5, 3) represents jugs of size 5 and 3)
    initial_state = State((0, 0))  # Initial state of the jugs
    goal_state = State((4, 0))  # Goal state to reach

    solution = bfs(initial_state, goal_state, jug_sizes)
    if solution:
        print("Solution:")
        for action in solution:
            print(action)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
