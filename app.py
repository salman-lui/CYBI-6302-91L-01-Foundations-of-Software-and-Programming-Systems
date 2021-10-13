#Author: Md Salman Rahman
'''
Course: CYBI 6302-91L/01 Foundations of Software and Programming Systems
Course Instructor: Dr. Jose Poveda
Homework: Develop a Python program that reads from the keyboard a temperature value in the Celsius scale 
and writes that temperature value on the console in the Fahrenheit scale. Use the following transformation Tf= (9*Tc/5) + 32 
'''
# take input of temperature value in the celsius scale 
print(" Please input the temperature value in the celsius scale\n")
Tc= float(input())

# converting the celsisu temp to fahrenheit scale 
Tf = (9*Tc/5) + 32
# defining only one digit after the decimal point 
Tf1=format(Tf,".1f")
print(f'The converted farenhit temperature is {Tf1}')

