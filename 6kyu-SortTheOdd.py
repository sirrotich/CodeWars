# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_array(arr):
    arr1 = []
    for i in arr:
        if i % 2 != 0:
            arr1.append(i)
        arr1.sort()
        
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            arr1.insert(j, arr[j])
    return arr1