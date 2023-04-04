import math

tuple=('a','b','c')
newTuple = (tuple,'f','g')
#tuple  = ('g','h')
print(newTuple)

v1 = 'a'
v2 = 'a'
v3 = ['a']
v4 = ['a']
print(v1 is v2)
print(v3 is v4)
'''
workhour = int(input('How many working hours a week?'))
rate1 = 51.45
rate2 = 88.9

if workhour <= 35:
    print(workhour* rate1)
else:
    print(workhour*rate2)
    print(type(workhour))
'''
preNum = 0
larNum = 0
numbers = [20,9,1,5,7,2,11,0,3,12,3,15]
for i, x in enumerate(numbers):
    if i <= 0:
        perNum = x
    else:
        if perNum >= x:
            larNum = perNum
        else:
            larNum = x
print(larNum)

lis1 = [1,2,3]
lis2 = [1,2,3]
for i in lis1:
    for j in lis2:
        if i <= j:
          print(i, j)