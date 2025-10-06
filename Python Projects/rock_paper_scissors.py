from tkinter import *
import random

def logic(player, computer):
    if player == computer:
        return "It's tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Won!"
    else:
        return "You Lose!"

def play_game(player):
    choices = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(choices)
    result = logic(player, computer)

    result_label.config(text=f"Player choose: {player}\nComputer choose: {computer}\n{result}")

def on_exit():
    print("Thanks For Playing!")
    window.destroy()

window = Tk()
window.title("Rock-Paper-Scissors")
window.geometry("300x400")

Label(window, text="Rock-Paper-Scissors", font=("Arial", 20)).pack(pady=10)

Button(window, text="Rock", font=("Arial", 15), width=10, command=lambda: play_game("Rock")).pack(pady=10)
Button(window, text="Paper", font=("Arial", 15), width=10, command=lambda: play_game("Paper")).pack(pady=10)
Button(window, text="Scissors", font=("Arial", 15), width=10, command=lambda: play_game("Scissors")).pack(pady=10)

result_label = Label(window, text="", font=("Arial", 15))
result_label.pack(pady=10)

Button(window, text="Exit", font=("Arial", 15), width=10, command=on_exit).pack(pady=10)

window.mainloop()