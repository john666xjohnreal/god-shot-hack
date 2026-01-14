from random import *
user_password = input("Enter Your Password: ")
crack =
password= ['a', 'b', 'c', 'd', 'e', 'f', 'g',
'1', 'm', 'n', 'o', 'p',
'w', 'x', 'y', 'z',]
while (crack != user_password):
crack =
for i in range(len(user_password)):
crack_letter = password[randint(0, 25
crack + crack_letter
print(crack)
print("Your Password Is:", crack)
