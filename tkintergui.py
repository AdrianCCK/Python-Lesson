from tkinter import *
class MyFirstGUI:
    def __init__(self, master):
        self.op_string = ""
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="1", command=lambda: self.do_op('1') )
        self.greet_button.pack(side=LEFT)

        self.close_button = Button(master, text="+", command= lambda: self.do_op('+'))
        self.close_button.pack(side=LEFT)

        self.close_button = Button(master, text="-", command= lambda: self.do_op('-'))
        self.close_button.pack(side=LEFT)

        self.greet_button = Button(master, text="3", command=lambda: self.do_op('3'))
        self.greet_button.pack(side=LEFT)

        self.close_button = Button(master, text="=", command=lambda: self.evaluate())
        self.close_button.pack(side=LEFT)

        self.greet_button = Button(master, text="5", command=lambda: self.greet)
        self.greet_button.pack(side=LEFT)

        self.close_button = Button(master, text="quit", command=master.quit)
        self.close_button.pack(side=LEFT)

    def greet(self):
        print("Greetings!")
        self.win = Toplevel(self.master)
        self.win.title('A new Window')
        self.second_label = Label(self.win, text="Label in Pane 1")
        self.second_label.pack()
        self.win.mainloop()

    
    def do_op(self, txt):
        self.op_string += txt

    def evaluate(self):
        self.win = Toplevel(self.master)
        self.win.title('A new Window')
        self.second_label = Label(self.win, text= eval(self.op_string) )
        self.op_string = ""
        self.second_label.pack()
        self.win.mainloop()
        
        
        

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
