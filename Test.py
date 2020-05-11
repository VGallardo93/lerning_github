# This is a test file in Python 3

print('Welcome to the new file... By vg.\n')

name_ = input('Hi. Insert your name: ')

while True:
  if name_.isdigit():
    print('\nInvalid name. Please try again.')
    name_ = input('Insert your name: ')
    continue

  else:
    print(f'\nHi {name_}! Nice to meet you.\n')
    break

# Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
  print(f'{name:10} ==> {phone:10d}')

# As an example, the following lines produce a tidily-aligned set of columns giving integers and their squares and cubes:
for x in range(1, 11):
  print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('\n>>> That\'s all folk!, bye!\n')

#Thank you to see!
