"""
name: Derek D'Arcy
Description: This program is the gui for project 2 which will have RPS and TICTACTOE
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import time


'''
Purple Illusion - #beadfe
Dreamy Candy Forest - #b4a2f1
Magic Carpet - #897dc7
Seven Seas - #446073
Continental Waters - #9bc5cc
Quick-Freeze - #c3dfe4
Wave Splash - #c7e2e7

'''


class Controller_Class:
    def __init__(self):
        self.absolute_path = os.path.dirname(__file__)

        self.bold_font = ("Arial", 16, "bold")
        self.large_font = ("Arial", 12)

        self.rps_player_One_Choice = -1
        self.rps_player_Two_Choice = -1

        self.purple_illusion = "#beadfe"
        self.dream_forest = "#b4a2f1"
        self.magic_carpet = "#897dc7"
        self.seven_seas = "#446073"
        self.continental_waters = "#9bc5cc"
        self.quick_freeze = "#c3dfe4"
        self.wave_splash = "#c7e2e7"


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
        for F, geometry in zip((Welcome, RPS_Settings, RPS_One_Choose, RPS_Two_Choose, RPS_Animation, RPS_Output, TTT_Settings, TTT_Board), ('400x400', '400x400', '', '400x400', '', '400x400', '400x400', '400x400')):
            page_name = F.__name__
            frame = F(parent=container, controller=self)

            self.frames[page_name] = (frame, geometry)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Welcome")
        self.title("Minigame Corner")

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
        self.config(bg=self.control.purple_illusion)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create button and labels
        title_label = Label(self, text="Mini Game Corner", font=("Arial", 24), fg=self.control.seven_seas,
                            background=self.control.purple_illusion, width=15, borderwidth=5)
        rps_button = Button(self, text="Rock Paper Scissors", width=20, height=5, command=lambda: controller.show_frame("RPS_Settings"))
        ttt_button = Button(self, text="Tic-Tac-Toe", width=20, height=5)

        # add button and labels to frame with grid
        title_label.grid(row=0, column=0, rowspan=2,  padx=5, pady=5, sticky=NSEW)
        rps_button.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)
        ttt_button.grid(row=3, column=0, sticky=NSEW, padx=5, pady=5)


class RPS_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        top_row = tk.Frame(self)

        # images
        home_img_path = os.path.join(self.control.absolute_path, 'images/home.png')
        home_photo = PhotoImage(file=home_img_path)
        home_photo_sub = home_photo.subsample(10, 10)

        # create button and labels
        button_home_page = Button(top_row, image=home_photo_sub, padx=40, pady=10, command=lambda: controller.show_frame("Welcome"))
        button_home_page.image = home_photo_sub  # type: ignore # keep a reference
        button_home_page.pack(side="left")
        rps_label = Label(top_row, text="Rock Paper Scissors", font=("Arial", 24), width=15, borderwidth=5)
        rps_label.pack(side="left")

        # create buttons
        one_player_button = Button(self, text="One Player", font=("Arial", 24), width=15, borderwidth=5, relief=SUNKEN, command=lambda: one_player_button_press())
        two_player_button = Button(self, text="Two Player", font=("Arial", 24), width=15, borderwidth=5, relief=RAISED, bg="gray", command=lambda: two_player_button_press())
        ready_button = Button(self, text="Play!", font=("Arial", 24), width=15, borderwidth=5, command=lambda: ready_button_press())

        # add to grids
        top_row.grid(column=0, row=0)
        one_player_button.grid(column=0, row=1)
        two_player_button.grid(column=0, row=2)
        ready_button.grid(column=0, row=3)

        global rps_players
        rps_players = 1

        def one_player_button_press():
            global rps_players
            rps_players = 1
            one_player_button.config(relief=SUNKEN, bg="white")
            two_player_button.config(relief=RAISED, bg="gray")

        def two_player_button_press():
            global rps_players
            rps_players = 2
            one_player_button.config(relief=RAISED, bg="gray")
            two_player_button.config(relief=SUNKEN, bg="white")

        def ready_button_press():
            if (rps_players == 1):
                controller.show_frame("RPS_One_Choose")
            elif (rps_players == 2):
                controller.show_frame("RPS_Two_Choose")


class RPS_One_Choose(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        choose_label = Label(self, text="Make your choice!", font=self.control.bold_font, padx=10, pady=10, bg='white')
        rock_button = Button(self, text="Rock", relief=SUNKEN, background=self.control.continental_waters, command=lambda: rock_button_press())
        paper_button = Button(self, text="Paper", relief=RAISED, background=self.control.seven_seas, command=lambda: paper_button_press())
        scissor_button = Button(self, text="Scissor", relief=RAISED, background=self.control.seven_seas, command=lambda: scissor_button_press())
        shoot_button = Button(self, text="Shoot!", relief=RAISED, background=self.control.dream_forest, command=lambda: shoot_button_press())

        choose_label.grid(column=0, row=0, sticky=NSEW)
        rock_button.grid(column=0, row=1, sticky=NSEW)
        paper_button.grid(column=0, row=2, sticky=NSEW)
        scissor_button.grid(column=0, row=3, sticky=NSEW)
        shoot_button.grid(column=0, row=4, sticky=NSEW)

        def rock_button_press():
            self.control.rps_player_One_Choice = 1
            rock_button.config(relief=SUNKEN, background=self.control.continental_waters)
            paper_button.config(relief=RAISED, background=self.control.seven_seas)
            scissor_button.config(relief=RAISED, background=self.control.seven_seas)

        def paper_button_press():
            self.control.rps_player_One_Choice = 2
            rock_button.config(relief=RAISED, background=self.control.seven_seas)
            paper_button.config(relief=SUNKEN, background=self.control.continental_waters)
            scissor_button.config(relief=RAISED, background=self.control.seven_seas)

        def scissor_button_press():
            self.control.rps_player_One_Choice = 3
            rock_button.config(relief=RAISED, background=self.control.seven_seas)
            paper_button.config(relief=RAISED, background=self.control.seven_seas)
            scissor_button.config(relief=SUNKEN, background=self.control.continental_waters)

        def shoot_button_press():
            controller.show_frame("RPS_Animation")


class RPS_Two_Choose(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class RPS_Animation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.config(background=self.control.quick_freeze)

        # images
        rps_gif_path = os.path.join(self.control.absolute_path, 'images/infiniteRPS.gif')
        rps_gif = PhotoImage(file=rps_gif_path)
        rps_gif_sub = rps_gif.subsample(3, 3)

        display = Label(self, image=rps_gif_sub, padx=10, pady=20, bg='white')
        display.image = rps_gif_sub  # type: ignore # keep a reference

        display.grid(column=0, row=0)

        result = Button(self, text="See Result", command=lambda: controller.show_frame("RPS_Output"))
        result.grid(column=0, row=1)

        frameList = []
        frame_index = 0

        while True:
            try:
                # Read a frame from GIF file
                part = 'gif -index {}'.format(frame_index)
                frame = tk.PhotoImage(file=rps_gif_path, format=part)
            except:
                last_frame = frame_index - 1    # Save index for last frame
                break               # Will break when GIF index is reached
            frameList.append(frame)
            frame_index += 1        # Next frame index

        def animate(frame_number):
            if frame_number > last_frame:
                frame_number = 0
            display.config(image=frameList[frame_number])
            self.after(125, animate, frame_number+1)

        animate(0)


class RPS_Output(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class TTT_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class TTT_Board(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


root = Page_Container()
root.mainloop()


# ideas:
#
#
#
#
#
#
#
#
