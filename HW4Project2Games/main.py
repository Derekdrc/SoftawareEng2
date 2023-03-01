"""
name: Derek D'Arcy
Description: This program is the gui for project 2 which will have RPS and TICTACTOE
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os


class Controller_Class:
    def __init__(self):
        self.current_entry_num = 0
        self.degrees = True
        self.absolute_path = os.path.dirname(__file__)
        self.second = False


class Page_Container(tk.Tk):
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
        for F, geometry in zip((Welcome, RPS_Settings), ('100x100', '100x100')):
            page_name = F.__name__
            frame = F(parent=container, controller=self)

            self.frames[page_name] = (frame, geometry)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Welcome")
        self.title("Home Page")

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame, geometry = self.frames[cont]
        self.update_idletasks()
        self.geometry(geometry)
        frame.tkraise()


class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(bg="blue", padx=5, pady=5)


class RPS_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(bg="blue", padx=5, pady=5)


root = Page_Container()
root.mainloop()
