from tkinter import *

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.bind("<Key>", self.input)

        self.l_input = Entry(self.window, bg="#b0b0b0")
        self.l_input.pack()
        
        self.r_input = Entry(self.window)
        self.r_input.pack()
        
        self.output = Entry(self.window, bg="#b0b0b0")
        self.output.pack()


    def run(self):
        self.window.mainloop()

    def input(self, event):
        if event.char == '\r':
            l = float(self.l_input.get())
            r = float(self.r_input.get())
            i: str = "dsf"
            self.output.delete(0, 'end')
            self.output.insert(0, str(l) + " + " + str(r) + " = " + str(l + r))
