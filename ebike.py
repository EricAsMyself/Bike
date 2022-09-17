from itertools import count
from tkinter import *
from random import randint
from filelock import Timeout, FileLock

root = Tk()
root.configure(bg='black')
root.title('Bike')
root.geometry('320x240+10+20')

# Add image file
bg = PhotoImage(file = "Bike/Untitled.png")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x =-3, y = -3)
lab = Label(root, bg="#222", fg='white', font=('Arial', 50))
lab.pack()

def update():
    lab.place(relx = 0.4, rely = 0.65, anchor ='sw')
    lock = FileLock("Bike/MPH.txt.lock")
    with lock:
        f = open("Bike/MPH.txt", "r")
        MPHS = f.read()

    lab['text'] = str(MPHS)
    root.after(10, update) # run itself again after 1000 ms

# run first time
update()

root.mainloop()