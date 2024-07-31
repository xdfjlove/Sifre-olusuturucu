import random 
numbers = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("How long would you like the password to be? ")) 
password = "" 
for _ in range(password_length): 
    password_char = random.choice(numbers) 
    password += password_char
print("Your password:", password)
