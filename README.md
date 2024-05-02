# ALX Interview Preparation: Lockboxes

Welcome to the ALX Interview Preparation repository! This project focuses on solving the Lockboxes problem, where you'll need to develop a method to determine if all boxes can be opened.

## Table of Contents

1. [Introduction](#introduction)
2. [Must Know](#must-know)
3. [Additional Resources](#additional-resources)
4. [Requirements](#requirements)
5. [Tasks](#tasks)
6. [Repo](#repo)

## Introduction

In this project, you'll be faced with a scenario where you have a number of locked boxes in front of you, each potentially containing keys to other boxes. Your task is to implement a method that can efficiently determine if all the boxes can be opened, given certain conditions.

## Must Know

To successfully tackle this project, it's crucial to have a solid understanding of the following key concepts:

- **Lists and List Manipulation**: You'll need to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically. [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

- **Graph Theory Basics**: Knowledge of graph theory, especially traversal algorithms like Depth-First Search or Breadth-First Search, can be helpful as boxes and keys can be represented as nodes and edges in a graph. [Graph Theory](https://www.khanacademy.org/computing/computer-science/algorithms)

- **Algorithmic Complexity**: Understanding the time and space complexity of your solution is important for writing efficient algorithms. [Big O Notation](https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/)

- **Recursion**: Some solutions might require a recursive approach to traverse through the boxes and keys. [Recursion in Python](https://realpython.com/python-recursion/)

- **Queue and Stack**: Knowledge of queues and stacks is crucial if implementing breadth-first search (BFS) or depth-first search (DFS) algorithms to traverse through the keys and boxes. [Python Queue and Stack](https://www.geeksforgeeks.org/queue-in-python/)

- **Set Operations**: Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process. [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

By reviewing these concepts and utilizing the provided resources, you'll be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

## Additional Resources

- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/TJ0FJhWeEGolIqMpwBn7Pg)

## Requirements

### General

- **Allowed editors**: vi, vim, emacs
- **Interpreted/compiled on**: Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File requirements**:
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A README.md file, at the root of the folder of the project, is mandatory
- **Coding standards**:
  - Your code should be documented
  - Your code should use the PEP 8 style (version 1.7.x)
- **Executable files**: All your files must be executable

## Tasks

### 0. Lockboxes (mandatory)

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- **Prototype**: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

Example:
```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False

