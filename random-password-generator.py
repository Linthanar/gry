import random
import string
smallCaps = string.ascii_lowercase
upperCaps = string.ascii_uppercase
numbers = string.digits
specialChars = string.punctuation
generatedPassword = ''
all = ''

digtsInPassword = 15
uppers = True
lowers = False
num = True
sign = True

if(uppers):
    all +=upperCaps
if(lowers):
    all +=smallCaps
if(num):
    all+=numbers
if(sign):
    all+=specialChars

generatedPassword = random.sample(all, digtsInPassword)

print('PASSWORD ', ''.join(generatedPassword))



