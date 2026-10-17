#search an absent element

arr = [2, 4, 6, 8]
target = 5

found = False

for i in range(len(arr)):
    if arr[i] == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")