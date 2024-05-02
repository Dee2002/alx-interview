#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the locked boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    # Initialize a list to keep track of visited boxes
    visited = [False] * len(boxes)
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Initialize a stack with the index of the first box

    # DFS to traverse through the boxes and keys
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes are visited
    return all(visited)
