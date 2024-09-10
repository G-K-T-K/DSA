prices = [7,1,5,3,6,4]
if not prices :
    print(0)
        
min = float('inf')
maxprof = 0

for price in prices :
    if price < min :
        min = price
    elif (price - min) > maxprof:
        maxprof = price - min
print(maxprof)
