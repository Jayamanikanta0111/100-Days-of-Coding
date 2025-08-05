def Merge(left, right):
    # Initialize an empty list to store the merged result
    result = []
    i = j = 0

    # Merge the two lists by comparing their elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from left or right
    result.extend(left[i:])
    result.extend(right[j:])
    
    # Return the merged sorted list
    return result
def merge_sort(array):
    # Base case: a list of zero or one elements is already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    # Merge the sorted halves
    return Merge(left_half, right_half)

# Example
mylist = [64, 34, 25, 5, 22, 11, 90, 12]
sorted_list = merge_sort(mylist)   
print(sorted_list)  # Output will be the sorted list