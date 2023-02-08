"""
name: Derek D'Arcy
Description: This program is the gui for a scientific calculator with other features
"""

from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_add():
    return

# define buttons


button_1 = Button(root, text="1", padx=40, pady=20, command=button_add)
button_2 = Button(root, text="2", padx=40, pady=20, command=button_add)
button_3 = Button(root, text="3", padx=40, pady=20, command=button_add)
button_4 = Button(root, text="4", padx=40, pady=20, command=button_add)
button_5 = Button(root, text="5", padx=40, pady=20, command=button_add)
button_6 = Button(root, text="6", padx=40, pady=20, command=button_add)
button_7 = Button(root, text="7", padx=40, pady=20, command=button_add)
button_8 = Button(root, text="8", padx=40, pady=20, command=button_add)
button_9 = Button(root, text="9", padx=40, pady=20, command=button_add)
button_0 = Button(root, text="0", padx=40, pady=20, command=button_add)
button_clear = Button(root, text="Clear", padx=40, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_add)
button_2nd = Button(root, text="2nd", fg='#f00', padx=40, pady=20, command=button_add)
button_plus = Button(root, text="+", padx=40, pady=20, command=button_add)
button_minus = Button(root, text="-", padx=40, pady=20, command=button_add)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_add)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_add)
button_log = Button(root, text="log", padx=40, pady=20, command=button_add)
button_sqrt = Button(root, text="\u221a", padx=40, pady=20, command=button_add)
button_factorial = Button(root, text="!", padx=40, pady=20, command=button_add)

# display buttons

button_clear.grid(row=1, column=0)
button_log.grid(row=1, column=1)
button_sqrt.grid(row=1, column=2)
button_factorial.grid(row=1, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_minus.grid(row=4, column=3)


button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)


button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_2nd.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_plus.grid(row=5, column=2)
button_equal.grid(row=5, column=3)


root.mainloop()
