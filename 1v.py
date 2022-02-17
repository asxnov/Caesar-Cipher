def encrypt(text,s): 
   result = "" 
   for i in range(len(text)): 
      char = text[i] 
      res = int(ord(char))
      if res==32:
          result+=' '
      else:
          if(char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
          else:
                result += chr((ord(char) + s - 97) % 26 + 97)
   return result 

text = "Erbolat" 
s = 3 

print ("Plain Text : " + str(text)) 
print ("Shift pattern : " + str(s))
print ("Cipher: " +encrypt(text,s))


