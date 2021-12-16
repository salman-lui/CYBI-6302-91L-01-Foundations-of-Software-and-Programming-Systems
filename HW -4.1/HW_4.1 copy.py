# Homework 4.1
# Angela Garcia
# CYBI-6302-91L
#Develop a Python program with a simple GUI that can read a temperature value in the Celsius scale or in the 
#Fahrenheit scale and can transform that imput temperature to the other temperature scale. Select the input 
#temperature scale with a OptionMenu graphical component and use the graphical component label to show the 
#transformation. If the transformation is not possible use the graphical component messagebox to show a warning.
#Use the transformations Tf = 1.8 * Tc + 32 and Tc = (5/9) * (Tf - 32) 

import tkinter as tk
from tkinter import *
from tkinter import messagebox

class App:

    # Initialize class
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Celsius - Fahrenheit converter")
        self.window.geometry("700x40")

        # Set items in first row

        # User entry
        self.userEntry = tk.Entry(self.window)
        self.userEntry.grid(row = 1, column = 1)

        # Option menu
        self.options = ["Fahrenheit to Celsius", "Celsius to Fahrenheit"]
        # Variable to keep track of the option selected
        self.optionSelected = tk.StringVar(self.window)
        self.optionSelected.set("Fahrenheit to Celsius")
        self.optionMenu = tk.OptionMenu(self.window, self.optionSelected, *self.options)
        self.optionMenu.grid(row = 1, column = 2)

        # Convert button
        tk.Button(self.window, text = "Convert", command = self.convert).grid(row = 1, column = 3)

        # Result label
        self.resultLabel = tk.Label(self.window, textvariable = "")
        self.resultLabel.grid(row = 1, column = 4)


    # Convert Celsius to Fahrenheits
    def convert(self):
        # Determine if Celsius of Fahrenheit was entered in the user entry
        celsius = ""
        fahrenheit = ""
        # If Fahrenheit was entered, calculate Celsius
        if self.optionSelected.get() == "Fahrenheit to Celsius":
            fahrenheit = self.userEntry.get()
            try:
                far = int(fahrenheit)
                cel = (far - 32) / (9/5)
                self.resultLabel.config(text = "is equal to {:.2f} Celsius".format(cel))
            except ValueError as error:
                self.resultLabel.config(text = "")
                messagebox.showwarning("Warning", "Value is not a valid number")
        # If Celsius was entered, calculate Fahrenheit
        elif self.optionSelected.get() == "Celsius to Fahrenheit":
            celsius = self.userEntry.get()
            try:
                cel = int(celsius)
                far = (9/5 * (cel)) + 32
                self.resultLabel.config(text = "is equal to {:.2f} Fahrenheit".format(far))
            except ValueError as error:
                self.resultLabel.config(text = "")
                messagebox.showwarning("Warning", "Value is not a valid number")


app = App()
app.window.mainloop()    # Run app forever