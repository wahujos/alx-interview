#!/usr/bin/python3
"""module commented documentation"""


def canUnlockAll(boxes):
    """Documenting the function"""
    # keys we processed
    set_of_keys = [0]
    # boxes we have visited
    visited_boxes = set()
    while set_of_keys:
        current_box = set_of_keys.pop()
        visited_boxes.add(current_box)
        keys_in_current_box = boxes[current_box]
        for key in keys_in_current_box:
            if key < len(boxes) and key not in visited_boxes:
                set_of_keys.append(key)
    return len(visited_boxes) == len(boxes)
