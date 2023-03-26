"""
name: Derek D'Arcy
Description: This program is the gui for project 2 which will have RPS and TICTACTOE
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import os
import time
from flask import Flask



'''
Purple Illusion - #beadfe
Dreamy Candy Forest - #b4a2f1
Magic Carpet - #897dc7
Seven Seas - #446073
Continental Waters - #9bc5cc
Quick-Freeze - #c3dfe4
Wave Splash - #c7e2e7

'''

#Create flask webhost
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def get_choice():
    player_two_choice = 0
    print(player_two_choice)
    
    return player_two_choice

class Controller_Class:
    def __init__(self):
        self.absolute_path = os.path.dirname(__file__)

        self.bold_font = ("Arial", 20, "bold")
        self.large_font = ("Arial", 16)
        self.normal_font = ("Arial", 12)

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
        for F, geometry in zip((Welcome, RPS_Settings, RPS_One_Choose, RPS_Two_Choose, RPS_Socket, RPS_Output, TTT_Settings, TTT_Board_One_Player, TTT_Board_Two_Player), ('300x300', '400x400', '300x300', '400x400', '400x400', '', '250x300', '400x400', '400x400')):
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
        title_label = Label(self, text="Mini Game Corner", font=self.control.large_font, fg=self.control.seven_seas,
                            background=self.control.purple_illusion, width=15)
        rps_button = Button(self, text="Rock Paper Scissors", font=self.control.normal_font, borderwidth=5,
                            width=20, height=5, background=self.control.quick_freeze, command=lambda: controller.show_frame("RPS_Settings"))
        ttt_button = Button(self, text="Tic-Tac-Toe", borderwidth=5, background=self.control.quick_freeze,
                            font=self.control.normal_font, width=20, height=5, command=lambda: controller.show_frame("TTT_Settings"))

        # add button and labels to frame with grid
        title_label.grid(row=0, column=0,  padx=5, pady=5, sticky=NSEW)
        rps_button.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)
        ttt_button.grid(row=3, column=0, sticky=NSEW, padx=5, pady=5)


class RPS_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        self.config(bg=self.control.purple_illusion)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        top_row = tk.Frame(self)
        top_row.config(background=self.control.purple_illusion)

        # images
        home_img_path = os.path.join(self.control.absolute_path, 'images/home.png')
        home_photo = PhotoImage(file=home_img_path)
        home_photo_sub = home_photo.subsample(3, 3)

        # create button and labels
        button_home_page = Button(top_row, image=home_photo_sub, padx=40, pady=10, background=self.control.purple_illusion,
                                  relief=GROOVE, borderwidth=2, command=lambda: controller.show_frame("Welcome"))
        button_home_page.image = home_photo_sub  # type: ignore # keep a reference
        button_home_page.pack(side="left")
        rps_label = Label(top_row, text="Rock-Paper-Scissors", font=self.control.bold_font, width=18, background=self.control.purple_illusion, borderwidth=5)
        rps_label.pack(side="left")

        # create buttons
        one_player_button = Button(self, text="One Player", font=("Arial", 24), width=15, borderwidth=5,
                                   background=self.control.continental_waters, relief=SUNKEN, command=lambda: one_player_button_press())
        two_player_button = Button(self, text="Two Player", font=("Arial", 24), width=15, borderwidth=5,
                                   background=self.control.seven_seas, relief=RAISED, command=lambda: two_player_button_press())
        two_player_socket_button = Button(self, text="2 Player P2P", font=("Arial", 24), width=15, borderwidth=5,
                                          background=self.control.seven_seas, relief=RAISED, command=lambda: two_player_e2e_button_press())
        ready_button = Button(self, text="Play!", font=("Arial", 24), width=15, borderwidth=5, background=self.control.magic_carpet, command=lambda: ready_button_press())

        # add to grids
        top_row.grid(column=0, row=0)
        one_player_button.grid(column=0, row=1)
        two_player_button.grid(column=0, row=2)
        two_player_socket_button.grid(column=0, row=3)
        ready_button.grid(column=0, row=4)

        global rps_players
        rps_players = 1

        def one_player_button_press():
            global rps_players
            rps_players = 1
            one_player_button.config(relief=SUNKEN, background=self.control.continental_waters)
            two_player_button.config(relief=RAISED, background=self.control.seven_seas)
            two_player_socket_button.config(relief=RAISED, background=self.control.seven_seas)

        def two_player_button_press():
            global rps_players
            rps_players = 2
            one_player_button.config(relief=RAISED, background=self.control.seven_seas)
            two_player_button.config(relief=SUNKEN, background=self.control.continental_waters)
            two_player_socket_button.config(relief=RAISED, background=self.control.seven_seas)

        def two_player_e2e_button_press():
            global rps_players
            rps_players = 3
            one_player_button.config(relief=RAISED, background=self.control.seven_seas)
            two_player_button.config(relief=RAISED, background=self.control.seven_seas)
            two_player_socket_button.config(relief=SUNKEN, background=self.control.continental_waters)

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
        self.config(background=self.control.purple_illusion)

        choose_label = Label(self, text="Make your choice!", font=self.control.bold_font,
                             foreground=self.control.seven_seas, background=self.control.purple_illusion, padx=5, pady=5)
        rock_button = Button(self, text="Rock", relief=SUNKEN, background=self.control.continental_waters, command=lambda: rock_button_press())
        paper_button = Button(self, text="Paper", relief=RAISED, background=self.control.seven_seas, command=lambda: paper_button_press())
        scissor_button = Button(self, text="Scissor", relief=RAISED, background=self.control.seven_seas, command=lambda: scissor_button_press())
        shoot_button = Button(self, text="Shoot!", relief=RAISED, background=self.control.magic_carpet, command=lambda: shoot_button_press())

        choose_label.grid(column=0, row=0, sticky=NSEW)
        rock_button.grid(column=0, row=1, sticky=NSEW)
        paper_button.grid(column=0, row=2, sticky=NSEW)
        scissor_button.grid(column=0, row=3, sticky=NSEW)
        shoot_button.grid(column=0, row=4, sticky=NSEW)

        global player_one_choice
        player_one_choice = 1

        def rock_button_press():
            global player_one_choice
            player_one_choice = 1
            rock_button.config(relief=SUNKEN, background=self.control.continental_waters)
            paper_button.config(relief=RAISED, background=self.control.seven_seas)
            scissor_button.config(relief=RAISED, background=self.control.seven_seas)

        def paper_button_press():
            global player_one_choice
            player_one_choice = 2
            rock_button.config(relief=RAISED, background=self.control.seven_seas)
            paper_button.config(relief=SUNKEN, background=self.control.continental_waters)
            scissor_button.config(relief=RAISED, background=self.control.seven_seas)

        def scissor_button_press():
            global player_one_choice
            player_one_choice = 3
            rock_button.config(relief=RAISED, background=self.control.seven_seas)
            paper_button.config(relief=RAISED, background=self.control.seven_seas)
            scissor_button.config(relief=SUNKEN, background=self.control.continental_waters)

        def shoot_button_press():
            global player_one_choice
            global player_two_choice
            player_two_choice = random.randint(1, 3)
            if(player_one_choice == 0):
                player_one_choice = 1
                controller.show_frame("RPS_Output")
            else:
                controller.show_frame("RPS_Output")


class RPS_Two_Choose(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        choose_label = Label(self, text="Make your choice!", font=self.control.bold_font,
                             foreground=self.control.seven_seas, background=self.control.purple_illusion, padx=5, pady=5)
        p1_rock_button = Button(self, text="Rock", relief=SUNKEN, background=self.control.continental_waters,
                                activebackground=self.control.continental_waters, command=lambda: p1_rock_button_press())
        p1_paper_button = Button(self, text="Paper", relief=SUNKEN, background=self.control.continental_waters,
                                 activebackground=self.control.continental_waters, command=lambda: p1_paper_button_press())
        p1_scissor_button = Button(self, text="Scissor", relief=SUNKEN, background=self.control.continental_waters,
                                   activebackground=self.control.continental_waters, command=lambda: p1_scissor_button_press())
        p2_rock_button = Button(self, text="Rock", relief=SUNKEN, background=self.control.continental_waters,
                                activebackground=self.control.continental_waters, command=lambda: p2_rock_button_press())
        p2_paper_button = Button(self, text="Paper", relief=SUNKEN, background=self.control.continental_waters,
                                 activebackground=self.control.continental_waters, command=lambda: p2_paper_button_press())
        p2_scissor_button = Button(self, text="Scissor", relief=SUNKEN, background=self.control.continental_waters,
                                   activebackground=self.control.continental_waters, command=lambda: p2_scissor_button_press())
        shoot_button = Button(self, text="Shoot!", relief=SUNKEN, background=self.control.magic_carpet, command=lambda: shoot_button_press())

        choose_label.grid(column=0, columnspan=2, row=0, sticky=NSEW)
        p1_rock_button.grid(column=0, row=1, sticky=NSEW)
        p1_paper_button.grid(column=0, row=2, sticky=NSEW)
        p1_scissor_button.grid(column=0, row=3, sticky=NSEW)
        p2_rock_button.grid(column=1, row=1, sticky=NSEW)
        p2_paper_button.grid(column=1, row=2, sticky=NSEW)
        p2_scissor_button.grid(column=1, row=3, sticky=NSEW)
        shoot_button.grid(column=0, columnspan=2, row=4, sticky=NSEW)

        global player_one_choice
        player_one_choice = 0

        global player_two_choice
        player_two_choice = 0

        def p1_rock_button_press():
            global player_one_choice
            player_one_choice = 1

        def p1_paper_button_press():
            global player_one_choice
            player_one_choice = 2

        def p1_scissor_button_press():
            global player_one_choice
            player_one_choice = 3

        def p2_rock_button_press():
            global player_two_choice
            player_two_choice = 1

        def p2_paper_button_press():
            global player_two_choice
            player_two_choice = 2

        def p2_scissor_button_press():
            global player_two_choice
            player_two_choice = 3

        def shoot_button_press():
            if (player_one_choice != 0 and player_two_choice != 0):
                controller.show_frame("RPS_Output")


class RPS_Socket(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5, background=self.control.purple_illusion)

        


class RPS_Output(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5, background=self.control.purple_illusion)

        animation = tk.Frame(self)
        animation.config(background=self.control.purple_illusion)
        result_page = tk.Frame(self)

        animation.grid(row=0, column=0)
        result_page.grid(row=0, column=0, sticky='NESW')

        animation.grid()
        result_page.grid_remove()

        # This part is the animation part
        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.config(background=self.control.purple_illusion)

        # images
        rps_gif_path = os.path.join(self.control.absolute_path, 'images/infiniteRPS.gif')
        rps_gif = PhotoImage(file=rps_gif_path)
        rps_gif_sub = rps_gif.subsample(3, 3)

        display = Label(animation, image=rps_gif_sub, relief=FLAT, padx=10, pady=20, borderwidth=0)
        display.image = rps_gif_sub  # type: ignore # keep a reference

        display.grid(column=0, row=0)

        result = Button(animation, text="See Result", background=self.control.purple_illusion,
                        fg=self.control.seven_seas, command=lambda: update_results())
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
            animation.after(175, animate, frame_number+1)

        animate(0)

        # End of animation part

        # helps with dynamic resizing
        result_page.grid_rowconfigure(0, weight=1)
        result_page.grid_columnconfigure(0, weight=1)
        result_page.grid_rowconfigure(1, weight=1)
        result_page.grid_columnconfigure(1, weight=1)
        result_page.grid_rowconfigure(2, weight=1)
        result_page.grid_columnconfigure(2, weight=1)
        result_page.grid_rowconfigure(3, weight=1)
        result_page.grid_columnconfigure(3, weight=1)
        result_page.grid_rowconfigure(4, weight=1)

        self.config(background=self.control.purple_illusion)

        # images
        home_img_path = os.path.join(self.control.absolute_path, 'images/home.png')
        home_photo = PhotoImage(file=home_img_path)
        home_photo_sub = home_photo.subsample(5, 5)

        restart_img_path = os.path.join(self.control.absolute_path, 'images/restart.png')
        restart_photo = PhotoImage(file=restart_img_path)
        restart_photo_sub = restart_photo.subsample(5, 5)

        left_rock_path = os.path.join(self.control.absolute_path, 'images/leftRockHand.png')
        left_rock_photo = PhotoImage(file=left_rock_path)
        left_rock_photo_sub = left_rock_photo.subsample(2, 2)

        right_rock_path = os.path.join(self.control.absolute_path, 'images/rightRockHand.png')
        right_rock_photo = PhotoImage(file=right_rock_path)
        right_rock_photo_sub = right_rock_photo.subsample(2, 2)

        left_paper_path = os.path.join(self.control.absolute_path, 'images/leftPaperHand.png')
        left_paper_photo = PhotoImage(file=left_paper_path)
        left_paper_photo_sub = left_paper_photo.subsample(2, 2)

        right_paper_path = os.path.join(self.control.absolute_path, 'images/rightPaperHand.png')
        right_paper_photo = PhotoImage(file=right_paper_path)
        right_paper_photo_sub = right_paper_photo.subsample(2, 2)

        left_scissor_path = os.path.join(self.control.absolute_path, 'images/leftScissorHand.png')
        left_scissor_photo = PhotoImage(file=left_scissor_path)
        left_scissor_photo_sub = left_scissor_photo.subsample(2, 2)

        right_scissor_path = os.path.join(self.control.absolute_path, 'images/rightScissorHand.png')
        right_scissor_photo = PhotoImage(file=right_scissor_path)
        right_scissor_photo_sub = right_scissor_photo.subsample(2, 2)

        # create buttons and labels
        p1_chose_label = Label(result_page, text="Player 1 Chose: ", background=self.control.purple_illusion)
        p1_picture = Label(result_page, image=left_rock_photo_sub, background=self.control.purple_illusion)
        p1_picture.image = left_rock_photo_sub  # type: ignore

        p2_chose_label = Label(result_page, text="Player 2 Chose: ", background=self.control.purple_illusion)
        p2_picture = Label(result_page, image=right_rock_photo_sub, background=self.control.purple_illusion)
        p2_picture.image = right_rock_photo_sub  # type: ignore

        winner_text_label = Label(result_page, text="Winner: ", background=self.control.purple_illusion)
        winner_box = Label(result_page, text="Player 1!", background=self.control.purple_illusion)

        home_button = Button(result_page, image=home_photo_sub, background=self.control.purple_illusion, command=lambda: home_button_press())
        home_button.image = home_photo_sub  # type: ignore # keep a reference
        play_again_button = Button(result_page, image=restart_photo_sub, background=self.control.purple_illusion, command=lambda: restart_button_press())
        play_again_button.image = restart_photo_sub  # type: ignore # keep a reference

        # layout to grid
        p1_chose_label.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        p1_picture.grid(row=1, column=0, columnspan=2, rowspan=2, sticky=NSEW)

        p2_chose_label.grid(row=0, column=2, columnspan=2, sticky=NSEW)
        p2_picture.grid(row=1, column=2, columnspan=2, rowspan=2, sticky=NSEW)

        winner_text_label.grid(row=3, column=0, columnspan=3, sticky=NSEW)
        winner_box.grid(row=4, column=0, columnspan=3, sticky=NSEW)

        home_button.grid(row=3, column=3, sticky=NSEW)
        play_again_button.grid(row=4, column=3, sticky=NSEW)

        def home_button_press():
            global player_one_choice
            global player_two_choice
            player_one_choice = 0
            player_two_choice = 0
            controller.show_frame("Welcome")
            result_page.grid_forget()
            animation.grid()

        def restart_button_press():
            global player_one_choice
            global player_two_choice
            player_one_choice = 0
            player_two_choice = 0
            controller.show_frame("RPS_Settings")
            result_page.grid_forget()
            animation.grid()

        def update_results():
            animation.grid_remove()
            result_page.grid()
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            if (player_one_choice == 1):
                p1_picture.config(image=left_rock_photo_sub)
                p1_picture.image = left_rock_photo_sub  # type: ignore
            elif (player_one_choice == 2):
                p1_picture.config(image=left_paper_photo_sub)
                p1_picture.image = left_paper_photo_sub  # type: ignore
            elif (player_one_choice == 3):
                p1_picture.config(image=left_scissor_photo_sub)
                p1_picture.image = left_scissor_photo_sub  # type: ignore

            if (player_two_choice == 1):
                p2_picture.config(image=right_rock_photo_sub)
                p2_picture.image = right_rock_photo_sub  # type: ignore
                if (player_one_choice == 1):
                    winner_box.config(text="Tie")
                elif (player_one_choice == 2):
                    winner_box.config(text="Player 1 Wins!")
                else:
                    winner_box.config(text="Player 2 Wins!")

            elif (player_two_choice == 2):
                p2_picture.config(image=right_paper_photo_sub)
                p2_picture.image = right_paper_photo_sub  # type: ignore
                if (player_one_choice == 1):
                    winner_box.config(text="Player 2 Wins!")
                elif (player_one_choice == 2):
                    winner_box.config(text="Tie")
                else:
                    winner_box.config(text="Player 1 Wins!")

            elif (player_two_choice == 3):
                p2_picture.config(image=right_scissor_photo_sub)
                p2_picture.image = right_scissor_photo_sub  # type: ignore
                if (player_one_choice == 1):
                    winner_box.config(text="Player 1 Wins!")
                elif (player_one_choice == 2):
                    winner_box.config(text="Player 2 Wins!")
                else:
                    winner_box.config(text="Tie")


class TTT_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5, background=self.control.purple_illusion)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        easy_hard = tk.Frame(self)

        # images
        home_img_path = os.path.join(self.control.absolute_path, 'images/home.png')
        home_photo = PhotoImage(file=home_img_path)
        home_photo_sub = home_photo.subsample(5, 5)

        title = Label(self, text="Tic-Tac-Toe", font=self.control.bold_font, background=self.control.purple_illusion)
        home_button = Button(self, image=home_photo_sub, background=self.control.purple_illusion, command=lambda: home_button_press())
        home_button.image = home_photo_sub  # type: ignore # keep a reference
        two_player = Button(self, text="Two Players", relief=SUNKEN, font=self.control.large_font, background=self.control.continental_waters, command=lambda: two_player_press())
        one_player = Button(self, text="One Player", font=self.control.large_font, background=self.control.seven_seas, command=lambda: one_player_press())

        easy = Button(easy_hard, state=DISABLED, text="Easy", font=self.control.large_font, background=self.control.seven_seas, command=lambda: easy_button_press())
        hard = Button(easy_hard, state=DISABLED, text="Hard", font=self.control.large_font, background=self.control.seven_seas, command=lambda: hard_button_press())
        easy.pack(side="left")
        hard.pack(side="left")

        play_button = Button(self, text="Play!", font=self.control.bold_font, background=self.control.magic_carpet, command=lambda: play_button_press())

        title.grid(column=1, row=0)
        home_button.grid(column=0, row=0)
        two_player.grid(column=0, row=1, columnspan=2)
        one_player.grid(column=0, row=2, columnspan=2)
        easy_hard.grid(column=0, row=3, columnspan=2)
        play_button.grid(column=0, row=4, columnspan=2)
        global ttt_players
        ttt_players = 2

        def home_button_press():
            controller.show_frame("Welcome")

        def easy_button_press():
            global ttt_mode
            ttt_mode = 1
            easy.config(relief=SUNKEN, background=self.control.continental_waters)
            hard.config(relief=RAISED, background=self.control.seven_seas)

        def hard_button_press():
            global ttt_mode
            ttt_mode = 2
            hard.config(relief=SUNKEN, background=self.control.continental_waters)
            easy.config(relief=RAISED, background=self.control.seven_seas)
        
        def one_player_press():
            global ttt_players
            ttt_players = 1
            global ttt_mode
            ttt_mode = 1
            two_player.config(relief=RAISED, background=self.control.seven_seas)
            one_player.config(relief=SUNKEN, background=self.control.continental_waters)
            easy.config(state=NORMAL, relief=SUNKEN, background=self.control.continental_waters)
            hard.config(state=NORMAL, relief=RAISED, background=self.control.seven_seas)

        def two_player_press():
            global ttt_players
            ttt_players = 2
            two_player.config(relief=SUNKEN, background=self.control.continental_waters)
            one_player.config(relief=RAISED, background=self.control.seven_seas)
            easy.config(state=DISABLED, relief=RAISED, background=self.control.seven_seas)
            hard.config(state=DISABLED, relief=RAISED, background= self.control.seven_seas)

        
        def play_button_press():
            global ttt_players
            if(ttt_players==2):
                controller.show_frame("TTT_Board_Two_Player")
            elif(ttt_players==1):
                if(ttt_mode == 1):
                    controller.show_frame("TTT_Board_One_Player")
                elif(ttt_mode == 2):
                    controller.show_frame("TTT_Board_One_Player")

                
class TTT_Board_One_Player(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5, background=self.control.purple_illusion)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #images
        X_img_path = os.path.join(self.control.absolute_path, 'images/X.png')
        X_photo = PhotoImage(file=X_img_path)
        X_photo_sub = X_photo.subsample(5, 5)

        O_img_path = os.path.join(self.control.absolute_path, 'images/O.png')
        O_photo = PhotoImage(file=O_img_path)
        O_photo_sub = O_photo.subsample(5, 5)

        home_img_path = os.path.join(self.control.absolute_path, 'images/home.png')
        home_photo = PhotoImage(file=home_img_path)
        home_photo_sub = home_photo.subsample(5, 5)

        restart_img_path = os.path.join(self.control.absolute_path, 'images/restart.png')
        restart_photo = PhotoImage(file=restart_img_path)
        restart_photo_sub = restart_photo.subsample(5, 5)

        blank_img_path = os.path.join(self.control.absolute_path, 'images/blank.png')
        blank_photo = PhotoImage(file=blank_img_path)
        blank_photo_sub = blank_photo.subsample(5, 5)

        display = tk.Frame(self, background=self.control.purple_illusion)

        buttons = []
        global taken
        taken = [0,0,0,0,0,0,0,0,0]


        home_button = Button(display, image=home_photo_sub, background=self.control.purple_illusion, command=lambda: home_button_press())
        home_button.image = home_photo_sub  # type: ignore # keep a reference
        play_again_button = Button(display, image=restart_photo_sub, background=self.control.purple_illusion, command=lambda: restart_button_press())
        play_again_button.image = restart_photo_sub  # type: ignore # keep a reference

        buttons.append(Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_left_button_press()))
        buttons[0].image = blank_photo_sub #type: ignore
        buttons.append(Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_mid_button_press()))
        buttons[1].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_right_button_press()))
        buttons[2].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_left_button_press()))
        buttons[3].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_mid_button_press()))
        buttons[4].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_right_button_press()))
        buttons[5].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_left_button_press()))
        buttons[6].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_mid_button_press()))
        buttons[7].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_right_button_press()))
        buttons[8].image = blank_photo_sub #type: ignore
        

        turn_label = Label(display, text="Player One's Turn", font=self.control.large_font, background=self.control.purple_illusion)

        buttons[0].grid(row=0, column=0, sticky='NESW')
        buttons[1].grid(row=0, column=1, sticky='NESW')
        buttons[2].grid(row=0, column=2, sticky='NESW')
        buttons[3].grid(row=1, column=0, sticky='NESW')
        buttons[4].grid(row=1, column=1, sticky='NESW')
        buttons[5].grid(row=1, column=2, sticky='NESW')
        buttons[6].grid(row=2, column=0, sticky='NESW')
        buttons[7].grid(row=2, column=1, sticky='NESW')
        buttons[8].grid(row=2, column=2, sticky='NESW')

        turn_label.grid(column=0, columnspan=2, row=0)
        play_again_button.grid(column=0, row=1)
        home_button.grid(column=1, row=1)

        display.grid(column=0, columnspan=3, row=4)

        def home_button_press():
            global taken
            taken = [0,0,0,0,0,0,0,0,0]
            buttons[0].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_left_button_press())
            buttons[0].image = blank_photo_sub #type: ignore
            buttons[1].config( image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_mid_button_press())
            buttons[1].image = blank_photo_sub #type: ignore
            buttons[2].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_right_button_press())
            buttons[2].image = blank_photo_sub #type: ignore
            buttons[3].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_left_button_press())
            buttons[3].image = blank_photo_sub #type: ignore
            buttons[4].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_mid_button_press())
            buttons[4].image = blank_photo_sub #type: ignore
            buttons[5].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_right_button_press())
            buttons[5].image = blank_photo_sub #type: ignore
            buttons[6].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_left_button_press())
            buttons[6].image = blank_photo_sub #type: ignore
            buttons[7].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_mid_button_press())
            buttons[7].image = blank_photo_sub #type: ignore
            buttons[8].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_right_button_press())
            buttons[8].image = blank_photo_sub #type: ignore
            turn_label.config(text="Player One's Turn")
            controller.show_frame("Welcome")

        def restart_button_press():
            global taken
            taken = [0,0,0,0,0,0,0,0,0]
            buttons[0].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_left_button_press())
            buttons[0].image = blank_photo_sub #type: ignore
            buttons[1].config( image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_mid_button_press())
            buttons[1].image = blank_photo_sub #type: ignore
            buttons[2].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_right_button_press())
            buttons[2].image = blank_photo_sub #type: ignore
            buttons[3].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_left_button_press())
            buttons[3].image = blank_photo_sub #type: ignore
            buttons[4].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_mid_button_press())
            buttons[4].image = blank_photo_sub #type: ignore
            buttons[5].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_right_button_press())
            buttons[5].image = blank_photo_sub #type: ignore
            buttons[6].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_left_button_press())
            buttons[6].image = blank_photo_sub #type: ignore
            buttons[7].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_mid_button_press())
            buttons[7].image = blank_photo_sub #type: ignore
            buttons[8].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_right_button_press())
            buttons[8].image = blank_photo_sub #type: ignore
            turn_label.config(text="Player One's Turn")
            controller.show_frame("TTT_Settings")

        def top_left_button_press():
            global taken
            taken[0] = 1
            buttons[0].config(image=X_photo_sub, command=lambda: None)
            buttons[0].image = X_photo_sub #type: ignore
            check_winner()
            computer_turn()
        
        def top_mid_button_press():
            global taken
            taken[1] = 1
            buttons[1].config(image=X_photo_sub, command=lambda: None)
            buttons[1].image = X_photo_sub #type: ignore
            check_winner()
            computer_turn()

        def top_right_button_press():
            global taken
            taken[2] = 1
            buttons[2].config(image=X_photo_sub, command=lambda: None)
            buttons[2].image = X_photo_sub #type: ignore
            check_winner()
            computer_turn()

        def mid_left_button_press():
            global taken
            taken[3] = 1
            buttons[3].config(image=X_photo_sub, command=lambda: None)
            buttons[3].image = X_photo_sub #type: ignore
            check_winner()
            computer_turn()

        def mid_mid_button_press():
            global taken
            taken[4] = 1
            buttons[4].config(image=X_photo_sub, command=lambda: None)
            buttons[4].image = X_photo_sub #type: ignore
            check_winner()
            computer_turn()

        def mid_right_button_press():
            global taken
            taken[5] = 1
            buttons[5].config(image=X_photo_sub, command=lambda: None)
            buttons[5].image = X_photo_sub #type: ignore
            check_winner()
            computer_turn()

        def bot_left_button_press():
            global taken
            taken[6] = 1
            buttons[6].config(image=X_photo_sub, command=lambda: None)
            buttons[6].image = X_photo_sub #type: ignore
            check_winner()
            computer_turn()

        def bot_mid_button_press():
            global taken
            taken[7] = 1
            buttons[7].config(image=X_photo_sub, command=lambda: None)
            buttons[7].image = X_photo_sub #type: ignore
            check_winner()
            computer_turn()

        def bot_right_button_press():
            global taken
            taken[8] = 1
            buttons[8].config(image=X_photo_sub, command=lambda: None)
            buttons[8].image = X_photo_sub #type: ignore
            check_winner()
            computer_turn()

        def computer_turn():
            time.sleep(0.5)
            computers_turn = True
            counter = 0
            for x in taken:
                if taken[x] !=0:
                    counter+=1
            if counter >=8:
                computers_turn = False
                turn_label.config(text="Cat Game!")
            while(computers_turn):
                target = random.randint(0,8)
                while (taken[target] != 0):
                    target = random.randint(0,8)
                taken[target] = 2
                buttons[target].config(image=O_photo_sub, command=lambda: None)
                check_winner()
                computers_turn = False

        def check_winner():
            if(taken[0] == taken[1] == taken[2]):
                if(taken[0] == 0 or taken[1] == 0 or taken[2] == 0):
                    turn_label.config(text="Continue Playing")
                if taken[0] == 1:
                    turn_label.config(text="Player 1 Wins!")
                elif taken[0] == 2:
                    turn_label.config(text="Player 2 Wins!")
                    


class TTT_Board_Two_Player(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5, background=self.control.purple_illusion)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #images
        X_img_path = os.path.join(self.control.absolute_path, 'images/X.png')
        X_photo = PhotoImage(file=X_img_path)
        X_photo_sub = X_photo.subsample(5, 5)

        O_img_path = os.path.join(self.control.absolute_path, 'images/O.png')
        O_photo = PhotoImage(file=O_img_path)
        O_photo_sub = O_photo.subsample(5, 5)

        home_img_path = os.path.join(self.control.absolute_path, 'images/home.png')
        home_photo = PhotoImage(file=home_img_path)
        home_photo_sub = home_photo.subsample(5, 5)

        restart_img_path = os.path.join(self.control.absolute_path, 'images/restart.png')
        restart_photo = PhotoImage(file=restart_img_path)
        restart_photo_sub = restart_photo.subsample(5, 5)

        blank_img_path = os.path.join(self.control.absolute_path, 'images/blank.png')
        blank_photo = PhotoImage(file=blank_img_path)
        blank_photo_sub = blank_photo.subsample(5, 5)

        display = tk.Frame(self, background=self.control.purple_illusion)

        buttons = []
        global p2_taken
        p2_taken = [0,0,0,0,0,0,0,0,0]


        home_button = Button(display, image=home_photo_sub, background=self.control.purple_illusion, command=lambda: home_button_press())
        home_button.image = home_photo_sub  # type: ignore # keep a reference
        play_again_button = Button(display, image=restart_photo_sub, background=self.control.purple_illusion, command=lambda: restart_button_press())
        play_again_button.image = restart_photo_sub  # type: ignore # keep a reference

        buttons.append(Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_left_button_press()))
        buttons[0].image = blank_photo_sub #type: ignore
        buttons.append(Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_mid_button_press()))
        buttons[1].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_right_button_press()))
        buttons[2].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_left_button_press()))
        buttons[3].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_mid_button_press()))
        buttons[4].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_right_button_press()))
        buttons[5].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_left_button_press()))
        buttons[6].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_mid_button_press()))
        buttons[7].image = blank_photo_sub #type: ignore
        buttons.append( Button(self, image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_right_button_press()))
        buttons[8].image = blank_photo_sub #type: ignore
        

        turn_label = Label(display, text="Player One's Turn", font=self.control.large_font, background=self.control.purple_illusion)

        buttons[0].grid(row=0, column=0, sticky='NESW')
        buttons[1].grid(row=0, column=1, sticky='NESW')
        buttons[2].grid(row=0, column=2, sticky='NESW')
        buttons[3].grid(row=1, column=0, sticky='NESW')
        buttons[4].grid(row=1, column=1, sticky='NESW')
        buttons[5].grid(row=1, column=2, sticky='NESW')
        buttons[6].grid(row=2, column=0, sticky='NESW')
        buttons[7].grid(row=2, column=1, sticky='NESW')
        buttons[8].grid(row=2, column=2, sticky='NESW')

        turn_label.grid(column=0, columnspan=2, row=0)
        play_again_button.grid(column=0, row=1)
        home_button.grid(column=1, row=1)

        display.grid(column=0, columnspan=3, row=4)

        global player_turn
        player_turn = 1

        def top_left_button_press():
            global player_turn
            global p2_taken
            if player_turn == 1:    
                p2_taken[0] = 1
                buttons[0].config(image=X_photo_sub, command=lambda: None)
                buttons[0].image = X_photo_sub #type: ignore
                player_turn = 2
                turn_label.config(text= "Player Two's Turn")
            elif player_turn == 2:
                p2_taken[0] = 2
                buttons[0].config(image=O_photo_sub, command=lambda: None)
                buttons[0].image = O_photo_sub #type: ignore
                player_turn = 1
                turn_label.config(text= "Player One's Turn")
            for x in p2_taken:
                print(x)
            check_winner()
            
        
        def top_mid_button_press():
            global player_turn
            global p2_taken
            if player_turn == 1:    
                p2_taken[1] = 1
                buttons[1].config(image=X_photo_sub, command=lambda: None)
                buttons[1].image = X_photo_sub #type: ignore
                player_turn = 2
                turn_label.config(text= "Player Two's Turn")
            elif player_turn == 2:
                p2_taken[1] = 2
                buttons[1].config(image=O_photo_sub, command=lambda: None)
                buttons[1].image = O_photo_sub #type: ignore
                player_turn = 1
                turn_label.config(text= "Player One's Turn")
            check_winner()
            

        def top_right_button_press():
            global player_turn
            global p2_taken
            if player_turn == 1:    
                p2_taken[2] = 1
                buttons[2].config(image=X_photo_sub, command=lambda: None)
                buttons[2].image = X_photo_sub #type: ignore
                player_turn = 2
                turn_label.config(text= "Player Two's Turn")
            elif player_turn == 2:
                p2_taken[2] = 2
                buttons[2].config(image=O_photo_sub, command=lambda: None)
                buttons[2].image = O_photo_sub #type: ignore
                player_turn = 1
                turn_label.config(text= "Player One's Turn")
            check_winner()


        def mid_left_button_press():
            global player_turn
            global p2_taken
            if player_turn == 1:    
                p2_taken[3] = 1
                buttons[3].config(image=X_photo_sub, command=lambda: None)
                buttons[3].image = X_photo_sub #type: ignore
                player_turn = 2
                turn_label.config(text= "Player Two's Turn")
            elif player_turn == 2:
                p2_taken[3] = 2
                buttons[3].config(image=O_photo_sub, command=lambda: None)
                buttons[3].image = O_photo_sub #type: ignore
                player_turn = 1
                turn_label.config(text= "Player One's Turn")
            check_winner()
            

        def mid_mid_button_press():
            global player_turn
            global p2_taken
            if player_turn == 1:    
                p2_taken[4] = 2
                buttons[4].config(image=X_photo_sub, command=lambda: None)
                buttons[4].image = X_photo_sub #type: ignore
                player_turn = 2
                turn_label.config(text= "Player Two's Turn")
            elif player_turn == 2:
                p2_taken[4] = 2
                buttons[4].config(image=O_photo_sub, command=lambda: None)
                buttons[4].image = O_photo_sub #type: ignore
                player_turn = 1
                turn_label.config(text= "Player One's Turn")
            check_winner()
            

        def mid_right_button_press():
            global player_turn
            global p2_taken
            if player_turn == 1:    
                p2_taken[5] = 1
                buttons[5].config(image=X_photo_sub, command=lambda: None)
                buttons[5].image = X_photo_sub #type: ignore
                player_turn = 2
                turn_label.config(text= "Player Two's Turn")
            elif player_turn == 2:
                p2_taken[5] = 2
                buttons[5].config(image=O_photo_sub, command=lambda: None)
                buttons[5].image = O_photo_sub #type: ignore
                player_turn = 1
                turn_label.config(text= "Player One's Turn")
            check_winner()
            

        def bot_left_button_press():
            global player_turn
            global p2_taken
            if player_turn == 1:    
                p2_taken[6] = 1
                buttons[6].config(image=X_photo_sub, command=lambda: None)
                buttons[6].image = X_photo_sub #type: ignore
                player_turn = 2
                turn_label.config(text= "Player Two's Turn")
            elif player_turn == 2:
                p2_taken[6] = 2
                buttons[6].config(image=O_photo_sub, command=lambda: None)
                buttons[6].image = O_photo_sub #type: ignore
                player_turn = 1
                turn_label.config(text= "Player One's Turn")
            check_winner()
            

        def bot_mid_button_press():
            global player_turn
            global p2_taken
            if player_turn == 1:    
                p2_taken[7] = 1
                buttons[7].config(image=X_photo_sub, command=lambda: None)
                buttons[7].image = X_photo_sub #type: ignore
                player_turn = 2
                turn_label.config(text= "Player Two's Turn")
            elif player_turn == 2:
                p2_taken[7] = 2
                buttons[7].config(image=O_photo_sub, command=lambda: None)
                buttons[7].image = O_photo_sub #type: ignore
                player_turn = 1
                turn_label.config(text= "Player One's Turn")
            check_winner()
            

        def bot_right_button_press():
            global player_turn
            global p2_taken
            if player_turn == 1:    
                p2_taken[8] = 1
                buttons[8].config(image=X_photo_sub, command=lambda: None)
                buttons[8].image = X_photo_sub #type: ignore
                player_turn = 2
                turn_label.config(text= "Player Two's Turn")
            elif player_turn == 2:
                p2_taken[8] = 2
                buttons[8].config(image=O_photo_sub, command=lambda: None)
                buttons[8].image = O_photo_sub #type: ignore
                player_turn = 1
                turn_label.config(text= "Player One's Turn")
            check_winner()
        

        def check_winner():
            global p2_taken
            if p2_taken[0] == p2_taken[1] and p2_taken[1] == p2_taken[2]:
                if p2_taken[0] == 0 or p2_taken[1] == 0 or p2_taken[2] == 0:
                    pass
                elif p2_taken[0] == 1:
                    for x in (0,1,2):
                        buttons[x].config(background = self.control.magic_carpet)
                    turn_label.config(text="Player One Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())
                elif p2_taken[0] == 2:
                    for x in (0,1,2):
                        buttons[x].config(background = self.control.wave_splash)
                    turn_label.config(text="Player Two Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())

            if p2_taken[3] == p2_taken[4] and p2_taken[4] == p2_taken[5]:
                if p2_taken[0] == 0:
                    return False
                elif p2_taken[0] == 1:
                    for x in (3,4,5):
                        buttons[x].config(background = self.control.magic_carpet)
                    turn_label.config(text="Player One Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())
                elif p2_taken[0] == 2:
                    for x in (3,4,5):
                        buttons[x].config(background = self.control.wave_splash)
                    turn_label.config(text="Player Two Wins!")
                    print("player 2")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())
            
            if p2_taken[6] == p2_taken[7] and p2_taken[7] == p2_taken[8]:
                if p2_taken[0] == 0:
                    return False
                elif p2_taken[0] == 1:
                    for x in (6,7,8):
                        buttons[x].config(background = self.control.magic_carpet)
                    turn_label.config(text="Player One Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())
                elif p2_taken[0] == 2:
                    for x in (6,7,8):
                        buttons[x].config(background = self.control.wave_splash)
                    turn_label.config(text="Player Two Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())

            if p2_taken[0] == p2_taken[3] and p2_taken[3] == p2_taken[6]:
                if p2_taken[0] == 0:
                    return False
                elif p2_taken[0] == 1:
                    for x in (0,3,6):
                        buttons[x].config(background = self.control.magic_carpet)
                    turn_label.config(text="Player One Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())
                elif p2_taken[0] == 2:
                    for x in (0,3,6):
                        buttons[x].config(background = self.control.wave_splash)
                    turn_label.config(text="Player Two Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())

            if p2_taken[1] == p2_taken[4] and p2_taken[4] == p2_taken[7]:
                if p2_taken[0] == 0:
                    return False
                elif p2_taken[0] == 1:
                    for x in (1,4,7):
                        buttons[x].config(background = self.control.magic_carpet)
                    turn_label.config(text="Player One Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())
                elif p2_taken[0] == 2:
                    for x in (1,4,7):
                        buttons[x].config(background = self.control.wave_splash)
                    turn_label.config(text="Player Two Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())

            if p2_taken[2] == p2_taken[5] and p2_taken[5] == p2_taken[8]:
                if p2_taken[0] == 0:
                    return False
                elif p2_taken[0] == 1:
                    for x in (2,5,8):
                        buttons[x].config(background = self.control.magic_carpet)
                    turn_label.config(text="Player One Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())
                elif p2_taken[0] == 2:
                    for x in (2,5,8):
                        buttons[x].config(background = self.control.wave_splash)
                    turn_label.config(text="Player Two Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())

            if p2_taken[0] == p2_taken[4] and p2_taken[4] == p2_taken[8]:
                if p2_taken[0] == 0:
                    return False
                elif p2_taken[0] == 1:
                    for x in (0,4,8):
                        buttons[x].config(background = self.control.magic_carpet)
                    turn_label.config(text="Player One Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())
                elif p2_taken[0] == 2:
                    for x in (0,4,8):
                        buttons[x].config(background = self.control.wave_splash)
                    turn_label.config(text="Player Two Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())

            if p2_taken[6] == p2_taken[4] and p2_taken[4] == p2_taken[2]:
                if p2_taken[0] == 0:
                    return False
                elif p2_taken[0] == 1:
                    for x in (6,4,2):
                        buttons[x].config(background = self.control.magic_carpet)
                    turn_label.config(text="Player One Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())
                elif p2_taken[0] == 2:
                    for x in (6,4,2):
                        buttons[x].config(background = self.control.wave_splash)
                    turn_label.config(text="Player Two Wins!")
                    for x in (0,8):
                        buttons[x].config(command=lambda: do_nothing())


        def do_nothing():
            pass

        def home_button_press():
            global player_turn
            global p2_taken
            player_turn = 1
            for x in (0,8):
                p2_taken[x] = 0
            buttons[0].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_left_button_press())
            buttons[0].image = blank_photo_sub #type: ignore
            buttons[1].config( image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_mid_button_press())
            buttons[1].image = blank_photo_sub #type: ignore
            buttons[2].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_right_button_press())
            buttons[2].image = blank_photo_sub #type: ignore
            buttons[3].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_left_button_press())
            buttons[3].image = blank_photo_sub #type: ignore
            buttons[4].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_mid_button_press())
            buttons[4].image = blank_photo_sub #type: ignore
            buttons[5].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_right_button_press())
            buttons[5].image = blank_photo_sub #type: ignore
            buttons[6].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_left_button_press())
            buttons[6].image = blank_photo_sub #type: ignore
            buttons[7].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_mid_button_press())
            buttons[7].image = blank_photo_sub #type: ignore
            buttons[8].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_right_button_press())
            buttons[8].image = blank_photo_sub #type: ignore
            turn_label.config(text="Player One's Turn")
            controller.show_frame("Welcome")

        def restart_button_press():
            global player_turn
            global p2_taken
            for x in (0,8):
                p2_taken[x] = 0
            player_turn = 1
            buttons[0].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_left_button_press())
            buttons[0].image = blank_photo_sub #type: ignore
            buttons[1].config( image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_mid_button_press())
            buttons[1].image = blank_photo_sub #type: ignore
            buttons[2].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: top_right_button_press())
            buttons[2].image = blank_photo_sub #type: ignore
            buttons[3].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_left_button_press())
            buttons[3].image = blank_photo_sub #type: ignore
            buttons[4].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_mid_button_press())
            buttons[4].image = blank_photo_sub #type: ignore
            buttons[5].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: mid_right_button_press())
            buttons[5].image = blank_photo_sub #type: ignore
            buttons[6].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_left_button_press())
            buttons[6].image = blank_photo_sub #type: ignore
            buttons[7].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_mid_button_press())
            buttons[7].image = blank_photo_sub #type: ignore
            buttons[8].config(image=blank_photo_sub, background=self.control.seven_seas, command=lambda: bot_right_button_press())
            buttons[8].image = blank_photo_sub #type: ignore
            turn_label.config(text="Player One's Turn")
            controller.show_frame("TTT_Settings")
            


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
#
#
#
