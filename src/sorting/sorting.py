# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # starting at the beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`
    # placement in left and right array
    i=0
    j=0
    # placement in merged array
    k=0
    # puts the elements back in the right spot in the merged array
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            i=i+1
        else:
            merged_arr[k]=arrB[j]
            j=j+1
        k=k+1

    while i < len(arrA):
        merged_arr[k]=arrA[i]
        i=i+1
        k=k+1

    while j < len(arrB):
        merged_arr[k]=arrB[j]
        j=j+1
        k=k+1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len( arr ) > 1:
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces
        # split the arr in half
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        # split left and right in half recursive
        # merge_sort(left)
        # merge_sort(right)
        # was having difficults with the return so desided to move tthe recursion into the function call
        arr = merge(merge_sort(left), merge_sort(right))
        # i=0
        # j=0
        # k=0 
        # while i < len(left) and j < len(right):
        #     if left[i] <= right[j]:
        #         arr[k]=left[i]
        #         i=i+1
        #     else:
        #         arr[k]=right[j]
        #         j=j+1
        #     k=k+1

        # while i < len(left):
        #     arr[k]=left[i]
        #     i=i+1
        #     k=k+1

        # while j < len(right):
        #     arr[k]=right[j]
        #     j=j+1
        #     k=k+1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

