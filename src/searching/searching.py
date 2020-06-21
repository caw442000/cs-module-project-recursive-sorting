# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # return true if found
    # else return false
    # if len(arr) == 0:
    #     return

    if end >= start:                          
    
        middle = (start + end) // 2
        guess = arr[middle]

        if guess == target:
            return middle

        elif guess > target:
            end = middle - 1 

        elif guess < target:
            start = middle + 1

        return binary_search(arr, target, start, end)

    else:
        return -1
    
    



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass