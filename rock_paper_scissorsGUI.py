import tkinter as tk
import random
from random import choice


def randomm(play):
    choiceee = ["Rock", "Paper", "Scissors"]
    rdmchc = random.choice(choiceee)
    if play == rdmchc:
         result = "It's a match/tie!"
    elif play == "Rock" and rdmchc == "Scissors" or \
         play == "Paper" and rdmchc == "Rock" or \
         play == "Scissors" and rdmchc == "Paper":
         result = "You win!"
    else:
         result = "You loose, nigga"

    result_label.config(text = f"Computer chose: {rdmchc}\nResult:{result}")

mainwindow = tk.Tk()
mainwindow.title("Rock Paper Scissors Game")
mainwindow.geometry("400x400")
textfield = tk.Label(mainwindow, text="Choose between: ")
textfield.pack()
button1 = tk.Button(mainwindow, text="Rock", command=lambda: randomm("Rock"))
button1.pack(pady=10)
button2 = tk.Button(mainwindow, text="Paper", command=lambda: randomm("Paper"))
button2.pack(pady=10)
button3 = tk.Button(mainwindow, text="Scissors", command=lambda: randomm("Scissors"))
button3.pack(pady=10)
result_label = tk.Label(mainwindow, text="")
result_label.pack(pady=10)


mainwindow.mainloop()