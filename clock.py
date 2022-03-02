import datetime as dt
from tkinter import *
from tkinter.font import *
from time import strftime

root = Tk()

#create label
root.title("NEON GENESIS CLOCK")
#puts it on the screen
bg = PhotoImage(file="clockdemo.png")
can = Canvas(root, width=800, height=500, background='black')
can.pack(fill="both", expand=True)
can.create_image(0,0, image=bg, anchor='nw')

#magi text
can.create_text(400,450, text="Powered by the MAGI", font=('times',15), fill='red')

#clock part
clock = Label(root, font =('Times',65), background='black', foreground='red')
clock.place(x=300,y=220)

#date
date = strftime('%x')
can.create_text(650,350, text=date, font=('times',45), fill='red')

def time():
    currTime = strftime('%I:%M:%S %p')
    clock.config(text = currTime)
    clock.after(200, time)

time()
root.mainloop()
