arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]
arr3 = arr1 + arr2
x = set(arr3)
y = len(x)
print(x,y)

a = list(set(arr1) & set(arr2))
b = len(a)
print(a,b)