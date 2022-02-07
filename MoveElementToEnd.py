#given an array and a target number, the goal is to find the target number in ther array and then move those target numbers to the end of the array.

# O(n) time | O(n) space
def moveElementToEnd(array, toMove):
    idx = 0
    idj = len(array) - 1
    # We've just made to pointers at the start and the end of the array to call upon in the while loop.
    while idx < idj:
        while idx < idj and array[idj] == toMove:
            idj -= 1
        # The first condition will check if the first pointer and is less than the second pointer, AND the second pointer is equal to the target number(2), move the second pointer down one.
        if array[idx] == toMove:
            array[idx], array[idj] = array[idj], array[idx]
        idx += 1
        # this second condition will check if the first pointer is equal to the target number(2) if so, it will swap the integers of idx and idj, moving them the target number to the back to the array - just as we want them to.
        # it will then move the idx up the array.
    return array
    # Once we have reordered the array in place and all the idj integers are bigger than the idx integers. Remeber that as the reordering takes place the idj moves to the left so at this stage, all the large numbers should be on the left of the array - moving down.
    # then this will print our reordered array


blah = moveElementToEnd([2,3,2,1,2,4,2,4,2], 2)
print(blah)