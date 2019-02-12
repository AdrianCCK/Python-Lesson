from tkinter import *

import winsound

class MyFirstGUI:
    def __init__(self, master):
        self.op_string = ""
        self.master = master
        master.title("Messaging App")

        self.username_label = Label(master, text= "Username")

        self.username_label.pack()
        
        self.username_txt = StringVar()
        self.username_entry = Entry(master, textvariable = self.username_txt)
        self.username_entry.pack()

        self.label = Label(master, text="Messages")
        self.label.pack()
        
        self.msginput_txt = StringVar()

        self.msgbox = Text(master );
        
        #self.msgbox.config(state=DISABLED)
        self.msgbox.pack()

        
        self.msginput = Entry(master, textvariable = self.msginput_txt)
        self.msginput.pack()

        self.greet_button = Button(master, text="Send", command=lambda: self.send_message(   ) )
        self.greet_button.pack(side=LEFT)


        f = open('msgbuffer.txt', 'r+')
        
        messages = f.readlines()
        mailboxSize = len(messages)


        f.close()
        
        if mailboxSize > 0 :
            #self.msgbox.delete(1.0, END)
            self.msgbox.insert(END, "".join( messages))
        self.msgbox.config(state=DISABLED)

        self.master.after(500, self.refresh_message)
        
    def refresh_message(self):
        self.msgbox.config(state=NORMAL)
        
        f = open('msgbuffer.txt', 'r+')
        username = self.username_txt.get()
        messages = f.readlines()
        mailboxSize = len(messages)        
        f.close()
        if mailboxSize > 0 :
            self.msgbox.delete(1.0, END)
            self.msgbox.insert(END, "".join(messages))
            winsound.Beep(1000,500)

        self.msgbox.config(state=DISABLED)
        
        self.master.after(500, self.refresh_message)
    
    def send_message(self ):
        
        self.msgbox.config(state=NORMAL)
        message = self.msginput.get()
        self.msginput.delete(0, END)


        
        f = open('msgbuffer.txt', 'r+')
        username = self.username_txt.get()
        messages = f.readlines()
        mailboxSize = len(messages)
        msg_to_send = '%s:%s' % (username, message)
        f.write( msg_to_send )
        f.write('\n')
        
        f.close()
        if mailboxSize > 0 :
            self.msgbox.delete(1.0, END)
            self.msgbox.insert(END, "".join(messages) + msg_to_send)

        self.msgbox.config(state=DISABLED)

        

        
        
        

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
