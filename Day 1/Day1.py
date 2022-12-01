#Part One
List = [l.strip() for l in open('./list.py')]
k = []
for elf in ('\n'.join(List)).split('\n\n'):
    i = 0
    for x in elf.split('\n'):
        i += int(x)
    k.append(i)
    print(sorted(k))

#Part Two
List = [l.strip() for l in open('./list.py')]
k = []
for elf in ('\n'.join(List)).split('\n\n'):
    i = 0
    for x in elf.split('\n'):
        i += int(x)
    k.append(i)
    print(max(k))


sum = 67966 + 69727 + 69883
print(sum)
