# Algorithmic
## 1. Searching algorithms
### 1.1. Solutions without cost function
#### 1.1.1. Backtracking
This algorithm is used to search for solutions to problems in which a set of restrictions must be satisfied,
**without a function to evaluate them**, that is, there are no better or worse solutions.

The search in the tree of states is carried out in depth,
evaluating each of them and pruning those that cannot generate feasible solutions (they do not satisfy any restriction).
When this happens the algorithm returns to the previous state and continues looking for a solution (**backtracking**).

The solution of two typical problems has been implemented, such as the n-queens and the sudoku puzzle.
The way in which the state tree has been represented in both cases has been through a list that stores the nodes to explore `__nodes_to_explore`. 
The nodes to be explored represent each of the depth levels of the tree and are extracted following a FIFO order.
The depth of the tree is determined by the node we are exploring and the width by each of the possible values that this node can take.
When a list node is eliminated, the depth of the tree is increased by 1 and a recursive call is made to explore the rest of the tree,
if no solution is found, the node is reinserted at the beginning of the list (**backtracking**),
a state is solution if the list of nodes to explore is empty.

![n-queens tree](./resource/media/n-queens_backtracking.gif)

n-queens tree

media source: https://ktiml.mff.cuni.cz/~bartak/constraints/propagation.html

As the algorithm is implemented, we can search and return the first solution found by the algorithm `solve()`
or return all solutions `solve_all_solutions()`.

In n-queens problem we can use an empty board (`[-1, -1, -1, -1]`) or fix the position of any of the queens on the board to generate the possible solutions.

```python
print('First solution')
nQueens = NQueensBacktracking([-1, -1, -1, -1, -1])
print(nQueens.solve())

print('All solutions')
nQueens = NQueensBacktracking([-1, -1, -1, -1, -1])
for solution in nQueens.solve_all_solutions():
    print(solution)
```
```
First solution
[0, 2, 4, 1, 3]
All solutions
[0, 2, 4, 1, 3]
[0, 3, 1, 4, 2]
[1, 3, 0, 2, 4]
[1, 4, 2, 0, 3]
[2, 0, 3, 1, 4]
[2, 4, 1, 3, 0]
[3, 0, 2, 4, 1]
[3, 1, 4, 2, 0]
[4, 1, 3, 0, 2]
[4, 2, 0, 3, 1]
```
```python
print('First solution')
nQueens = NQueensBacktracking([-1, -1, 4, -1, -1])
print(nQueens.solve())

print('All solutions')
nQueens = NQueensBacktracking([-1, -1, 4, -1, -1])
for solution in nQueens.solve_all_solutions():
    print(solution)
```
```
First solution
[0, 2, 4, 1, 3]
All solutions
[0, 2, 4, 1, 3]
[3, 1, 4, 2, 0]
```
