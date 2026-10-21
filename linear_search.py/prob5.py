#find the second occurence
arr = [5, 2, 5, 8, 5]
target = 5

count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count += 1

        if count == 2:
            print(i)
            break
else:
    print("Second occurrence not found")