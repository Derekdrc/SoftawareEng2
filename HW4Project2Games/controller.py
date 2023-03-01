import os


class Controller:
    def __init__(self):
        self.current_entry_num = 0
        self.degrees = True
        self.absolute_path = os.path.dirname(__file__)
        self.second = False
