# Leetcode Solutions

## Solution Strategies
Here are some common stategies that can be used to solve LeetCode problems:

Brute force: This is the simplest and most straightforward approach to solve a problem by iterating through all possible solutions. Although it may work for small inputs, it may not scale for larger inputs.

Greedy Algorithms: This approach involves making locally optimal choices at each step of the algorithm, hoping to find a global optimal solution. It can be efficient in some cases, but may not always find the optimal solution.

Divide and conquer: This approach involves dividing the problem into smaller sub-problems, solving each sub-problem recursively, and then combining the results to solve the original problem. This approach is commonly used in searching and sorting algorithms.

Dynamic Programming: This approach involves breaking down a problem into smaller sub-problems and storing the solutions to each sub-problem to avoid redundant computations. Dynamic programming is commonly used to solve problems where the optimal solution can be built from optimal solutions to smaller sub-problems.

Backtracking: This approach involves exploring all possible solutions by incrementally building candidates to the solutions, and abandoning a candidate ("backtracking") as soon as it is determined that the candidate cannot possibly be completed to a valid solution.

Binary Search: This approach involves dividing the search space in half at each step, eliminating half of the remaining possibilities until the desired solution is found.

Graphs and Trees: This approach involves representing a problem as a graph or tree, and using algorithms such as breadth-first search, depth-first search, and Dijkstra's algorithm to traverse the graph or tree and find the solution.

## Time Complexity
Time complexity is a measure of the amount of time a program takes to execute as the size of the input grows. It is often expressed in Big O notation, which provides an upper bound on the growth rate of the algorithm's time as the size of the input increases. Here are the most common examples of time complexity in Big O notation:

O(1) - constant time complexity: This indicates that the algorithm takes a constant amount of time, regardless of the size of the input. Examples of O(1) algorithms include accessing an array element, performing basic arithmetic operations, and returning a constant value.

O(log n) - logarithmic time complexity: This indicates that the algorithm's running time increases logarithmically as the size of the input increases. Examples of O(log n) algorithms include binary search, finding an element in a balanced binary tree, and certain divide-and-conquer algorithms.

O(n) - linear time complexity: This indicates that the algorithm's running time increases linearly with the size of the input. Examples of O(n) algorithms include iterating over an array, finding the maximum or minimum element in an unsorted array, and computing the sum of elements in an array.

O(n log n) - linearithmic time complexity: This indicates that the algorithm's running time increases by the product of the input size and the logarithm of the input size. Examples of O(n log n) algorithms include sorting algorithms such as merge sort, quicksort, and heap sort.

O(n^2) - quadratic time complexity: This indicates that the algorithm's running time increases quadratically with the size of the input. Examples of O(n^2) algorithms include nested loops, matrix multiplication, and bubble sort.

O(2^n) - exponential time complexity: This indicates that the algorithm's running time increases exponentially with the size of the input. Examples of O(2^n) algorithms include the subset sum problem, the traveling salesman problem, and the knapsack problem.

In general, algorithms with lower time complexity are more efficient than those with higher time complexity. 
