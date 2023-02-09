"""
name: Derek D'Arcy
Description: This program is the gui for a scientific calculator with other features
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk


LARGEFONT = ("Verdana", 35)


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
        for F in (main_page, settings_page, temperature_page, currency_page):

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

        def button_add():
            return

        # define entry box
        e = Entry(self, width=15, borderwidth=5, font=('Arial', 24))
        e.grid(row=0, column=1, columnspan=5, padx=10, pady=10)

        # define buttons

        button_1 = Button(self, text="1", padx=40, pady=20, command=button_add)
        button_2 = Button(self, text="2", padx=40, pady=20, command=button_add)
        button_3 = Button(self, text="3", padx=40, pady=20, command=button_add)
        button_4 = Button(self, text="4", padx=40, pady=20, command=button_add)
        button_5 = Button(self, text="5", padx=40, pady=20, command=button_add)
        button_6 = Button(self, text="6", padx=40, pady=20, command=button_add)
        button_7 = Button(self, text="7", padx=40, pady=20, command=button_add)
        button_8 = Button(self, text="8", padx=40, pady=20, command=button_add)
        button_9 = Button(self, text="9", padx=40, pady=20, command=button_add)
        button_0 = Button(self, text="0", padx=40, pady=20, command=button_add)
        button_clear = Button(self, text="Clear", padx=40, pady=20, command=button_add)
        button_equal = Button(self, text="=", padx=40, pady=20, command=button_add)
        button_2nd = Button(self, text="2nd", fg='#f00', padx=40, pady=20, command=button_add)
        button_plus = Button(self, text="+", padx=40, pady=20, command=button_add)
        button_minus = Button(self, text="-", padx=40, pady=20, command=button_add)
        button_multiply = Button(self, text="*", padx=40, pady=20, command=button_add)
        button_divide = Button(self, text="/", padx=40, pady=20, command=button_add)
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


class settings_page(tk.Frame):
    # page that handles settings
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Settings")
        label.grid(row=0, column=4, padx=10, pady=10)

        # label of frame Layout 2
        label = ttk.Label(self, text="Settings", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

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
        currency_button.grid(row=2, column=1, padx=10, pady=10)

        # main page button and add to grid
        main_page_button = ttk.Button(self, text="Main Calculator",
                                      command=lambda: controller.show_frame(main_page))

        main_page_button.grid(row=3, column=1, padx=10, pady=10)


class temperature_page(tk.Frame):
    # page that handles temperature conversions
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Temperature Conversion")
        label.grid(row=0, column=4, padx=10, pady=10)

        # label of frame Layout temp page
        label = ttk.Label(self, text="Temperature Page", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        settings_button = ttk.Button(self, text="Settings",
                                     command=lambda: controller.show_frame(settings_page))

        # putting the button in its place by
        # using grid
        settings_button.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        currency_button = ttk.Button(self, text="Currency Exchange",
                                     command=lambda: controller.show_frame(currency_page))

        # putting the button in its place by
        # using grid
        currency_button.grid(row=2, column=1, padx=10, pady=10)

        # main page button and add to grid
        main_page_button = ttk.Button(self, text="Main Calculator",
                                      command=lambda: controller.show_frame(main_page))

        main_page_button.grid(row=3, column=1, padx=10, pady=10)


class currency_page(tk.Frame):
    # page that handles currency conversions
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Currency Conversion")
        label.grid(row=0, column=4, padx=10, pady=10)

        # label of frame Layout currency page
        label = ttk.Label(self, text="Currency Conversion", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        settings_button = ttk.Button(self, text="Settings",
                                     command=lambda: controller.show_frame(settings_page))

        # putting the button in its place by
        # using grid
        settings_button.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        temperature_button = ttk.Button(self, text="Temperature Conversion",
                                        command=lambda: controller.show_frame(temperature_page))

        # putting the button in its place by
        # using grid
        temperature_button.grid(row=2, column=1, padx=10, pady=10)

        # main page button and add to grid
        main_page_button = ttk.Button(self, text="Main Calculator",
                                      command=lambda: controller.show_frame(main_page))

        main_page_button.grid(row=3, column=1, padx=10, pady=10)


# driver code
root = page_container()
root.mainloop()
