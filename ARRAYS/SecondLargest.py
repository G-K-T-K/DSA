arr = [3,2,1,5,2]
maximum = arr[0]
for element in arr:
    if element > maximum:
        maximum = element
arr.remove(maximum)
maximum1 = arr[0]
for element1 in arr:
    if element1 > maximum1:
        maximum1 = element1
print(maximum1)

arr = [3,2,1,5,2]
maximum = arr[0]
for element in arr:
    if element > maximum:
        maximum = element
maximum2 = -1
for element in arr:
    if element > maximum2 and element!=maximum:
        maximum2=element
print(maximum2)

arr = [3,2,1,5,2]
largest = arr[0]
slargest = -1
for i in arr:
    if i > largest:
        slargest = largest
        largest = i
    elif i < largest and i > slargest:
        slargest = i
print(slargest)