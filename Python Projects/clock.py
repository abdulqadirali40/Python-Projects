from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    date_string = strftime("%A")
    date_label.config(text=date_string)

    day_string = strftime("%B %d, %Y")
    day_label.config(text=day_string)

    window.after(1000, update)

window = Tk()
window.title("Python Clock")

time_label = Label(window, font=("Arial", 50))
time_label.pack()

date_label = Label(window, font=("Arial", 30))
date_label.pack()

day_label = Label(window, font=("Arial", 30))
day_label.pack()

update()

window.mainloop()