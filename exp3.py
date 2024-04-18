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

def dfs(state, goal, jug_sizes, visited):
    if state == goal:
        return []
    visited.add(state)
    for succ_state in successors(state, jug_sizes):
        if succ_state not in visited:
            result = dfs(succ_state, goal, jug_sizes, visited)
            if result is not None:
                pour_amount = [state.jugs[i] - succ_state.jugs[i] for i in range(len(state.jugs))]
                return [f"Pour {pour_amount[i]} from jug {i+1} to jug {j+1}" for i, j in enumerate(range(len(state.jugs)))]

    return None

def main():
    jug_sizes = (5, 3)  # Jug sizes (e.g., (5, 3) represents jugs of size 5 and 3)
    initial_state = State((0, 0))  # Initial state of the jugs
    goal_state = State((4, 0))  # Goal state to reach

    visited = set()
    solution = dfs(initial_state, goal_state, jug_sizes, visited)
    if solution:
        print("Solution:", solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
