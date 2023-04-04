# tic = Qan.ax

string1 = '''John said,'dfdf'dfdf '''
print(string1)


def ret(height, wide, length):
    vol = height * wide * length
    print("The volume is : ", vol)


ret(30.5,33,56)

lst = [1, "string", True, None, True]
print(f"Original lst is {lst}")

lst.remove(True)
print(f"lst after removing the first True is {lst}")

lst.pop(2)
print(f"lst after removing the element CURRENTLY at index 2 is {lst}")

lst.pop()
print(f"lst after removing the CURRENT last element is {lst}")

str2 = 'From firstname.surname@unsw.edu.au Tue Oct 06'
lst2 = str2.split(".")
#lst3 = lst2[1].split(".")
print(lst2)
#print(lst3)
print(lst2[1])

domain = str2.split()[1].split('@')[1]
print(domain)

