"""
name: Derek D'Arcy
Description: This program is the gui for a scientific calculator with other features
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import math


LARGEFONT = ("Verdana", 24)


class page_container(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (main_page, settings_page, temperature_page, currency_page, second_page):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main_page)
        self.title("Calculator")

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class main_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def button_clear():
            e.delete(0, END)
            button_0.configure(bg='cyan', command=lambda: button_click(0))

        def do_nothing():
            return

        def button_add():
            first_number = e.get()
            global f_num
            global math
            math = "add"
            f_num = int(first_number)
            e.delete(0, END)

        def button_subtract():
            first_number = e.get()
            global f_num
            global math
            math = "subtract"
            f_num = int(first_number)
            e.delete(0, END)

        def button_multiply():
            first_number = e.get()
            global f_num
            global math
            math = "multiply"
            f_num = int(first_number)
            e.delete(0, END)

        def button_divide():
            first_number = e.get()
            global f_num
            global math
            math = "divide"
            f_num = int(first_number)
            e.delete(0, END)
            button_0.configure(bg='red', command=lambda: do_nothing)

        def button_equal():
            second_number = e.get()
            e.delete(0, END)

            if math == "add":
                e.insert(0, f_num + int(second_number))

            elif math == "subtract":
                e.insert(0, f_num - int(second_number))

            elif math == "multiply":
                e.insert(0, f_num * int(second_number))

            elif math == "divide":
                e.insert(0, str(round(f_num / int(second_number), 6)))

        def button_click(num):
            box = e.get()
            e.delete(0, END)
            e.insert(0, str(box) + str(num))

        # define entry box
        e = Entry(self, width=15, borderwidth=5, font=('Arial', 24))
        e.grid(row=0, column=1, columnspan=5, padx=10, pady=10)

        # define buttons

        button_1 = Button(self, text="1", bg='cyan', padx=40, pady=20, command=lambda: button_click(1))
        button_2 = Button(self, text="2", bg='cyan', padx=40, pady=20, command=lambda: button_click(2))
        button_3 = Button(self, text="3", bg='cyan', padx=40, pady=20, command=lambda: button_click(3))
        button_4 = Button(self, text="4", bg='cyan', padx=40, pady=20, command=lambda: button_click(4))
        button_5 = Button(self, text="5", bg='cyan', padx=40, pady=20, command=lambda: button_click(5))
        button_6 = Button(self, text="6", bg='cyan', padx=40, pady=20, command=lambda: button_click(6))
        button_7 = Button(self, text="7", bg='cyan', padx=40, pady=20, command=lambda: button_click(7))
        button_8 = Button(self, text="8", bg='cyan', padx=40, pady=20, command=lambda: button_click(8))
        button_9 = Button(self, text="9", bg='cyan', padx=40, pady=20, command=lambda: button_click(9))
        button_0 = Button(self, text="0", bg='cyan', padx=40, pady=20, command=lambda: button_click(0))

        button_clear = Button(self, text="Clear", padx=40, pady=20, command=button_clear)
        button_equal = Button(self, text="=", padx=40, pady=20, command=button_equal)
        button_2nd = Button(self, text="2nd", fg='#f00', padx=40, pady=20, command=lambda: controller.show_frame(second_page))
        button_plus = Button(self, text="+", padx=40, pady=20, command=button_add)
        button_minus = Button(self, text="-", padx=40, pady=20, command=button_subtract)
        button_multiply = Button(self, text="*", padx=40, pady=20, command=button_multiply)
        button_divide = Button(self, text="/", padx=40, pady=20, command=button_divide)
        button_log = Button(self, text="log", padx=40, pady=20, command=button_add)
        button_sqrt = Button(self, text="\u221a", padx=40, pady=20, command=button_add)
        button_factorial = Button(self, text="!", padx=40, pady=20, command=button_add)

        button_temp_page = Button(self, text="Temperature", padx=40, pady=20,  command=lambda: controller.show_frame(temperature_page))
        button_settings_page = Button(self, text="Settings", padx=40, pady=20, command=lambda: controller.show_frame(settings_page))
        button_currency_page = Button(self, text="Currency Exchange", padx=40, pady=20,  command=lambda: controller.show_frame(currency_page))

        # display buttons

        button_clear.grid(row=2, column=0)
        button_log.grid(row=2, column=1)
        button_sqrt.grid(row=2, column=2)
        button_factorial.grid(row=2, column=3)

        button_1.grid(row=5, column=0)
        button_2.grid(row=5, column=1)
        button_3.grid(row=5, column=2)
        button_minus.grid(row=5, column=3)

        button_4.grid(row=4, column=0)
        button_5.grid(row=4, column=1)
        button_6.grid(row=4, column=2)
        button_multiply.grid(row=4, column=3)

        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)
        button_divide.grid(row=3, column=3)

        button_2nd.grid(row=6, column=0)
        button_0.grid(row=6, column=1)
        button_plus.grid(row=6, column=2)
        button_equal.grid(row=6, column=3)

        button_temp_page.grid(row=1, column=0, columnspan=2)
        button_currency_page.grid(row=1, column=2, columnspan=2)

        button_settings_page.grid(row=0, column=0)


class second_page(tk.Frame):
    # page that handles 2nd functions
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # define entry box
        e = Entry(self, width=15, borderwidth=5, font=('Arial', 24))
        e.grid(row=0, column=1, columnspan=5, padx=10, pady=10)

        # define num buttons, make them do nothing
        button_1 = Button(self, text="1", padx=40, pady=20)
        button_2 = Button(self, text="2", padx=40, pady=20)
        button_3 = Button(self, text="3", padx=40, pady=20)
        button_4 = Button(self, text="4", padx=40, pady=20)
        button_5 = Button(self, text="5", padx=40, pady=20)
        button_6 = Button(self, text="6", padx=40, pady=20)
        button_7 = Button(self, text="7", padx=40, pady=20)
        button_8 = Button(self, text="8", padx=40, pady=20)
        button_9 = Button(self, text="9", padx=40, pady=20)
        button_0 = Button(self, text="0", padx=40, pady=20)

        # define other buttons
        button_clear = Button(self, text="Clear", padx=40, pady=20)
        button_equal = Button(self, text="=", padx=40, pady=20)
        button_2nd = Button(self, text="2nd", bg='#f00', fg='#fff', padx=40, pady=20, command=lambda: controller.show_frame(main_page))
        button_plus = Button(self, text="+", padx=40, pady=20)
        button_minus = Button(self, text="-", padx=40, pady=20)
        button_multiply = Button(self, text="*", padx=40, pady=20)
        button_divide = Button(self, text="/", padx=40, pady=20)
        button_log = Button(self, text="log", padx=40, pady=20)
        button_sqrt = Button(self, text="\u221a", padx=40, pady=20)
        button_factorial = Button(self, text="!", padx=40, pady=20)

        button_temp_page = Button(self, text="Temperature", padx=40, pady=20,  command=lambda: controller.show_frame(temperature_page))
        button_settings_page = Button(self, text="Settings", padx=40, pady=20, command=lambda: controller.show_frame(settings_page))
        button_currency_page = Button(self, text="Currency Exchange", padx=40, pady=20,  command=lambda: controller.show_frame(currency_page))

        # display buttons

        button_clear.grid(row=2, column=0)
        button_log.grid(row=2, column=1)
        button_sqrt.grid(row=2, column=2)
        button_factorial.grid(row=2, column=3)

        button_1.grid(row=5, column=0)
        button_2.grid(row=5, column=1)
        button_3.grid(row=5, column=2)
        button_minus.grid(row=5, column=3)

        button_4.grid(row=4, column=0)
        button_5.grid(row=4, column=1)
        button_6.grid(row=4, column=2)
        button_multiply.grid(row=4, column=3)

        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)
        button_divide.grid(row=3, column=3)

        button_2nd.grid(row=6, column=0)
        button_0.grid(row=6, column=1)
        button_plus.grid(row=6, column=2)
        button_equal.grid(row=6, column=3)

        button_temp_page.grid(row=1, column=0, columnspan=2)
        button_currency_page.grid(row=1, column=2, columnspan=2)

        button_settings_page.grid(row=0, column=0)


class settings_page(tk.Frame):
    # page that handles settings
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Settings", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        temperature_button = ttk.Button(self, text="Temperature Conversion",
                                        command=lambda: controller.show_frame(temperature_page))

        # putting the button in its place by
        # using grid
        temperature_button.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        currency_button = ttk.Button(self, text="Currency Exchange",
                                     command=lambda: controller.show_frame(currency_page))

        # putting the button in its place by
        # using grid
        currency_button.grid(row=1, column=2, padx=10, pady=10)

        # main page button and add to grid
        main_page_button = ttk.Button(self, text="Main Calculator",
                                      command=lambda: controller.show_frame(main_page))

        main_page_button.grid(row=1, column=3, padx=10, pady=10)

        degrees_button = ttk.Button(self, text="Degrees")
        radians_button = ttk.Button(self, text="Radians")

        degrees_button.grid(row=2, column=0, columnspan=2)
        radians_button.grid(row=2, column=2, columnspan=2)


class temperature_page(tk.Frame):
    # page that handles temperature conversions
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Temperature Conversion", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        settings_button = ttk.Button(self, text="Settings",
                                     command=lambda: controller.show_frame(settings_page))

        # putting the button in its place by
        # using grid
        settings_button.grid(row=1, column=0, padx=10, pady=10)

        # button to show frame 2 with text layout2
        currency_button = ttk.Button(self, text="Currency Exchange",
                                     command=lambda: controller.show_frame(currency_page))

        # putting the button in its place by
        # using grid
        currency_button.grid(row=1, column=1, padx=10, pady=10)

        # main page button and add to grid
        main_page_button = ttk.Button(self, text="Main Calculator",
                                      command=lambda: controller.show_frame(main_page))

        main_page_button.grid(row=1, column=2, padx=10, pady=10)

        # create dropdowns for choosing temp conversions
        options = [
            "Farenheit",
            "Celsius",
            "Kelvin",
        ]

        user_input_box = Entry(self, width=15, borderwidth=5, font=('Arial', 10))
        user_input_box.grid(row=2, column=0)

        first_clicked = StringVar()
        first_clicked.set("Temp")
        first_drop_menu = OptionMenu(self, first_clicked, *options)
        first_drop_menu.grid(row=2, column=1)

        display_box = Entry(self, width=15, borderwidth=5, font=('Arial', 10), state=tk.DISABLED)
        display_box.grid(row=2, column=2)

        second_clicked = StringVar()
        second_clicked.set("Temp")
        displayed_drop_menu = OptionMenu(self, second_clicked, *options)
        displayed_drop_menu.grid(row=2, column=3)

        calculate_button = ttk.Button(self, text="Calculate")
        calculate_button.grid(row=3, column=0, columnspan=4)


class currency_page(tk.Frame):
    # page that handles currency conversions
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Currency Exchange", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        settings_button = ttk.Button(self, text="Settings",
                                     command=lambda: controller.show_frame(settings_page))

        # putting the button in its place by
        # using grid
        settings_button.grid(row=1, column=0, padx=10, pady=10)

        # button to show frame 2 with text layout2
        temperature_button = ttk.Button(self, text="Temperature Conversion",
                                        command=lambda: controller.show_frame(temperature_page))

        # putting the button in its place by
        # using grid
        temperature_button.grid(row=1, column=1, padx=10, pady=10)

        # main page button and add to grid
        main_page_button = ttk.Button(self, text="Main Calculator",
                                      command=lambda: controller.show_frame(main_page))

        main_page_button.grid(row=1, column=2, padx=10, pady=10)

        # create dropdowns for choosing currency conversions
        options = [
            "US Dollar",
            "Pound",
            "Yen",
            "Cad",
            "BTC"
        ]

        user_input_box = Entry(self, width=15, borderwidth=5, font=('Arial', 10))
        user_input_box.grid(row=2, column=0)

        first_clicked = StringVar()
        first_clicked.set("Currency")
        first_drop_menu = OptionMenu(self, first_clicked, *options)
        first_drop_menu.grid(row=2, column=1)

        display_box = Entry(self, width=15, borderwidth=5, font=('Arial', 10), state=tk.DISABLED)
        display_box.grid(row=2, column=2, padx=0)

        second_clicked = StringVar()
        second_clicked.set("Currency")
        displayed_drop_menu = OptionMenu(self, second_clicked, *options)
        displayed_drop_menu.grid(row=2, column=3, padx=0)

        calculate_button = ttk.Button(self, text="Calculate")
        calculate_button.grid(row=3, column=0, columnspan=4)


# driver code
root = page_container()
root.geometry("440x460")
root.mainloop()


# notes:
#
#
#
#
#
#
#
#
