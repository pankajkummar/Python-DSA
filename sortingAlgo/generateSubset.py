a=[0,1,2,3]
def subs(l):
    if len(l) == 0:
        return []
    res = []
    subsets = subs(l[0:-1])
    res = res+subsets
    res.append([l[-1]])
    for sub in subsets:
        res.append(sub+[l[-1]])
    return res

print (subs(a))