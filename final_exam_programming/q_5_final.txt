# Author: Md Salman Rahman


import tkinter as tk
from tkinter import Variable, messagebox
from tkinter import font
# This function is called whenever the button is pressed
def convert_us2mx():

    # Convert US$ to MX$ and update label (through textvariable)
    try:
        c_usd = entry_usd.get()
        c_mxd=18.5*float(c_usd)
        label_equal.config(text = "is equal to " + f'{c_mxd:.2f} MX$')      
    except:
        messagebox.showinfo("Warning","Input error!")

def convert_mx2us():

    # Convert MX$ to US$ and update label (through textvariable)
    try:
        c_usd = entry_usd.get()
        c_usd=(1/18.5)* float(c_usd)
        label_equal.config(text = "is equal to " + f'{c_usd:.2f} US$')       
    except:
        messagebox.showinfo("Warning","Input error!")

def convert():
    if variable.get()=="USA$ to MX$":
        convert_us2mx()
    if variable.get()=="MX$ to USA$":
        convert_mx2us()
    

# Create the main window
app = tk.Tk()
app.title("  Currency Converter  ")
app.geometry('530x50')
app.resizable(False, False)


# Create and add the main container
frame = tk.Frame(app)
frame.pack()

# Creating Widges
entry_usd = tk.Entry(frame,width=7)
entry_usd.insert(0,"0.0")

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
entry_usd.grid(row=1, column=0, padx=5, pady=5)
opt.grid(row=1, column=1, padx=1, pady=5)
button_convert.grid(row=1, column=2, padx=5, pady=5)
label_equal.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

#Run app
app.mainloop()

