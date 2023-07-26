a = [1,3,5,6,11,23]
sum = 9
twosum = 0
found = False

for i in range(6):
  for j in range(6):
    twosum = a[i] + a[j]
    if twosum == sum:
      print(a[i],a[j]) 
      found = True
      break
    else:
      j=j+1
      twosum = 0
  i=i+1
  if found == True:
    break