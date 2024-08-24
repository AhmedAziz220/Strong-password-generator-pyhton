import string 
import random
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

character_numbers = input("How many characters for the password: ")

while True:
    try:
        character_numbers = int(character_numbers)
        if character_numbers < 6:
            print("you need at least 6 characters")
            character_numbers = input("Please enter the number again: ")
        else:
            break

    except:
        print("Invalid input, please enter numbers only")
        character_numbers = input("Please enter the number again: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character_numbers * (30/100))
part2 = round(character_numbers * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])

print(password)
