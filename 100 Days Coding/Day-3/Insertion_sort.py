mylist = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(mylist)
for i in range(1,n):
  # Select the element to be inserted
  insert_index = i
  current_value = mylist.pop(i)
  for j in range(i-1, -1, -1):
    # Find the correct position for the current_value
    if mylist[j] > current_value:
      insert_index = j
  # Insert the element at its correct position
  mylist.insert(insert_index, current_value)

# Print the sorted list
print(mylist)