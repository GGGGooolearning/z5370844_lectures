x = '1234567890'
y = x[:5]
print(y)

COLWIDTHS = {'Volume': 14, 'Date': 11, 'Adj Close': 19, 'Close': 10, 'Open': 6, 'High': 20}
lst = []
for a, b in COLWIDTHS.items():
    lst.append(b)
    print(lst)

print(type(b))
print(lst[0])