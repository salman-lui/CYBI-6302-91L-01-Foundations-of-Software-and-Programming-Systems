# Md Salman Rahman
# HW 4.1

# Develop a Python program with a simple GUI that can read a temperature value in the Celsius scale or in 
# the Fahrenheit scale and can transform that imput temperature to the other temperature scale. 
# Select the input temperature scale with a OptionMenu graphical component and use the graphical component label to show the transformation. 
# If the transformation is not possible use the graphical component messagebox to show a warning.

import tkinter as tk
from tkinter import Variable, messagebox
from tkinter import font
# This function is called whenever the button is pressed
def convert_c2f():

    # Convert Celsius to Fahrenheit and update label (through textvariable)
    try:
        temp_c = entry_celsius.get()
        temp_f=1.8*float(temp_c)+32
        label_equal.config(text = "is equal to " + f'{temp_f:.2f} F')      
    except:
        messagebox.showinfo("Warning","Input error!")

def convert_f2c():

    # Convert Fahrenheit to Celsius and update label (through textvariable)
    try:
        temp_c = entry_celsius.get()
        temp_c=(1/1.8)*(float(temp_c)-32)
        label_equal.config(text = "is equal to " + f'{temp_c:.2f} C')       
    except:
        messagebox.showinfo("Warning","Input error!")

def convert():
    if variable.get()=="Celsius to Fahrenheit":
        convert_c2f()
    if variable.get()=="Fahrenheit to Celsius":
        convert_f2c()
    

# Create the main window
app = tk.Tk()
app.title("  Temperature Converter  ")
app.geometry('530x50')
app.resizable(False, False)


# Create and add the main container
frame = tk.Frame(app)
frame.pack()

# Creating Widges
entry_celsius = tk.Entry(frame,width=7)
entry_celsius.insert(0,"0.0")

OptionList =[
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius"
]
variable =tk.StringVar(frame)
variable.set(OptionList[0])
opt = tk.OptionMenu(frame,variable, *OptionList)
opt.config(width=20,font = ('Helvetica',11))

button_convert = tk.Button(frame, text="Convert", command=convert, font = ('Helvetica',11))

label_equal = tk.Label(frame, text="'is equal to 32.00 F", font = ('Helvetica',11))

# Layout widgets in a matrix
entry_celsius.grid(row=1, column=0, padx=5, pady=5)
opt.grid(row=1, column=1, padx=1, pady=5)
button_convert.grid(row=1, column=2, padx=5, pady=5)
label_equal.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

#Run app
app.mainloop()

