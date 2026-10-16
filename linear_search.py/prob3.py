#find the index
arr = [5, 8, 12, 15]
target = 12

index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print(index)