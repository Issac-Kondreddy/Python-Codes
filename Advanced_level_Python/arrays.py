#Array can be handled in Python by a module named Array

"""
Some of the basic operations supported by an array are as follows:

Traverse - It prints all the elements one by one.
Insertion - It adds an element at the given index.
Deletion - It deletes an element at the given index.
Search - It searches an element using the given index or by the value.
Update - It updates an element at the given index.
"""

import array as arr

array = arr.array('i',[1,2,3,4,5,6,7,8,9])

for i in range(0,len(array)):
    print(array[i], end=" ")


array[5] = 55
array[2:4] = arr.array('i',[34,23])

print()
for i in range(0, len(array)):
    print(array[i], end=" ")

print()
print(len(array))