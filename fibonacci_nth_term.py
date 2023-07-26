n=0
while n < 1:
  n = int(input('Which term of the fibonacci sequence do you wish to find?  '))
  

temp=0
nums = [0,1]
for i in range(n):
  temp = nums[0]+nums[1]
  nums[0] = nums[1]
  nums[1] = temp

print(nums[0])

#to find the desired number in the sequence, you plug in the nth term into the range(). Similar to the bubble sort number sorting technique, we create a temporary number storage that we can put the sum of the two previous numbers in. Next we make the 1st of the two array numbers = the 2nd and then we put the temporary number into the 2nd slot.
#this process is then repeated n number of times.