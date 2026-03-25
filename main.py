#Grafischer Taschenrechner
import tkinter            #tkinter-modul=die Standardbibliothek für GUI-Programmierung in Python


#oop die Rechenmethoden
class calculation_methods:
    def __init__(self, entry_field):            #entry_field als platzhalter für entry
        self.entry = entry_field

    def addition(self):
        self.entry.insert("end", "+")

    def subtraction(self):
        self.entry.insert("end", "-")

    def multiplication(self):
        self.entry.insert("end", "*")

    def division(self):
        self.entry.insert("end", "/")


    #Knöpfe Erstellen und platzieren
    def button_1(self):
        self.entry.insert("end", "1")
    def button_2(self):
        self.entry.insert("end", "2")
    def button_3(self):
        self.entry.insert("end", "3")
    def button_4(self):
        self.entry.insert("end", "4")
    def button_5(self):
        self.entry.insert("end", "5")
    def button_6(self):
        self.entry.insert("end", "6")
    def button_7(self):
        self.entry.insert("end", "7")
    def button_8(self):
        self.entry.insert("end", "8")
    def button_9(self):
        self.entry.insert("end", "9")
    def button_0(self):
        self.entry.insert("end", "0")


    def button_addition(self):
        self.entry.insert("end", "+")
    def button_subtraction(self):
        self.entry.insert("end", "-")
    def button_multiplication(self):
        self.entry.insert("end", "*")
    def button_division(self):
        self.entry.insert("end", "/")
    def clear(self):
        self.entry.delete(0, "end")


    def calculate(self):
        result = eval(self.entry.get())  # eval rechnet den text
        self.entry.delete(0, "end")  # entry = speichern als text ""
        self.entry.insert(0, str(result))


# fenster erstellen/öffnen
root = tkinter.Tk()                 # root= fenster   #Tk() ist eine Funktion aus dem Modul tkinter
root.title("Taschenrechner")

entry = tkinter.Entry(root)         # entry=das gui feld insert=text schreiben
entry.grid()                        # grid() statt pack() beides geht nicht (grid da man da die knöpfe leichter anordnen kan)

cal_methods = calculation_methods(entry)


buttons = []

button1 = tkinter.Button(root, text="1", command=cal_methods.button_1)     #tk = erstellt den knopf
button2 = tkinter.Button(root, text="2", command=cal_methods.button_2)
button3 = tkinter.Button(root, text="3", command=cal_methods.button_3)
button4 = tkinter.Button(root, text="4", command=cal_methods.button_4)
button5 = tkinter.Button(root, text="5", command=cal_methods.button_5)
button6 = tkinter.Button(root, text="6", command=cal_methods.button_6)
button7 = tkinter.Button(root, text="7", command=cal_methods.button_7)
button8 = tkinter.Button(root, text="8", command=cal_methods.button_8)
button9 = tkinter.Button(root, text="9", command=cal_methods.button_9)
button0 = tkinter.Button(root, text="0", command=cal_methods.button_0)

buttonaddition = tkinter.Button(root, text="+", command=cal_methods.button_addition)
buttonsubtraction = tkinter.Button(root, text="-", command=cal_methods.button_subtraction)
buttonmultiplication = tkinter.Button(root, text="*", command=cal_methods.button_multiplication)
buttondivision = tkinter.Button(root, text="/", command=cal_methods.button_division)

button_equals = tkinter.Button(root, text="=", command=cal_methods.calculate)  #Button für Berechnung =
button_clear = tkinter.Button(root, text="C", command=cal_methods.clear)     #löschen nach rechnung


button1.grid(row=3,column=0)            #grid = ordnet in Zeilen und Spalten an
button2.grid(row=3,column=1)            #row= Zeilennummer
button3.grid(row=3,column=2)            #column= spaltennummer
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=1)

buttonaddition.grid(row=1, column=3)
buttonsubtraction.grid(row=2, column=3)
buttonmultiplication.grid(row=3, column=3)
buttondivision.grid(row=4, column=3)
button_equals.grid(row=4, column=2)
button_clear.grid(row=4, column=0)

root.mainloop()