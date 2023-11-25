from tkinter import *
def click():
    print("THANK'S FOR CLICKING")
windows = Tk()
windows.title("TEST 4")
button = Button(windows,text="click me !",command=click,fg="black",font=('Comic Sans',40),bg="pink",relief=RAISED,bd=20)
button.pack()
windows.mainloop()