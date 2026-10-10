#Problem statement: Given a list of integers and a target number, find the index of the target using Linear Search. If the target is not present, print -1.

# Linear Search - Beginner Problem

arr = [10, 20, 30, 40, 50]
target = 30

found = -1

for i in range(len(arr)):
    if arr[i] == target:
        found = i
        break

print("Index:", found)
