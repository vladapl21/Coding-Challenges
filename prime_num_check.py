num = int(input('Enter a number:  '))
prime=True

#we create a for loop with the number of iterations set to the number entered-3. Next, we divide num by all integers between 2 and num-1 (if there is no remainder - it divides exactly - we set prime to false and break the loop)
#We are adding 2 to i in the modular division because we cannot divide the numbers by 0 or 1 (not 1 because if a number divides by 1, it is not prime - this is the same reason why we -3 from num and not 2 because when i gets to == num, it will essentially divide by itself which will also not make it a prime number.)
for i in range(num-3):
  if num%(i+2)==0:
    prime=False
    break

if prime == True:
  print(f'{num} is prime')
else:
  print(f'{num} is not prime as it is divisible by {i+2}')

#we can also let the user know the lowest factor of the number other than 1 by writing what i+2 was before the loop was broken.