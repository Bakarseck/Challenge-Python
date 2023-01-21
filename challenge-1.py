# The first challenges in python

# Je prends le nombre d'entrée de l'utilisateur
numberOfinput = int(input("Veuillez saisir un entier : "))

# Je déclare une liste vide afin de stocker les nombres là dedans
listOfNumbers = []

print(f"Veuillez entrer {numberOfinput} nombres ") 

# Je prends l'entrée de l'utilisateur
str_number = input()

# Je parcours tous les élements et je les mets dans un tableau et je ne prends pas les espaces
for element in str_number:
    if element != ' ':
        listOfNumbers.append(int(element)) 

# là je trie le tableau pour prendre les deux maximums qui seront en dernière position
# J'utilise la fonction sort() qui est une fonction native en python pour trier le tableau
listOfNumbers.sort()

# le tableau doit contenir le nombre d'éléments en haut !!!
# je mets un contrôle de saisie
if len(listOfNumbers) != numberOfinput :
    print(f"Veuillez entrer {numberOfinput} nombres ")
else :
    lastNumber = listOfNumbers[numberOfinput - 1] # je recupère le dernier nombre
    beforLastNumber = listOfNumbers[numberOfinput - 2] # je recupère l'avant dernier nombre
    product = lastNumber*beforLastNumber # Je calcule le produit
    print(f"Les deux plus grands nombres sont {beforLastNumber} et {lastNumber} et leur produit est {product} ")
