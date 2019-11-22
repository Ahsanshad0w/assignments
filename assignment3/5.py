from collections import Counter

lst= [1,2,3,4,3,2,1,5,6,7,7]
values=Counter(lst)
for k in values:
    if values[k]>1:
        print(f"{k} has {values.get(k, '')} number of duplicates")