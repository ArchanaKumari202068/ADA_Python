# Implement Binary Search in python

# Repeat until low and high meet each other
def binarySearch(array, x, low, high):
    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1

array = [9, 11,2, 5, 6, 21, 8, 52,1]
x = 8

# Calling binarySearch function
output = binarySearch(array, x, 0, len(array)-1)

if output != -1:
    print("Element is present at index " + str(output))
else:
    print("Not found")