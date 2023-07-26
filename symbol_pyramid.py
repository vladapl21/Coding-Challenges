symbol = input('Enter a symbol: ')
finalrow = int(input('Odd number of symbols in the final row: '))

if finalrow%2 != 0:
  for i in range(1,finalrow+1,2):
    print(f'{" "*int(((finalrow-i)/2))}{symbol*i}{" "*int(((finalrow-i)/2))}')
else:
  print('Number has to be odd')