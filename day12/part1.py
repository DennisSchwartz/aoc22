import numpy as np

ELEVATION = 'abcdefghijklmnopqrstuvwxyz'


def reconstruct_path(came_from, current):
    return 0


def a_star(start, goal, h):
    open_set = set(start)
    came_from = {}
    g_score = {start: 0}
    f_score = {start: 0}

    while open_set:
        current = next(iter(open_set))
        for pos in open_set:
            if f_score.get(pos, np.inf) < f_score[current]:
                current = pos

        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.pop(current)
        neighbors = [
            (open_set[0] - 1, open_set[1]),  # below
            (open_set[0] + 1, open_set[1]),  # above
            (open_set[0], open_set[1] - 1),  # left
            (open_set[0], open_set[1] + 1)  # right
        ]
        for n in neighbors:
            tentative_g_score = 0

def main(in_file):
    grid = []
    start = None
    goal = None
    for line in in_file.readlines():
        line = line.strip()
        if 'S' in line:
            start = (line.index('S'), len(grid))
            line = line.replace('S', 'a')
        if 'E' in line:
            goal = (line.index('E'), len(grid))
            line = line.replace('E', 'z')
        grid.append([ELEVATION.index(l) for l in line])

    print(grid)




if __name__ == '__main__':
    with open('example.txt', 'r') as f:
        res = main(f)
        print(res)


# function reconstruct_path(cameFrom, current)
#     total_path := {current}
#     while current in cameFrom.Keys:
#         current := cameFrom[current]
#         total_path.prepend(current)
#     return total_path
#
# // A* finds a path from start to goal.
# // h is the heuristic function. h(n) estimates the cost to reach goal from node n.
# function A_Star(start, goal, h)
#     // The set of discovered nodes that may need to be (re-)expanded.
#     // Initially, only the start node is known.
#     // This is usually implemented as a min-heap or priority queue rather than a hash-set.
#     openSet := {start}
#
#     // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
#     // to n currently known.
#     cameFrom := an empty map
#
#     // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
#     gScore := map with default value of Infinity
#     gScore[start] := 0
#
#     // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
#     // how cheap a path could be from start to finish if it goes through n.
#     fScore := map with default value of Infinity
#     fScore[start] := h(start)
#
#     while openSet is not empty
#         // This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
#         current := the node in openSet having the lowest fScore[] value
#         if current = goal
#             return reconstruct_path(cameFrom, current)
#
#         openSet.Remove(current)
#         for each neighbor of current
#             // d(current,neighbor) is the weight of the edge from current to neighbor
#             // tentative_gScore is the distance from start to the neighbor through current
#             tentative_gScore := gScore[current] + d(current, neighbor)
#             if tentative_gScore < gScore[neighbor]
#                 // This path to neighbor is better than any previous one. Record it!
#                 cameFrom[neighbor] := current
#                 gScore[neighbor] := tentative_gScore
#                 fScore[neighbor] := tentative_gScore + h(neighbor)
#                 if neighbor not in openSet
#                     openSet.add(neighbor)
#
#     // Open set is empty but goal was never reached
#     return failure
