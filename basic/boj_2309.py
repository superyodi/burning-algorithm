i = 0
dwarf = []

while i < 9:
    dwarf.append(int(input()))
    i += 1

dwarf.sort()

f_sum = sum(dwarf) - 100
outs = set()

for i in range(8):
    for j in range(i+1, 9):
        if dwarf[i] + dwarf[j] == f_sum:
            outs = (i, j)
            break

# print(outs)
sum = 0
for i in range(9):
    if i in outs:
        continue
    sum += dwarf[i]
    print(dwarf[i])

# print("합:",sum)

