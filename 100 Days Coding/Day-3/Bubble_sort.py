l1=[21,34,12,45,67,89,23,56]
for i in range(len(l1)-1):
    # Traverse the list from the beginning to the (n-i-1)th element
    for j in range(len(l1)-1-i):
        # Compare adjacent elements and swap if needed
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]
print("Sorted list:", l1)

