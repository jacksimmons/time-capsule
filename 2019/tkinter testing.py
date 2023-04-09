# Initial commit timestamp: Nov 11 2019

import tkinter as tk
from tkinter import scrolledtext
import turtle

def stuff():
    eq = equation_input.get()
    if len(eq) == 10: #len('y = mx + c')
        if eq[:4] == 'y = ':
            if eq[4].isdigit() == True:
                print(eq)
            else:
                print("Invalid equation y = (m)x + c")
        else:
            print("Invalid equation (y = )mx + c")
    else:
        print("Invalid equation (y = mx + c)")

window = tk.Tk()
window.title("HI")
window.geometry('640x480')

#-----

eq_xpos = 60
eq_ypos = 60

equation_label = tk.Label(text="Enter an equation (y = mx + c):")
equation_label.place(x=eq_xpos,y=eq_ypos)

equation_input = tk.Entry(text=0)
equation_input.place(x=eq_xpos+24,y=eq_ypos+2,w=100,h=18)

output_label = tk.Label(text=equation_input["text"])
output_label.place(x=eq_xpos,y=eq_ypos+20)

button = tk.Button(text='Start', command=stuff)
button.place(x=23,y=55)

#-----

window.mainloop()
