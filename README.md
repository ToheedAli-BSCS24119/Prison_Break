# Prison_Break
Discrete Structure Show and Tell Project of Prison Break
# Agenda
1. Introduction to Graph Theory
2. Prison Break Concept in Graph Theory
3. Logic and Propositions
4. Set theory
5. Combination and Permutations
6. Path Finding Algorithm(BFS and DFS)
7. Comparison of Algorithm
8. Live demo of Prison Break (Code)
9. Real_World Application
10. Thought Provoking Questions & Discussion
# Introduction to Graph Theory:
Graph theory is a branch of mathematics that studies structures formed by nodes (vertices) and edges (connections). It allows us to represent and analyze relationships and pathways in a variety of systems, such as social networks, road maps, and communication networks. Graphs provide a way to visualize and solve problems involving connectivity and flow. In the context of our project, graph theory helps us model and understand the "Prison Break" setup.

# Prison Break Concept in Graph Theory:
The "Prison Break" concept uses graph theory to represent a prison layout, where cells, guards, and hallways become nodes, and possible escape routes are edges. This model helps us simulate escape strategies by visualizing the relationships and potential movements within the prison. By treating the prison as a graph, we can apply algorithms to find optimal paths, avoid obstacles, or even locate safe zones. This graphical representation is crucial in designing and analyzing escape plans.

# Logic and Propositions:
Logic involves reasoning through true or false statements, known as propositions, to build structured arguments or decisions. In "Prison Break," logical statements can model guard behaviors, alarm triggers, or safe passage conditions. Boolean logic helps us combine propositions to form complex conditions necessary for planning an escape. For instance, by combining propositions, we can decide if a particular escape route is feasible based on guard placements.

# Set Theory:
Set theory allows us to group related objects, such as different groups of cells, accessible paths, or guard positions, to manage them systematically. In the "Prison Break" model, sets can represent cells within guard sight, possible escape routes, or even restricted zones. Using unions, intersections, and differences between sets, we can refine our escape plans by determining areas that are safe, unsafe, or accessible. This mathematical foundation helps us define clear relationships between different parts of the prison layout


# Combination and Permutations:
Combinations and permutations help calculate the different ways of arranging or selecting escape routes and movements, taking order and grouping into account. In "Prison Break," they allow us to examine multiple possible sequences of moves or select the optimal paths considering various conditions. For example, by calculating permutations of movements, we can simulate different escape routes and assess their success probabilities. This combinatorial approach provides a structured way to explore all possible actions for effective escape planning.

A BIT MORE EXPLANATION:
Formula for permutations:
P(n,r)=n!/(n-r)!
Where:
•	n= total number of objects,
•	r = number of objects selected,
•	! represents factorial (e.g., 5!=5×4×3×2×15! = 5 \times 4 \times 3 \times 2 \times 1 times=5×4×3×2×1).
Formula for combinations:
C(n,r)=n!/r!(n-r)!Where:
•	n = total number of objects,
•	r = number of objects selected.
suppose i have 1 prisoner that will escape and 3 escape routes
then combination will be better to use
hence I have 
C(3,1)=3!/1!(3-1)!
C(3,1)=3
HENCE 3 POSSIBLE COMBINATIONS OF ESCAPE NOW I WILL USE MORE ROUTES AND GUARDS AND WALLS AND TRAPS ETC ETC

# Path Finding Algorithm (BFS and DFS):
Breadth-First Search (BFS) and Depth-First Search (DFS) are foundational graph algorithms that explore possible paths through a network of nodes. BFS systematically explores each level, ideal for finding the shortest path in an unweighted graph, while DFS dives deep into each branch, useful for exhaustive exploration. In "Prison Break," these algorithms help identify viable escape routes, prioritize paths, and navigate around obstacles like guards or locked doors. By applying BFS or DFS, we can determine the quickest or safest escape plan.
