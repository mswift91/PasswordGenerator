import string
import random
chars = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(random.randint(7,11)):
  password = password + (chars[random.randint(0,(len(chars)-1))])
print (password)
