#search by name
arr = ["Ram", "Ravi", "Sita"]
target = "Ravi"

index = -1

for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

print(index)