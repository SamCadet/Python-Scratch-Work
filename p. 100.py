import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

# p. 102
print(int('3' * 2) / 11)
