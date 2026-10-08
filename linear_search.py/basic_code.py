# Linear Search in Python
numbers = [10, 25, 30, 45, 50, 65, 70]

# Element to search
target = 45

# Linear Search
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found!")
        print("Element:", target)
        print("Index:", i)
        found = True
        break

if not found:
    print("Element not found!")