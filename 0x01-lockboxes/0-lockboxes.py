#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the locked boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True  # Mark the first box as visited
    queue = [0]  # Initialize a queue with the index of the first box

    # BFS to traverse through the boxes and keys
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes are visited
    return all(visited)
