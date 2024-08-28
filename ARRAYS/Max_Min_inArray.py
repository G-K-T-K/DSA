arr = [3, 2, 1, 56, 10000, 167]
max = arr[0]
min = arr[0]
for i in arr:
    if i > max :
        max = i
print(max)
for i in arr:
    if i < min :
        min = i
print(min)