def partition(array, low, high):
  # Choose the last element as pivot
  pivot = array[high]
  # Pointer for greater element
  i = low - 1

  # Traverse through all elements
  for j in range(low, high):
     # If current element is smaller than or equal to pivot
     if array[j] <= pivot:
       i += 1
       # Swap elements at i and j
       array[i], array[j] = array[j], array[i]

  # Swap the pivot element with the element at i+1
  array[i+1], array[high] = array[high], array[i+1]
  # Return the partitioning index
  return i+1

def quicksort(array, low=0, high=None):
  # Set high to last index if not provided
  if high is None:
    high = len(array) - 1

  # Only sort if there are at least two elements
  if low < high:
    # Find the partition index
    pivot_index = partition(array, low, high)
    # Recursively sort elements before and after partition
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)

# Example
mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)  # Output will be the sorted list