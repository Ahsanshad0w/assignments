d={'english':0, 'urdu': 0, 'computer science': 0, 'geography': 0, 'history': 0}
for k in d:
    marks=int(input(f"Enter marks for {k}: "))
    d[k]= marks
print("Results")

for k in d:
    print(f"{k} : {d[k]}")

print("Total :", sum(d.values(1)) )