list1 = [1, 2, 3, 4]
list2 = [8, 12, 45, 67, 89, 45]
list3 = [78, 90, 65]

for i in list1:
    list1.append(i)
    if len(list1) == 8:
        break

for z in list2:
    list2.append(z)
    if len(list2) == 12:
        break

for x in list3:
    list3.append(x)
    if len(list3) == 6:
        break

print(list1)
print(list2)
print(list3)

