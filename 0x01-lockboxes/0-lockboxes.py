#!/usr/bin/python3
""" A method that determines
if all the boxes can be opened."""


def canUnlockAll(boxes):
    """A method that determines
    if all the boxes can be opened.
    Args:
        boxes: a list of lists.

    Returns:
        True if all boxes can be opened,
        else return False.
    """
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False
    return True
