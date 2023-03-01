import container
import controller
import tkinter as tk


class Welcome(tk.Frame):
    def __init__(self, container.parent, container.controller):
        tk.Frame.__init__(self, container.parent)
        self.control = controller.Controller()
        self.config(bg="blue", padx=5, pady=5)
