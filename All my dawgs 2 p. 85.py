dog_names = []
while True:
    print('Enter the name of the dog ' + str(len(dog_names) + 1) +
          ' (or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    dog_names = dog_names + [name]  # list concatenation

print('The dog names are:')
for name in dog_names:
    print(' ' + name)
