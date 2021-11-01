from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from random import randint
from tkinter import messagebox

window = Tk()
window.title("Rock Paper Scissor")
window.configure(background="#3f184d")
#ttk.Frame(window, padding=(50,50,12,12))
#window.geometry('1300x600')

# Load images
image_rock_user = ImageTk.PhotoImage(Image.open("rock.png"))
image_paper_user = ImageTk.PhotoImage(Image.open("paper.png"))
image_scissor_user = ImageTk.PhotoImage(Image.open("scissor.png"))
image_rock_computer = ImageTk.PhotoImage(Image.open("com_rock.png"))
image_paper_computer = ImageTk.PhotoImage(Image.open("com_paper.png"))
image_scissor_computer = ImageTk.PhotoImage(Image.open("com_scissor.png"))

# Image Position lebeling
label_user = Label(window,image=image_scissor_user)
label_computer = Label(window,image=image_scissor_computer)
label_user.grid(row=1,column=0)
label_computer.grid(row=1,column=4)

# Showing scores
user_score = Label(window,text=0,font= ("arial",50,"bold"),bg="#3f184d", fg="white")
computer_score = Label(window,text=0,font= ("arial",50,"bold"),bg="#3f184d", fg="white")
user_score.grid(row=1,column=1)
computer_score.grid(row=1,column=3)

# Selecting side for player and computer
Label(window,text="PLAYER",font= ("arial",20,"bold"),bg="#3f184d", fg="#0ABDE3").grid(row=0,column=0)
Label(window,text="COMPUTER",font= ("arial",20,"bold"),bg="#3f184d", fg="#0ABDE3").grid(row=0,column=4)

# Showing Message of win or lose
final_message = Label(window,font=("arial",15,"bold"),text="Welcome :)",bg="#3f184d",fg="white")
final_message.grid(row=3,column=2)

#update message
def msg_update(x):
    final_message['text'] = x

#update score
def computer_score_update():
    score = int(computer_score['text'])
    score+=1
    computer_score['text'] = str(score)

def user_score_update():
    score = int(user_score['text'])
    score+=1
    user_score['text'] = str(score)

# Winning Condition
def win_check(player,computer):
    if player==computer:
        msg_update("It's a tie!")
    elif player == "rock" and computer == "scissor":
        msg_update("You win :)")
        user_score_update()
    elif player == "paper" and computer == "rock":
        msg_update("You win :)")
        user_score_update()
    elif player == "scissor" and computer == "paper":
        msg_update("You win :)")
        user_score_update()
    else:
        msg_update("You loose :(")
        computer_score_update()

# Update Picture and score with button pressing
choices = ["rock", "paper", "scissor"]
def choice_update(x):
    choice_computer = choices[randint(0,2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock_computer)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper_computer)
    else:
        label_computer.configure(image=image_scissor_computer)

    if x=="rock":
        label_user.configure(image=image_rock_user)
    elif x=="paper":
        label_user.configure(image=image_paper_user)
    else:
        label_user.configure(image=image_scissor_user)

    win_check(x,choice_computer)

#add Button
button_rock = Button(window, width=10, height=2, text="ROCK",
              bg="#FF3E4D", fg="white",font=("arial",15,"bold"),command=lambda:choice_update("rock")).grid(row=2,column=1)
button_paper = Button(window, width=10, height=2, text="PAPER",
              bg="#FAD02E", fg="white",font=("arial",15,"bold"),command=lambda:choice_update("paper")).grid(row=2,column=2)
button_scissor = Button(window, width=10, height=2, text="SCISSOR",
              bg="#0ABDE3", fg="white",font=("arial",15,"bold"),command=lambda:choice_update("scissor")).grid(row=2,column=3)

# Confirmation when closing
def on_close():
    response=messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        window.destroy()
window.protocol('WM_DELETE_WINDOW',on_close)

window.mainloop()