#Password Generator Project
#Ahmed Osama Mahmoud FCAI cairo univ

import random as rd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

passs = letters[0:nr_letters]  + symbols[0:nr_symbols] + numbers[0:nr_numbers];
print(passs)

finalRes=[]
sz=len(passs)
for i in range(sz):
    finalRes.append(passs[i]);
    
res=[]

finalRes.append('+');

for i in range(sz):
    pos=rd.randint(0,len(passs));
    res.append(passs[pos-1]);
    finalRes.append(passs[pos-1]);
    passs.remove(passs[pos-1]);
print(res)

for i in range (len(finalRes)):
    print(finalRes[i], end=''),

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P