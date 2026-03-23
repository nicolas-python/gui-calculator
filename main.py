#Grafischer Taschenrechner

import tkinter            #tkinter-modul=die Standardbibliothek für GUI-Programmierung in Python

#fenster erstellen/öffnen
root = tkinter.Tk()                      #root= fenster   #Tk() ist eine Funktion aus dem Modul tkinter
root.title("Taschenrechner")

entry = tkinter.Entry(root)             #entry=das gui feld insert=text schreiben
entry.pack()

#Knöpfe Erstellen und platzieren
def button_1():
    entry.insert("end", "1")
def button_2():
    entry.insert("end", "2")
def button_3():
    entry.insert("end", "3")
def button_4():
    entry.insert("end", "4")
def button_5():
    entry.insert("end", "5")
def button_6():
    entry.insert("end", "6")
def button_7():
    entry.insert("end", "7")
def button_8():
    entry.insert("end", "8")
def button_9():
    entry.insert("end", "9")
def button_0():
    entry.insert("end", "0")

buttons = []

button1 = tkinter.Button(root, text="1", command=button_1)     #tk = erstellt den knopf
button2 = tkinter.Button(root, text="2", command=button_2)
button3 = tkinter.Button(root, text="3", command=button_3)
button4 = tkinter.Button(root, text="4", command=button_4)
button5 = tkinter.Button(root, text="5", command=button_5)
button6 = tkinter.Button(root, text="6", command=button_6)
button7 = tkinter.Button(root, text="7", command=button_7)
button8 = tkinter.Button(root, text="8", command=button_8)
button9 = tkinter.Button(root, text="9", command=button_9)
button0 = tkinter.Button(root, text="0", command=button_0)

buttons.append(button1)
buttons.append(button2)
buttons.append(button3)
buttons.append(button4)
buttons.append(button5)
buttons.append(button6)
buttons.append(button7)
buttons.append(button8)
buttons.append(button9)
buttons.append(button0)

#anzeigen der knöpfe
for b in buttons:
    b.pack()                        #pack zeigt den Knopf im fenster an und platziert ihn/pack nur für einzelne Widgets

#def calculate():

#def calculation_methods():

#def clear():


root.mainloop()