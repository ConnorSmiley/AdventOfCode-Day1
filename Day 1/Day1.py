#Part One
List = [l.strip() for l in open('./list.py')]
L = []
for elf in ('\n'.join(List)).split('\n\n'):
    i = 0
    for x in elf.split('\n'):
        i += int(x)
    L.append(i)
    print(sorted(L))

#Part Two
List = [l.strip() for l in open('./list.py')]
L = []
for elf in ('\n'.join(List)).split('\n\n'):
    i = 0
    for x in elf.split('\n'):
        i += int(x)
    L.append(i)
    print(max(L))


sum = 67966 + 69727 + 69883
print(sum)
