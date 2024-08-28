arr = [1,2,3,4,5,6,7]

def reverse_subarray(arr, start, end):
    arr[start:end+1] = arr[start:end+1][::-1]
    return arr

# range inclusive
def reverseSubArray(self,arr,l,r):
		arr[l-1:r] = arr[l-1:r][::-1]
		return arr