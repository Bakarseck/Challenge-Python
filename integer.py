number = int(input("Give me a number between 1 and 20 : \n"))

while number <= 1 or number >= 20:
    number = int(input("Give me a valid number between 1 and 20 : \n"))

for i in range(number):
    print(i**2)
