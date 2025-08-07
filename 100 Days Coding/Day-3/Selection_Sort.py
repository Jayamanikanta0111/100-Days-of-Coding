li=[23,34,12,45,67,89,21,56]
n = len(li)
for i in range(n-1):
  # Assume the current position is the minimum
  min_index = i
  for j in range(i+1, n):
     # Find the index of the minimum element in the unsorted part
     if li[j] < li[min_index]:
       min_index = j
  # Remove the minimum element and insert it at the correct position
  min_value = li.pop(min_index)
  li.insert(i, min_value)

# Print the sorted list
print(li)