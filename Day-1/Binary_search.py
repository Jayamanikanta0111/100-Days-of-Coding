def binary_search(arr, val):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1

    # Continue searching while the search space is valid
    while left <= right:
        # Find the middle index
        mid = (left + right) // 2
        mid_val = arr[mid]  # Get the value at the middle index

        # Check if the middle value is the target
        if mid_val == val:
            return mid  # Target found, return its index
        # If the middle value is less than the target, search the right half
        elif mid_val < val:
            left = mid + 1
        # If the middle value is greater than the target, search the left half
        else:
            right = mid - 1

    # Target not found, return -1
    return -1

# Example usage
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Sorted list to search
x = 5  # Value to search for
result = binary_search(mylist, x)  # Call the function

# Print the result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")