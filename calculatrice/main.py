# Couleurs
# Noir : #101419
# Bleu : #476C98
# Rouge : #984447

"""
----
789*
456-
123+
0,/=
----

"""
from  tkinter import *

expression = ""

def appuyer(touche):
    if touche == "=":
        calculer()
        return
    
    global expression
    expression += str(touche)
    equation.set(expression)

def calculer():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def effacer():
    global expression
    expression = ""
    equation.set("")

# Create a Graphical User Interface
gui = Tk()

# Background-color
gui.configure(background="#101419")

# Taille de la fenêtre
# gui.geometry("198x385")

# Title of the application
gui.title("Calculatrice")

# Variable to store the current content
equation = StringVar()

# Boite de résultats
resultat = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=3)
resultat.grid(columnspan=4)

# Boutons
boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, "-", "/", "="]
ligne = 1
colonne = 0

for bouton in boutons:
    b = Label(gui, text=str(bouton), bg="#476C98", fg="#FFF", height=4, width=6)

    # make the button clickable
    b.bind("<Button-1>", lambda e, bouton=bouton : appuyer(bouton))


    b.grid(row = ligne, column=colonne)

    colonne += 1
    if colonne == 4:
        colonne = 0
        ligne += 1

erase = Label(gui, text="Effacer", bg="#984447", fg="#FFF", height=4, width=25)
erase.bind("<Button-1>", lambda e : effacer())
erase.grid(columnspan=4)

# Expand The 
gui.mainloop()
