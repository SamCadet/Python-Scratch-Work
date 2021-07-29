# https://youtu.be/2u_ZExcNBzA

a = set()
print(a)
a.add(1)
print(a)

dat_list = [3, 3, 3, 1, 1, 1, 6, 4, 8, 90, 44, 5]

new_set = set()
for x in dat_list:
    new_set.add(x)
print(new_set)


dat_list2 = []
for x in new_set:
    dat_list2.append(x)
print(dat_list2)

dat_list3 = [1, 3, 4, 1, 3]

new_set2 = set()
for x in dat_list3:
    new_set2.add(x)
    x = x + 1
# sum(new_set2)

total = 0
for x in new_set2:
    total += x

print(total)
