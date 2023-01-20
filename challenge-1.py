# The first challenges in python

numberOfinput = int(input("Veuillez saisir un entier : "))
listOfNumbers = []

print(f"Veuillez entrer {numberOfinput} nombres ")

str_number = input()

for i in str_number:
    if i != ' ':
        listOfNumbers.append(int(i))

listOfNumbers.sort()

if len(listOfNumbers) != numberOfinput :
    print(f"Veuillez entrer {numberOfinput} nombres ")
else :
    lastNumber = listOfNumbers[numberOfinput - 1]
    beforLastNumber = listOfNumbers[numberOfinput - 2]
    product = lastNumber*beforLastNumber
    print(f"Les deux plus grands nombres sont {beforLastNumber} et {lastNumber} et leur produit est {product} ")
