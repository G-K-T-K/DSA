arr = []
if len(s) != len(t):
    return False
        
arr = list(s)

for i in t :
    if i in arr:
        arr.remove(i)
    else:
        return False    
return True


----------------------


arr = []
if len(s) != len(t):
    return False
return sorted(s) == sorted(t)
