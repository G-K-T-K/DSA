import random
nums = [3,2,3,1,2,4,5,5,6]
k = 4
def findKthLargest(self,nums):
    pivot = random.choice(nums)
    left = [x for x in nums if x < pivot]
    right = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
            
    if k <= len(right): 
        return self.findKthLargest(right, k)
    elif k > len(right) + len(mid):
        return self.findKthLargest(left, k - len(right) - len(mid))
    else: 
        return mid[0]