arr = [11, 22, 33, 44, 55]
target = 44

count = 0

for i in range(len(arr)):
    count += 1

    if arr[i] == target:
        break

print(count)