from pop_up_screen import pop_up
from menu_page import menu_form
import webbrowser
import mysql.connector
from pdf_viewer import create_pdf
import os
from  login import  *
import  login


words = ["Rahul is good boy.", 'Salad is for rabbits.', 'Our school is good.', 'since I can see you, I am better.',
         "Does she live in Paris?", "The quick brown fox jumps.","Although he was wealthy, he was still unhappy",
         " The phrase is commonly in practice","The train leaves every morning at 18 AM","Even though they were millionaires,they drive old cars"]


def time():
    global timeleft, score, miss, accuracy, WPM
    if (timeleft > 0):
        timeleft -= 1
        timelabelcount.configure(text=timeleft)
        timelabelcount.after(1000, time)
    else:
        rr = messagebox.askretrycancel("Notification", "FOR PLAY AGAIN HIT ENTER BUTTON ")
        if (rr == True):
            WPM = 0
            score = 0
            timeleft = 60
            miss = 0
            timelabelcount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
        gameplaydetail.configure(text="WPM={} |score={}".format(WPM, score))


def startGame(event):
    global timeleft, score, miss, accuracy, WPM
    if (timeleft == 60):
        time()
    gameplaydetail.configure(text="")
    if (wordEntry.get() == wordLabel['text']):
        WPM += (130/5)-miss
        score += 10
        scoreLabelCount.configure(text=WPM)
        scoreLabelCount.configure(text=score)


    else:
        miss += 1

    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, END)


def pop():
    show = Tk()
    app = pop_up(show)
    show.mainloop()


def menu():

    menu = Tk()
    app = menu_form(menu)
    menu.mainloop()



def certificate_link():
    create_pdf()
    webbrowser.open("mypdf.pdf")


def save_information():


    conn = mysql.connector.connect(host="Localhost", user="root", password="rohandesai664", database="typing_speed")
    my_cursor = conn.cursor()
    query = ("update register set wpm=%s ,accuracy=%s ")
    value = (WPM, score)
    my_cursor.execute(query, value)
    row = my_cursor.fetchone()
    conn.commit()
    conn.close()

    messagebox.showinfo("save", "value is stored")


from tkinter import *
import random
from tkinter import messagebox

root = Tk()

root.geometry('1400x800+0+0')
root.configure(bg='light blue')
root.title('TYPING SPEED TEST')
bg = PhotoImage(file="gameimage.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)
####################################################### Variable
score = 0
timeleft = 60
miss = 0
WPM = 0
accuracy = 0
################################label method
fontLabel = Label(root, text='ALL THE BEST FOR YOUR TEST', font=('arial', 35, 'italic bold'), fg='#0f0f3e',
                  bg="#6666ff")
fontLabel.place(x=330, y=10)
random.shuffle(words)

wordLabel = Label(root, text=words[0], font=('fontial', 25, 'italic bold'), fg='black', bg='white')
wordLabel.place(x=400, y=330)

gameplaydetail = Label(root, text='Hit Enter to Start Test ', font=('fontial', 20, 'italic bold'), fg='black',
                       bg='#99ccff')
gameplaydetail.place(x=480, y=500)

timelabel = Label(root, text='time left:', font=('fontial', 25, 'italic bold'), fg='#0f0f3e', bg='#6666ff')
timelabel.place(x=100, y=180)

timelabelcount = Label(root, text=timeleft, font=('fontial', 25, 'italic bold'), fg='#0f0f3e', bg='#6666ff')
timelabelcount.place(x=250, y=180)

scoreLabel = Label(root, text='score:', font=('fontial', 25, 'italic bold'), fg='#0f0f3e', bg='#6666ff')
scoreLabel.place(x=100, y=250)

scoreLabelCount = Label(root, text=score, font=("fontial", 25, 'italic bold'), fg='#0f0f3e', bg='#6666ff')
scoreLabelCount.place(x=200, y=250)

menu_button = Button(root, text='MENU', command=menu, fg='#00e6e6', font=('fontial', 20, 'italic bold'), height=1,
                     width=10, bg="#1a1aff", background="#1a1aff", activebackground="#1a1aff")
menu_button.place(x=1150, y=20)

personal_info = Button(root, text='CERTIFICATE', command=certificate_link, fg='#00e6e6', font=('fontial', 20, 'italic bold'), height=1,
                       width=10, bg="#1a1aff", activebackground="#1a1aff")
personal_info.place(x=1150, y=80)


save = Button(root, text='SAVE', command=save_information, fg='#00e6e6', font=('fontial', 20, 'italic bold'), height=1,
              width=10, bg="#1a1aff", activebackground="#1a1aff")
save.place(x=550, y=600)

######################################entry method
wordEntry = Entry(root, font=('fontial', 40, 'italic bold'), fg='black', bg='white', bd=7, justify="center")
wordEntry.focus_set()
wordEntry.place(x=400, y=400)
wordEntry.focus_set()
####################################
root.bind("<Return>", startGame)
root.mainloop()

