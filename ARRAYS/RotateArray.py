nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
k = k % n
nums = nums[n-k:] + nums[:n-k]
print(nums)

n = len(nums)
k = k % n
x = n - k
nums1 = nums[0:x]
nums[0:x] = []
nums.extend(nums1)