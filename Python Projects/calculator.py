from tkinter import *

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""
    
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

def clear():
    global equation_text

    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Python Calculator")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

Label(window,
      textvariable=equation_label,
      font=("consolas", 20),
      bg="white",
      width=24,
      height=2).pack()

frame = Frame(window)
frame.pack()

Button(frame,
       text=1,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(1)).grid(row=0, column=0)

Button(frame,
       text=2,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(2)).grid(row=0, column=1)

Button(frame,
       text=3,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(3)).grid(row=0, column=2)

Button(frame,
       text=4,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(4)).grid(row=1, column=0)

Button(frame,
       text=5,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(5)).grid(row=1, column=1)

Button(frame,
       text=6,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(6)).grid(row=1, column=2)

Button(frame,
       text=7,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(7)).grid(row=2, column=0)

Button(frame,
       text=8,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(8)).grid(row=2, column=1)

Button(frame,
       text=9,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(9)).grid(row=2, column=2)

Button(frame,
       text=0,
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(0)).grid(row=3, column=0)

Button(frame,
       text="+",
       height=4,
       width=9,
       font=35,
       command=lambda: button_press("+")).grid(row=0, column=3)

Button(frame,
       text="-",
       height=4,
       width=9,
       font=35,
       command=lambda: button_press("-")).grid(row=1, column=3)

Button(frame,
       text="*",
       height=4,
       width=9,
       font=35,
       command=lambda: button_press("*")).grid(row=2, column=3)

Button(frame,
       text="/",
       height=4,
       width=9,
       font=35,
       command=lambda: button_press("/")).grid(row=3, column=3)

Button(frame,
       text="=",
       height=4,
       width=9,
       font=35,
       command=equals).grid(row=3, column=2)

Button(frame,
       text=".",
       height=4,
       width=9,
       font=35,
       command=lambda: button_press(".")).grid(row=3, column=1)

Button(window,
       text="clear",
       height=4,
       width=12,
       font=35,
       command=clear).pack()

window.mainloop()