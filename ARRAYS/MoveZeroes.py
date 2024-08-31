nums = [0,1,0,3,12]
nz_index = 0
for i in range(len(nums)) :
    if nums[i] != 0 :
        nums[nz_index], nums[i] = nums[i],nums[nz_index]
        nz_index += 1

print(nums)