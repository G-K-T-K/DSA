n = 6
arr = [10, 5, 2, 7, 1, 9]
k = 15

# OUTPUT=4

sum = {}
curr_sum = 0
max_len = 0

for i in range(len(arr)) :
    curr_sum += arr[i]

    if curr_sum == k :
        max_len = i + 1

    if (curr_sum - k) in sum :
        max_len = max(max_len, i - sum[curr_sum - k])

    if curr_sum not in sum :
        sum[curr_sum] = i

print(max_len)