# This is a test file in Python 3

print('Welcome to the new file... By vg.\n')

name_ = input('Hi. Insert your name: ')

while True:
  if name_.isdigit():
    print('\nInvalid name. Please try again.')
    name_ = input('Insert your name: ')
    continue

  else:
    print('\nHi {name_}, nice to meet you.', name_)
    break

print('That\'s all folk!, bye!')


