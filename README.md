Collatz Conjecture Visualizer 🔢📊

A Python program that demonstrates the Collatz Conjecture (3n + 1 problem) for a given range of numbers. It calculates how many steps each number takes to reach 1 and visualizes the results with a line graph.

📌 Features

Validates input range (positive integers only).

Applies Collatz rules (n → 3n + 1 if odd, n → n/2 if even).

Tracks and prints the sequence for each number.

Finds numbers with minimum and maximum iterations.

Plots a graph of Numbers vs Iterations using Matplotlib.

💻 Example
Input:
ENTER LOWER LIMIT: 5
ENTER UPPER LIMIT: 10

Output:
5 → 16 → 8 → 4 → 2 → 1
No. of iterations: 5
...
10 → 5 → 16 → 8 → 4 → 2 → 1
No. of iterations: 6

5 has the lowest no. of iterations, 5 in this range.
10 has the highest no. of iterations, 6 in this range.


Graph:
📈 Line chart showing how many iterations each number took.

▶️ Usage

Run the script with Python:

python collatz.py
