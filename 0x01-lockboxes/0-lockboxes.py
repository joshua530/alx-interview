#!/usr/bin/python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened
'''


def canUnlockAll(boxes):
    '''checks whether a given list of boxes can be unlocked when
    given certain keys
    '''
    if len(boxes) == 0:
        return False

    keys = boxes[0].copy()
    current_key_i = 0
    # first box is unlocked
    unlocked_boxes = {'0': True}
    unlocked_boxes_count = 1

    while current_key_i < len(keys):
        key = keys[current_key_i]
        if key < len(boxes):
            # unlock the box and add its keys to the list of keys for unlocking
            # other boxes
            if str(key) not in unlocked_boxes:
                # if we've already opened a box, opening it again will just
                # cause key duplication and an infinite loop so we don't do it
                keys += boxes[key]
                unlocked_boxes[str(key)] = True
                unlocked_boxes_count += 1
        # if we have already unlocked all the boxes, our job is done, looping
        # further will just be a waste of resources
        if unlocked_boxes_count == len(boxes):
            break
        current_key_i += 1
    if unlocked_boxes_count == len(boxes):
        return True
    return False
