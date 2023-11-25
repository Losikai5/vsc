from tkinter import *
def sumbit_button():
    username = entry_p.get()
    print("hello"+ "   " + username)
def delete():
    entry_p.delete(0,END)   
def backspace():
    entry_p.delete(len(entry_p.get())-1,END) 
         
    
windows = Tk()
entry_p = Entry(windows,font=("Comic Sons",40))
entry_p.pack(side=LEFT)
sumbit_button = Button(windows,font=("Comic Sons",20),text="sumbit",command=sumbit_button)
sumbit_button.pack(side=RIGHT)
entry_p.config(show="*")
delete = Button(windows,font=("Comic Sons",20),text="delete",command=delete)
delete.pack(side=RIGHT)
backspace = Button(windows,font=("Comic Sons",20),text="backspace",command=backspace)
backspace.pack(side=RIGHT)
windows.mainloop()