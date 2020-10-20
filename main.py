from tkinter import *


root = Tk()


class Player:

    def __init__(self, master=None):
        self.root = root
        self.window()
        self.labels()
        root.mainloop()

    def window(self, **kwargs):
        self.w_height = 440
        self.w_width = 630
        self.root.title('MP3 PLAYER')

        try:
            self.w_width = kwargs['width']
        except KeyError:
            pass

        try:
            self.w_width = kwargs['height']
        except KeyError:
            pass

        self.screenWidht = self.root.winfo_screenmmwidth()
        self.screenHeight = self.root.winfo_screenheight()
        self.left = (self.screenWidht / 2) - (self.w_width / 2)
        self.top = (self.screenHeight / 2) - (self.w_height / 2)

        self.root.geometry('%dx%d+%d+%d' % (self.w_width,
                                            self.w_height,
                                            self.left, self.top))
    def labels(self):
        self.winmus = Text(self.root, bg='white')
        self.winmus.configure(state='disabled')
        self.winmus.place(height=300, width=300, x=165, bordermode=INSIDE)

Player(root)
