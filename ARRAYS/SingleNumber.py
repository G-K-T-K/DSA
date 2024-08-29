nums = [4,1,2,1,2]
seen = []
for i in nums:
    if i not in seen:
        seen.append(i)
        i+=1
    elif i in seen:
        seen.remove(i)
        i+=1
print(seen[0])