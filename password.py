import random
import hashlib
def sha256_hash(text):
  sha256 = hashlib.sha256()
  sha256.update(text.encode())
  return sha256.hexdigest()

def random_password():
    indexa = random.randint(0, 25)
    indexb = random.randint(0, 9)
    indexc = random.randint(0, 5)
    a = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = "0123456789"
    c = "!#%@$&"
    
    firstpart = random.choice(uppercase)  + random.choice(a + b + c) + random.choice(a + b + c)
    secondpart= random.choice(a + b + c)  + random.choice(a + b + c)
    thirdpart= random.choice(a + b + c)  + random.choice(a + b + c) + random.choice(a + b + c)
    return(firstpart+secondpart+thirdpart)

print(random_password())
  #  decrypted = firstpart + secondpart + thirdpart 
 #   return decrypted


#encrypted_text = sha256_hash(random_password())
#num = int(len(encrypted_text)/4)

#print (encrypted_text[0: num])
