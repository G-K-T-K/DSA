n = 5
arr1 = [1, 2, 3, 4, 5]  
m = 5 
arr2  = [1, 2, 3, 6, 7]
arr3 = []
ele = arr1[0]
for ele in arr1:
    if ele not in arr3:
        arr3.append(ele)
ele1 = arr2[0]
for ele1 in arr2:
    if ele1 not in arr3:
        arr3.append(ele1)
arr3.sort()
print (arr3)

arr3 = arr1 + arr2
x = sorted(set(arr3))
y = list(x)
print(y)