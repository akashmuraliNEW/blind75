from collections import defaultdict


strs = ["act","pots","tops","cat","stop","hat"]
dict1 = defaultdict(list)
for s in strs:
    count = [0] * 26
    for c in s:
        count[ord(c)-ord("a")]+=1
    # print(count)
    dict1[tuple(count)].append(s)
print( dict1.values())
