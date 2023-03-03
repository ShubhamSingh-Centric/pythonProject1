#generate random password

import random

l = []
for i in range(8):
    l.append(str(random.randint(1,9)))


password = "".join(l)

print(password)


import string
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
random.choice(string.ascii_letters + "!@#$%^&*1234567890")

l2 = []
for i in range(20):
    l2.append(random.choice(string.ascii_letters + "!@#$%^&*1234567890"))


password = "".join(l2)

print(password)


# -------------------------------------------------#
# solutions
#1
# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print(p)

#2

import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))