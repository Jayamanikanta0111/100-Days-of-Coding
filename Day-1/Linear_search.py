# Function to perform linear search
def linearSearch(lis, val):
  for i in range(len(lis)):
    # Check if the current element matches the value we're searching for
    if lis[i] == val:
      return i  # Return the index where the value is found
  return -1  # Return -1 if value not found in the list

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

# Call the function and store the result
result = linearSearch(mylist, x)

# Check the result and print appropriate message
if result != -1:
  print(f"Found at index {result}")
else:
  print("Value not found in the list")