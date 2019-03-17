#! /usr/bin/env python3.6

import tkinter as tk
import tkinter.ttk as ttk
from ColorList import color_list

def ChangeColor():
    
    color_var = color_choice.get()
    bg_color = color_var
    frame.configure(background = bg_color)
    #color_label.configure(text = bg_color)
    #color_entered.delete(0, 'end') 

bg_color = 'moccasin'

root = tk.Tk()
root.geometry('%sx%s' % (400, 400))
root.title("Ubuntu Color Demo for Tkinter")
root.configure(background = 'slate grey')

frame = tk.LabelFrame(root)
frame.configure(background = bg_color)
frame.pack(fill = 'both', expand = True, side = 'top')

#color_label = tk.Label(frame, text = bg_color)
#color_label.pack(pady = 50, side = 'top')

color = tk.StringVar()
color_choice = ttk.Combobox(root, width = 20, textvariable = color)
color_choice['values'] = color_list
color_choice.pack(side = 'left', padx = 5, pady = 10)
#color_entered = tk.Entry(root, width=20, 
#    textvariable=color, bd=5, relief=tk.RIDGE)
#color_entered.pack(side = 'left')

c_button = tk.Button(root, text = 'Change Color', command = ChangeColor,
    background = '#48483E', foreground = '#CFD0C2')
c_button.pack(side = 'left', pady = 10)
button = tk.Button(root, text = 'Exit', command = root.destroy,
    background = '#48483E', foreground = '#CFD0C2')
button.pack(side = 'right', pady = 10)

root.mainloop()