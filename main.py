from tkinter import *
import pygame
from tkinter import filedialog


pygame.init()
root = Tk()


class Player:

    def __init__(self, master=None):
        self.root = root
        self.window()
        self.labels()
        self.buttons()
        root.mainloop()

    def window(self, **kwargs):
        self.w_height = 440
        self.w_width = 630
        self.root.title('MP3 PLAYER')
        self.root.configure(background='#dde')

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
        self.winmus = Entry(self.root, bg='white')
        self.winmus.configure(state='disabled')
        self.winmus.place(height=300, width=300, x=165, bordermode=INSIDE)
    
    def buttons(self):
        self.previous = Button(self.root, text='<')
        self.previous.place(x=165, y=300, width=30)

        self.play = Button(self.root, text='Play/Pause')
        self.play.place(x=195, y=300, width=100)

        self.next = Button(self.root, text='>')
        self.next.place(x=295, y=300, width=30)

        self.add_ = Button(self.root, text='Adicionar música', command=self.add_msc)
        self.add_.place(x=325, y=300)

    def add_msc(self):
        self.dir = filedialog.askopenfilenames()

Player(root)
