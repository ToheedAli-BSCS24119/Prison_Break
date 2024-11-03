# Prison_Break
Discrete Structure Show and Tell Project of Prison Break
# Agenda
1. Introduction to Graph Theory
2. Prison Break Concept in Graph Theory
3. Breadth-First Search (BFS)
4. Depth-First Search (DFS)
5. Dijkstra’s Algorithm
6. A* Algorithm
7. Comparison of Algorithms
8. Live Demo of a Prison Break
9. Real-World Applications
10. Thought-Provoking Questions and Discussion

# Contribution 
We divided our work in the following manner:
1. Graph Theory: Toheed Ali
2. BFS: Bilawal Nouman
3. DFS: Taha Qureshi
4. Dijkstra’s Algorithm​: M.Ibraheem Tahir
5. A* Algorithm: Hassnain Javiad
# Graph Theory
1. Mapping the Prison: We can create a map (a graph) where rooms and hallways are connected like dots (nodes) and lines (edges). This makes it easier to plan possible routes to escape.​
2. Finding the Best Path: We can use math to find the shortest or safest way out, avoiding areas with guards or cameras.​
# Breadth-First Search (BFS) 
Breadth-First Search (BFS) is an algorithm that explores nodes in a graph layer by layer, starting from a given node. It visits all neighboring nodes before moving to the next level, ensuring the shortest path in unweighted graphs. BFS uses a queue to track nodes and is ideal for finding the shortest path in simple, evenly weighted environments like grids or mazes.
# Depth-First Search (DFS)
Depth-First Search (DFS) is an algorithm that explores as far down each branch of a graph as possible before backtracking. It dives deeply into each path from the starting node, using a stack (or recursion) to remember the path. DFS is effective for exploring all possible paths or configurations, but it doesn’t guarantee the shortest path in unweighted graphs.
# Dijkstra’s Algorithm
Dijkstra’s Algorithm is a graph search algorithm used to find the shortest path from a starting node to all other nodes in a weighted graph with non-negative edge weights. It works by maintaining a priority queue of nodes to explore, selecting the node with the smallest tentative distance, and updating the distances of its neighbors. The algorithm continues until all nodes have been processed, resulting in the shortest path from the starting node to each reachable node.
# A* (A-Star)
A* (A-Star) is a pathfinding algorithm that finds the shortest path by combining actual path cost with a heuristic estimate of the remaining distance to the goal. It prioritizes paths that are likely to lead closer to the destination, balancing optimality and speed. A* is widely used in scenarios with weighted paths, such as robotics and games, where finding efficient routes in complex environments is essential.
