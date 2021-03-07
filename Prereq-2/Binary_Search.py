# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    while l<r :
        mid = int((l+r) / 2)
        #print(mid)
        if arr[mid] is x :
            return mid
        elif arr[mid] < x:
            l = mid+1
        elif arr[mid] > x:
            r = mid-1
    return -1

# write your code here


# Test array
arr = [2, 3, 4, 10, 40]
x = 11

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
