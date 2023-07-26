alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
substitute = ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","_"]

message = input("Enter message to be encrypted: ")
new = ''

#nested for loop - on the first layer we are looping through each character of the message string. On the second, we are looping through the alphabet and comparing that character of the message string to each letter of the alphabet. When there is a match, we add the chcaracter form the same position in the substitute array into the 'new' empty string.
for j in range(len(message)):
  found=False
  for i in range(len(alphabet)):
    if alphabet[i] == message[j]:
      new += substitute[i]
      found=True
      break
  #if user enters a character that is not in our alphabet array, we append a star to the message in place of that character.
  if found==False:
    new += '*'

print(new)
