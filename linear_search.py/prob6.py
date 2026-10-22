#find the first number greater than a given value
arr = [4, 9, 2, 15]
target = 8

found = False

for i in range(len(arr)):
    if arr[i] > target:
        print(arr[i])
        found = True
        break

if not found:
    print("No greater number found")