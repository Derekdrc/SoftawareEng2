"""
name: Derek D'Arcy
Description: This program is the gui for a scientific calculator with other features
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import math
import os
from currency_converter import CurrencyConverter

LARGEFONT = ("Verdana", 24)


class Controller:
    def __init__(self):
        self.current_entry_num = 0
        self.degrees = True
        self.absolute_path = os.path.dirname(__file__)
        self.second = False

    def checkDegrees(self):
        if self.degrees:
            return True
        else:
            return False


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
        for F, geometry in zip((main_page, settings_page, temperature_page, currency_page), ('450x465', '410x200', '450x200', '500x200')):
            page_name = F.__name__
            frame = F(parent=container, controller=self)

            self.frames[page_name] = (frame, geometry)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("main_page")
        self.title("Calculator")

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame, geometry = self.frames[cont]
        self.update_idletasks()
        self.geometry(geometry)
        frame.tkraise()


class main_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller()
        self.config(bg="blue")

        def button_clear_click():
            e.delete(0, END)
            if not self.control.second:
                button_0.configure(bg='cyan', command=lambda: button_click(0))

        def do_nothing():
            ...

        def button_add():
            first_number = e.get()
            global f_num
            global Math
            Math = "add"
            f_num = float(first_number)
            e.delete(0, END)

        def button_subtract():
            first_number = e.get()
            global f_num
            global Math
            Math = "subtract"
            f_num = float(first_number)
            e.delete(0, END)

        def button_multiply():
            first_number = e.get()
            global f_num
            global Math
            Math = "multiply"
            f_num = float(first_number)
            e.delete(0, END)

        def button_divide():
            first_number = e.get()
            global f_num
            global Math
            Math = "divide"
            f_num = float(first_number)
            e.delete(0, END)
            button_0.configure(bg='red', command=lambda: do_nothing)

        def button_sqrt():
            first_number = e.get()
            global f_num
            f_num = float(first_number)
            e.delete(0, END)
            ans = round(math.sqrt(f_num), 3)
            e.insert(0, str(ans))

        def button_log():
            first_number = e.get()
            global f_num
            global Math
            Math = "log"
            f_num = float(first_number)
            e.delete(0, END)

        def button_equal():
            second_number = e.get()
            e.delete(0, END)

            if Math == "add":
                e.insert(0, f_num + float(second_number))

            elif Math == "subtract":
                e.insert(0, f_num - float(second_number))

            elif Math == "multiply":
                e.insert(0, f_num * float(second_number))

            elif Math == "divide":
                if (second_number == '0' or second_number == ''):
                    e.insert(0, "ERROR: Div by 0",)
                else:
                    e.insert(0, str(round(f_num / float(second_number), 6)))
            elif Math == "log":
                ans = round(math.log(f_num, float(second_number)), 3)
                e.insert(0, str(ans))

        def button_click(num):
            if (num in (1, 2, 3, 4, 5, 6, 7, 8, 9)):
                button_0.configure(bg='cyan', command=lambda: button_click(0))
            box = e.get()
            e.delete(0, END)
            e.insert(0, str(box) + str(num))

        def button_decimal():
            box = e.get()
            e.delete(0, END)
            e.insert(0, str(box) + '.')

        def button_sin():
            box = e.get()
            if deg_rad == False:
                e.delete(0, END)
                e.insert(0, str(round(math.sin(float(box)), 3)))
            else:
                e.delete(0, END)
                e.insert(0, str(round(math.sin(math.radians(float(box))), 3)))

        def button_cos():
            box = e.get()
            if deg_rad == False:
                e.delete(0, END)
                e.insert(0, str(round(math.cos(float(box)), 3)))
            else:
                e.delete(0, END)
                e.insert(0, str(round(math.cos(math.radians(float(box))), 3)))

        def button_tan():
            box = e.get()
            if deg_rad == False:
                e.delete(0, END)
                e.insert(0, str(round(math.tan(float(box)), 3)))
            else:
                e.delete(0, END)
                e.insert(0, str(round(math.tan(math.radians(float(box))), 3)))

        def button_factorial():
            box = e.get()
            try:
                if float(box) >= 0:
                    num = int(box)
                    e.delete(0, END)
                    e.insert(0, str(math.factorial(num)))
                else:
                    e.delete(0, END)
                    e.insert(0, "ERROR")
            except:
                e.delete(0, END)
                e.insert(0, "ERROR")

        # handles pressing the second button to toggle "pages"

        def second_button_click():
            if not self.control.second:
                self.control.second = True
                button_0.config(bg='gray', command=lambda: do_nothing)
                button_1.config(bg='gray', command=lambda: do_nothing)
                button_2.config(bg='gray', command=lambda: do_nothing)
                button_3.config(bg='gray', command=lambda: do_nothing)
                button_4.config(bg='gray', command=lambda: do_nothing)
                button_5.config(bg='gray', command=lambda: do_nothing)
                button_6.config(bg='gray', command=lambda: do_nothing)
                button_7.config(bg='gray', command=lambda: do_nothing)
                button_8.config(bg='gray', command=lambda: do_nothing)
                button_9.config(bg='gray', command=lambda: do_nothing)
                button_0.config(bg='gray', command=lambda: do_nothing)
                button_plus.config(bg='gray', command=lambda: do_nothing)
                button_minus.config(bg='gray', command=lambda: do_nothing)
                button_decimal_point.config(bg='gray', command=lambda: do_nothing)
                button_equal_sign.config(bg='gray', command=lambda: do_nothing)
                button_log_sin.config(bg='red', text="Sin", command=lambda: button_sin())
                button_sqrt_cos.config(bg='red', text="Cos", command=lambda: button_cos())
                button_divide_tan.config(bg='red', text="Tan", command=lambda: button_tan())
                button_multiply_factorial.config(bg='red', text="!", command=lambda: button_factorial())
                button_2nd.config(bg='red', fg='black')
            else:
                self.control.second = False
                button_0.config(bg='cyan', command=lambda: button_click(0))
                button_1.config(bg='cyan', command=lambda: button_click(1))
                button_2.config(bg='cyan', command=lambda: button_click(2))
                button_3.config(bg='cyan', command=lambda: button_click(3))
                button_4.config(bg='cyan', command=lambda: button_click(4))
                button_5.config(bg='cyan', command=lambda: button_click(5))
                button_6.config(bg='cyan', command=lambda: button_click(6))
                button_7.config(bg='cyan', command=lambda: button_click(7))
                button_8.config(bg='cyan', command=lambda: button_click(8))
                button_9.config(bg='cyan', command=lambda: button_click(9))
                button_plus.config(bg='plum2', command=lambda: button_add)
                button_minus.config(bg='plum2', command=lambda: button_subtract)
                button_decimal_point.config(bg='plum2', command=lambda: button_decimal)
                button_equal_sign.config(bg='plum2', command=lambda: button_equal)
                button_log_sin.config(bg='plum2', text="log", command=lambda: button_log())
                button_sqrt_cos.config(bg='plum2', text="\u221a", command=lambda: button_sqrt())
                button_divide_tan.config(bg='plum2', text="/", command=lambda: button_divide())
                button_multiply_factorial.config(bg='plum2', text="*", command=lambda: button_multiply())
                button_2nd.config(bg='green', fg='red')

        # images
        settings_img_path = os.path.join(self.control.absolute_path, 'images/settings.png')
        settings_photo = PhotoImage(file=settings_img_path)
        settings_photo_sub = settings_photo.subsample(3, 3)

        e = Entry(self, width=15, borderwidth=5, bg="peachpuff", font=('Arial', 24))
        e.grid(row=0, column=1, columnspan=5, padx=10, pady=10)

        # define buttons

        button_1 = Button(self, text="1", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(1))
        button_2 = Button(self, text="2", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(2))
        button_3 = Button(self, text="3", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(3))
        button_4 = Button(self, text="4", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(4))
        button_5 = Button(self, text="5", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(5))
        button_6 = Button(self, text="6", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(6))
        button_7 = Button(self, text="7", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(7))
        button_8 = Button(self, text="8", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(8))
        button_9 = Button(self, text="9", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(9))
        button_0 = Button(self, text="0", bg='cyan', padx=40, pady=20, width=3, command=lambda: button_click(0))

        button_decimal_point = Button(self, text=".", padx=40, pady=20, width=3, bg="plum2", command=button_decimal)
        button_clear = Button(self, text="Clear", padx=40, pady=20, fg="magenta", bg="black", command=button_clear_click)
        button_equal_sign = Button(self, text="=", padx=40, pady=20, width=3, bg="plum2", command=button_equal)
        button_2nd = Button(self, text="2nd", font=" arial 12 bold", fg='red', bg="green", padx=40, pady=17, command=second_button_click)
        button_plus = Button(self, text="+", padx=40, pady=20, width=3, bg="plum2", command=button_add)
        button_minus = Button(self, text="-", padx=40, pady=20, width=3, bg="plum2", command=button_subtract)
        button_multiply_factorial = Button(self, text="*", padx=40, width=3, pady=20, bg="plum2", command=button_multiply)
        button_divide_tan = Button(self, text="/", padx=40, pady=20, width=3, bg="plum2", command=button_divide)
        button_log_sin = Button(self, text="log", padx=40, pady=20, bg="plum2", command=button_log)
        button_sqrt_cos = Button(self, text="\u221a", padx=40, pady=20, width=3, bg="plum2", command=button_sqrt)

        button_temp_page = Button(self, text="Temperature", padx=40, pady=20, bg="firebrick4", fg="turquoise1", command=lambda: controller.show_frame("temperature_page"))
        button_settings_page = Button(self, image=settings_photo_sub, padx=40, pady=20, bg='white', command=lambda: controller.show_frame("settings_page"))
        button_settings_page.image = settings_photo_sub  # keep a reference or smth so that button actually show img??? no clue why but this line is necessary
        button_currency_page = Button(self, text="Currency Exchange", padx=40, pady=20, bg="darkgreen", fg="white", command=lambda: controller.show_frame("currency_page"))

        # display buttons

        button_clear.grid(row=2, column=0)
        button_log_sin.grid(row=2, column=1)
        button_sqrt_cos.grid(row=2, column=2)
        button_divide_tan.grid(row=2, column=3)

        button_1.grid(row=5, column=0)
        button_2.grid(row=5, column=1)
        button_3.grid(row=5, column=2)
        button_plus.grid(row=5, column=3)

        button_4.grid(row=4, column=0)
        button_5.grid(row=4, column=1)
        button_6.grid(row=4, column=2)
        button_minus.grid(row=4, column=3)

        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)
        button_multiply_factorial.grid(row=3, column=3)

        button_2nd.grid(row=6, column=0, pady=5)
        button_0.grid(row=6, column=1)
        button_decimal_point.grid(row=6, column=2)
        button_equal_sign.grid(row=6, column=3)

        button_temp_page.grid(row=1, column=0, columnspan=2)
        button_currency_page.grid(row=1, column=2, columnspan=2)

        button_settings_page.grid(row=0, column=0)


class settings_page(tk.Frame):
    # page that handles settings
    def __init__(self, parent, controller):
        self.control = Controller()
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Settings", font=LARGEFONT, justify=CENTER, background="yellow")
        self.config(bg="yellow")

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        temperature_button = ttk.Button(self, text="Temperature Conversion",
                                        command=lambda: controller.show_frame("temperature_page"))

        # putting the button in its place by
        # using grid
        temperature_button.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        currency_button = ttk.Button(self, text="Currency Exchange",
                                     command=lambda: controller.show_frame("currency_page"))

        # putting the button in its place by
        # using grid
        currency_button.grid(row=1, column=2, padx=10, pady=10)

        # main page button and add to grid
        main_page_button = ttk.Button(self, text="Main Calculator",
                                      command=lambda: controller.show_frame("main_page"))

        main_page_button.grid(row=1, column=3, padx=10, pady=10)

        global deg_rad
        deg_rad = True

        def degree_push():
            if not self.control.degrees:
                self.control.degrees = True
                degrees_button.config(relief=SUNKEN, bg="green")
                radians_button.config(relief=RAISED, bg="gray")
                global deg_rad
                deg_rad = True

        def radian_push():
            if self.control.degrees:
                self.control.degrees = False
                degrees_button.config(relief=RAISED, bg="gray")
                radians_button.config(relief=SUNKEN, bg="green")
                global deg_rad
                deg_rad = False

        degrees_button = Button(self, text="Degrees", relief=SUNKEN, height=5, width=20, bg="green", command=lambda: degree_push())
        radians_button = Button(self, text="Radians", relief=RAISED, height=5, width=20, bg="gray", command=lambda: radian_push())

        degrees_button.grid(row=2, column=0, columnspan=2, rowspan=2)
        radians_button.grid(row=2, column=2, columnspan=2, rowspan=2)


class temperature_page(tk.Frame):
    # page that handles temperature conversions
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Temperature Conversion", font=('Arial', 20), anchor="center")

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky=E+W+N+S)

        settings_button = ttk.Button(self, text="Settings",
                                     command=lambda: controller.show_frame("settings_page"))

        # putting the button in its place by
        # using grid
        settings_button.grid(row=1, column=0, padx=10, pady=10)

        # button to show frame 2 with text layout2
        currency_button = ttk.Button(self, text="Currency Exchange",
                                     command=lambda: controller.show_frame("currency_page"))

        # putting the button in its place by
        # using grid
        currency_button.grid(row=1, column=1, padx=10, pady=10)

        # main page button and add to grid
        main_page_button = ttk.Button(self, text="Main Calculator",
                                      command=lambda: controller.show_frame("main_page"))

        main_page_button.grid(row=1, column=2, padx=10, pady=10)

        # config page size and format
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

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

        display_box = Label(self, width=15, borderwidth=5, font=('Arial', 10), relief=RIDGE)
        display_box.grid(row=2, column=2)

        second_clicked = StringVar()
        second_clicked.set("Temp")
        displayed_drop_menu = OptionMenu(self, second_clicked, *options)
        displayed_drop_menu.grid(row=2, column=3)

        calculate_button = ttk.Button(self, text="Calculate", command=lambda: calculate())
        calculate_button.grid(row=3, column=0, columnspan=4, pady=10)

        def calculate():
            user_temp = float(user_input_box.get())
            new_temp = 0
            if (first_clicked.get() == "Farenheit"):
                if (second_clicked.get() == "Farenheit"):
                    display_box.config(text="")
                    new_temp = user_temp
                elif (second_clicked.get() == "Celsius"):
                    display_box.config(text="")
                    new_temp = ((user_temp-32)*(5/9))
                elif (second_clicked.get() == "Kelvin"):
                    display_box.config(text="")
                    new_temp = ((user_temp-32)*(5/9)+273.15)
            elif (first_clicked.get() == "Celsius"):
                if (second_clicked.get() == "Farenheit"):
                    display_box.config(text="")
                    new_temp = (user_temp * (9/5) + 32)
                elif (second_clicked.get() == "Celsius"):
                    display_box.config(text="")
                    new_temp = user_temp
                elif (second_clicked.get() == "Kelvin"):
                    display_box.config(text="")
                    new_temp = (user_temp + 273.15)
            elif (first_clicked.get() == "Kelvin"):
                if (second_clicked.get() == "Farenheit"):
                    display_box.config(text="")
                    new_temp = ((user_temp-273.15) * (9/5) + 32)
                elif (second_clicked.get() == "Celsius"):
                    display_box.config(text="")
                    new_temp = (user_temp - 273.15)
                elif (second_clicked.get() == "Kelvin"):
                    display_box.config(text="")
                    new_temp = user_temp

            display_box.config(text=str(round(new_temp, 2)))


class currency_page(tk.Frame):
    # page that handles currency conversions
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Currency Exchange", font=LARGEFONT)

        # currency converter object
        c = CurrencyConverter()
        curr_set = c.currencies

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        settings_button = ttk.Button(self, text="Settings",
                                     command=lambda: controller.show_frame("settings_page"))

        # putting the button in its place by
        # using grid
        settings_button.grid(row=1, column=0, padx=10, pady=10)

        # button to show frame 2 with text layout2
        temperature_button = ttk.Button(self, text="Temperature Conversion",
                                        command=lambda: controller.show_frame("temperature_page"))

        # putting the button in its place by
        # using grid
        temperature_button.grid(row=1, column=1, padx=10, pady=10)

        # main page button and add to grid
        main_page_button = ttk.Button(self, text="Main Calculator",
                                      command=lambda: controller.show_frame("main_page"))

        main_page_button.grid(row=1, column=2, padx=10, pady=10)

        def button_calculate():
            money_entered = float(user_input_box.get())
            conversion = round(c.convert(money_entered, first_clicked.get(), second_clicked.get()), 2)
            display_box.config(text=str(conversion))

        # create dropdowns for choosing currency conversions
        options = [
            "USD",
            "EUR",
            "AUD",
            "CAD",
            "GBP",
            "DKK",
            "RUB"
        ]

        user_input_box = Entry(self, width=15, borderwidth=5, font=('Arial', 10))
        user_input_box.grid(row=2, column=0)

        first_clicked = StringVar()
        first_clicked.set("Currency")
        first_drop_menu = OptionMenu(self, first_clicked, *options)
        first_drop_menu.grid(row=2, column=1)

        display_box = Label(self, width=15, borderwidth=5, relief=RIDGE, font=('Arial', 10))
        display_box.grid(row=2, column=2, padx=0)

        second_clicked = StringVar()
        second_clicked.set("Currency")
        displayed_drop_menu = OptionMenu(self, second_clicked, *options)
        displayed_drop_menu.grid(row=2, column=3, padx=0)

        calculate_button = ttk.Button(self, text="Calculate", command=lambda: button_calculate())
        calculate_button.grid(row=3, column=0, columnspan=4)


# driver code
root = page_container()
root.mainloop()


# notes:
# pictures for degrees, currencys
# fix settings page DONE
# implement rest of math via second DONE
# fix user input when they type divide by 0 DONE
#
#
#
#
#
#
