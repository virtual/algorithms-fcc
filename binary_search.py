def binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    first = 0
    last = len(list) - 1

    # Keep executing while loop while val of first <= last
    while first <= last:
        midpoint = (first + last) // 2 # floor division
        if (list[midpoint] == target):
            return midpoint
        elif (list[midpoint] < target): # midpoint value is less than target
            # first changes to midpoint + 1
            first = midpoint + 1
        else: # midpoint value is more than target
            # last changes to midpoint
            last = midpoint - 1          
    
    # if not found after while loop, return None
    return None        

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers, 6)
verify(result)