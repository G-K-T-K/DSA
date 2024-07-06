nums = [2,7,11,15]
target = 9
i = 0
while i < len(nums):
    sum = target - nums[i]
    j = i + 1
    while j < len(nums):
        if nums[j] == sum:
            print([i,j])
            j+=1
        i+=1
    print([-1,-1])