def sumin(x, y):
  for i in range(x+1, y+1):
    print(i)
    if i == x:
      continue
    x += i 
  return x

result = sumin(int(input('start: ')), int(input('end: ')))
print(result)