import os 
os.system ('cls' if os.name == 'nt' else 'clear')

from collections import deque

# Define the updated prison layout with guards(G), walls(#), start(S), End(E) and Free Space(.)
prison = [
    ['S', '.', '#', '.', '.', '.','.'],
    ['#', '.', '#', '.', '#','G', '.'],
    ['.', '.', '.', '.', '#','.', '.'],
    ['#', 'G', '.', '.', '#','.','.'],
    ['#', '#', '.', 'G', '#','.', 'G'],
    ['#', '#', 'G', 'G', '#','.', 'G'],
    ['#', '#', '.', 'G', 'E', '.', '.']
]

# Define directions for moving in the grid (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS algorithm to find the shortest path while avoiding guards
def escape_prison(prison):
    # Find the starting point (S)
    for i in range(len(prison)):
        for j in range(len(prison[0])):
            if prison[i][j] == 'S':
                start = (i, j)

    # Queue for BFS, starting from the start position
    queue = deque([(start, [])])  # stores (current position, path taken)
    visited = set([start])  # track visited cells

    while queue:
        (x, y), path = queue.popleft()

        # If we reach the exit, return the path
        if prison[x][y] == 'E':
            return path + [(x, y)]

        # Explore each direction
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the new position is within bounds, open, and not a guard
            if 0 <= nx < len(prison) and 0 <= ny < len(prison[0]) and (nx, ny) not in visited:
                if prison[nx][ny] != '#' and prison[nx][ny] != 'G':  # not a wall or guard
                    queue.append(((nx, ny), path + [(x, y)]))
                    visited.add((nx, ny))

    return None  # No path found

# Run the escape algorithm
path = escape_prison(prison)

if path:
    print("Escape path found:", path)
else:
    print("No escape path exists.")
