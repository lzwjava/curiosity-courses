ages = {'li': 19, 'wang': 28, 'he' : 7}
for name, age in ages.items():
    print(name, age)

# li 19
# wang 28
# he 7    

for name in ages:
    print(name)
    
# li
# wang
# he    

# for name, age in ages:
#     print(name)

# ValueError: too many values to unpack (expected 2)    

for i, name in enumerate(['li', 'wang', 'he']):
    print(i, name)

# 0 li
# 1 wang
# 2 he    

print(reversed([1, 2, 3]))
# <list_reverseiterator object at 0x10701ffd0>

print(list(reversed([1, 2, 3])))
# [3, 2, 1]

