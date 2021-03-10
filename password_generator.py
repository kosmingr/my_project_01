#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total = []
for i in range(0, nr_letters):
    x = random.choice(letters)
    total.append(x)
#print(total)

total_1 = []
for i in range(0, nr_numbers):
    x = random.choice(numbers)
    total_1.append(x)
#print(total_1)

total_2 = []
for i in range(0, nr_symbols):
    x = random.choice(symbols)
    total_2.append(x)
#print(total_2)


total_5 = "".join(total) + "".join(total_1) + "".join(total_2)
print(f"Your password is: {total_5}")

total_6 = (''.join(random.sample(total_5,len(total_5))))
print(f"Your randomised password is: {total_6}")