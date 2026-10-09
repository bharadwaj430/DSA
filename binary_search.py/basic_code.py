
# Binary Search in Python

# Given sorted list
arr = [10, 20, 30, 40, 50, 60, 70]

# Element to search
target = int(input("Enter the element to search: "))

# Initialize pointers
low = 0
high = len(arr) - 1

# Binary Search
while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index:", mid)
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Element not found")
