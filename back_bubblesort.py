tosort = [36,21,13,1,3,87,20,6,4,17,15]

def bubblesort(arr):
  temp = 0 #temporary storage of number
  j=0
  swap=True
  while swap==True:
    swap=False
    j+=1
    for i in range(len(tosort)-j):
      if tosort[i] > tosort[i+1]:
        swap=True #When all numbers are sorted and none need to be swapped, when iterations through the for loop will stop and swap will still be false. This will force us out of the while loop, avoiding extra iterations.
        temp = tosort[i]
        tosort[i] = tosort[i+1]
        tosort[i+1] = temp

  return tosort

print(bubblesort(tosort))