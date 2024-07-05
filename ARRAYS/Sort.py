# arr = [1,6,4,5,7,8,3,1,6,5,9]
arr=[1,2,3,4,5,100,10]
c=0
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        # print("arr is sorted")
        c+=1
    else:
        print("not sorted")
        break
if(c==len(arr)-1):
    print("The array is sorted")