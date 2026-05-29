# Assignment 5 - Q1 - Game Search Algorithms

## Aim

To implement and compare different game search algorithms used in Artificial Intelligence for decision making in games.

The following algorithms were implemented:

- Minimax Search
- Alpha-Beta Search
- Heuristic Alpha-Beta Search
- Monte-Carlo Tree Search (MCTS)

The algorithms were tested using the Tic-Tac-Toe game.

---

# Introduction

Game search algorithms are used in Artificial Intelligence to determine the best possible move in a game by exploring future game states.

These algorithms help an agent make optimal decisions by evaluating possible outcomes and selecting the move that maximizes its chances of winning.

Tic-Tac-Toe was chosen as the example game because it is simple and suitable for demonstrating search-based decision making.

---

# Algorithms Implemented

### 1. Minimax Search

Minimax explores all possible game states and selects the move that gives the best outcome assuming both players play optimally.

Player X is considered the maximizing player and Player O is considered the minimizing player.

---

### 2. Alpha-Beta Search

Alpha-Beta Search is an optimized version of Minimax.

It reduces the number of game states explored by pruning branches that cannot affect the final decision, making the search faster while producing the same result as Minimax.

---

### 3. Heuristic Alpha-Beta Search

Heuristic Alpha-Beta Search uses a depth limit and a heuristic evaluation function.

Instead of exploring the complete game tree, it estimates the quality of a board position when the depth limit is reached.

This helps reduce computation time for larger search spaces.

---

### 4. Monte-Carlo Tree Search (MCTS)

Monte-Carlo Tree Search uses random simulations to estimate the best move.

The algorithm performs multiple random playouts from possible moves and selects the move that produces the best results.

Since MCTS uses randomness, the output may vary between different executions.

---

# Game Used

Tic-Tac-Toe is a two-player zero-sum game.

Players:

- X → Maximizing Player
- O → Minimizing Player

Utility values used:

```text
X Wins = +1
O Wins = -1
Draw   = 0
```

---

# Test Cases

## Test Case 1

Board:

```text
X | X |
O | O |
  |   |
```

Player to Move:

```text
X
```

Expected Result:

```text
X should place at position 2 and win.
```

Output:

```text
Minimax Move: 2 Value: 1
Alpha-Beta Move: 2 Value: 1
Heuristic Alpha-Beta Move: 2 Heuristic Value: 100
MCTS Move: 2
```

---

## Test Case 2

Board:

```text
X | O | X
  | O |
  |   |
```

Player to Move:

```text
X
```

Output:

```text
Minimax Move: 7 Value: 0
Alpha-Beta Move: 7 Value: 0
Heuristic Alpha-Beta Move: 7 Heuristic Value: 10
MCTS Move: may vary
```

---

## Test Case 3

Board:

```text
X | O | X
O | X |
  |   | O
```

Player to Move:

```text
X
```

Expected Result:

```text
X should place at position 6 and win.
```

Output:

```text
Minimax Move: 6 Value: 1
Alpha-Beta Move: 6 Value: 1
Heuristic Alpha-Beta Move: 6 Heuristic Value: 100
MCTS Move: 6
```

---

## Test Case 4

Board:

```text
O | O |
X | X |
  |   |
```

Player to Move:

```text
O
```

Expected Result:

```text
O should place at position 2 and win.
```

Output:

```text
Minimax Move: 2 Value: -1
Alpha-Beta Move: 2 Value: -1
Heuristic Alpha-Beta Move: 2 Heuristic Value: -100
MCTS Move: 2
```

---

# Observation

- Minimax and Alpha-Beta produced the same optimal moves.
- Alpha-Beta reduced unnecessary search through pruning.
- Heuristic Alpha-Beta used board evaluation to make decisions with limited search depth.
- Monte-Carlo Tree Search produced good results using random simulations.
- MCTS may generate different moves in different runs because of randomness.

---

# Conclusion

The Minimax, Alpha-Beta, Heuristic Alpha-Beta, and Monte-Carlo Tree Search algorithms were implemented successfully using Tic-Tac-Toe.

The implementation was tested on multiple board positions to verify the correctness of the algorithms. The results demonstrate how different game search techniques can be used to make intelligent decisions in adversarial environments.
