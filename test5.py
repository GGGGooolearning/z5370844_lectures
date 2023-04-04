lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evennum(lst):
    lst2 = []
    for x in lst:
        if x % 2 == 0:
            lst2.append(x)
        else:
            continue
    return lst2


print(evennum(lst1))
'''
# Create a list with all even integers from 0 to 1 million
evens = []
for x in range(1_000_000 + 1):
    if x % 2 == 0:
        evens.append(x)

print(evens[:10])


pairs = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]
# Create an empty dictionary
dic = {}                      # (1)

# Iterate over each tuple in `pairs` and update the dictionary
for key, value in pairs:      # (2)
    dic.update({key:value})   # (3)

print(dic)
# Create a list with all even integers from 0 to 1 million
evens = [x for x in range(1_000_000 + 1) if x % 2 == 0]
print(evens[:10])


pairs = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]
# This WILL work
dic = {key:value for key, value in pairs}
print(dic)
'''

lst3 = [2,3,10,14,20,21,25,13,15]
sqlst = [x for x in lst3 if x * x > 150]
#print(sqlst)

lst4 = [0,1,1,2,5,6,8,2,4,6,8]
unlst = list({x for x in lst4 if x % 2 == 0})
#unlst = [i for i in set(lst4) if i % 2 == 0]
unlst.sort()
print(unlst)
#print(type(unlst))
