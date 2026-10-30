#find the first even number
arr = [1, 3, 7, 8, 10]

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i])
        break
else:
    print("No even number found")