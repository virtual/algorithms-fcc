def binary_search_recursive(list, target):
    """
    Returns true or false if target is found
    """

    if (len(list) == 0):
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if (list[midpoint] < target):
                # start:end, if no end provided goes to end automagically
                return binary_search_recursive(list[midpoint + 1: ], target)
            else:
                # list goes to midpoint (not midpoint - 1)
                # because Python list slicing is not inclusive of end position
                return binary_search_recursive(list[: midpoint], target)

def verify(result):
    if (result == True):
        print("Target found")
    else:
        print("target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
verify(binary_search_recursive(numbers, 5))
verify(binary_search_recursive(numbers, 16))