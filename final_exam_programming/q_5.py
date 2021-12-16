# Md Salman Rahman

import tkinter as tk
from tkinter import Variable, messagebox
from tkinter import font
# This function is called whenever the button is pressed
def convert_us_to_mx():

    # Convert us dollar to mexican dollar and update label (through textvariable)
    try:
        dis_us = entry_us.get()
        dis_mx= 18.5*float(dis_us)
        label_equal.config(text = "is equal to " + f'{dis_mx:.2f} MX$')      
    except:
        messagebox.showinfo("Warning","Input error!")

def convert_mx_to_us():

    # Convert mile to km and update label (through textvariable)
    try:
        dis_us = entry_us.get()
        dis_us= (1/18.5)*float(dis_us)
        label_equal.config(text = "is equal to " + f'{dis_us:.2f} USA$')       
    except:
        messagebox.showinfo("Warning","Input error!")

def convert():
    if variable.get()=="USA$ to MX$":
        convert_us_to_mx()
    if variable.get()=="MX$ to US$":
        convert_mx_to_us()
    

# Create the main window
app = tk.Tk()
app.title("  Currency Converter  ")
app.geometry('530x50')
app.resizable(False, False)


# Create and add the main container
frame = tk.Frame(app)
frame.pack()

# Creating Widges
entry_us = tk.Entry(frame,width=7)
entry_us.insert(0,"0.0")

OptionList =[
    "USA$ to MX$",
    "MX$ to USA$"
]
variable =tk.StringVar(frame)
variable.set(OptionList[0])
opt = tk.OptionMenu(frame,variable, *OptionList)
opt.config(width=20,font = ('Helvetica',11))

button_convert = tk.Button(frame, text="Convert", command=convert, font = ('Helvetica',11))

label_equal = tk.Label(frame, text="'is equal to 0 MX$", font = ('Helvetica',11))

# Layout widgets in a matrix
entry_us.grid(row=1, column=0, padx=5, pady=5)
opt.grid(row=1, column=1, padx=1, pady=5)
button_convert.grid(row=1, column=2, padx=5, pady=5)
label_equal.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

#Run app
app.mainloop()

