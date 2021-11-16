'''from tkinter import *
import random
from tkinter import messagebox
from pop_up_screen import pop_up
from menu_page import menu_form
import webbrowser
import mysql.connector
words = ["Rahul is good boy.", 'Salad is for rabbits.', 'Our school is good.', 'Cats hate water.',
         "Does she live in Paris?", "The quick brown fox jumps.",
         " The phrase is commonly in practice"]

def pop():
    show = Tk()
    app = pop_up(show)
    show.mainloop()


def menu():
    menu = Tk()
    app = menu_form(menu)
    menu.mainloop()


def certificate_link():
 f = open("mypdf.pdf")
   # f.close()
 webbrowser.open("mypdf.pdf")


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
            accuracy = 0
            timeleft = 60
            miss = 0
            timelabelcount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
        gameplaydetail.configure(text="WPM={} |accuracy={}".format(WPM, accuracy))

def startGame(event):
    global timeleft, score, miss, accuracy, WPM
    if (timeleft == 60):
        time()
    gameplaydetail.configure(text="")
    if (wordEntry.get() == wordLabel['text']):
        WPM += 5
        accuracy += 10
        scoreLabelCount.configure(text=WPM)
        scoreLabelCount.configure(text=accuracy)


    else:
        miss += 1
        print("miss :", miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, END)


def save_information():
    conn = mysql.connector.connect(host="Localhost", user="root", password="rohandesai664", database="typing_speed")
    my_cursor = conn.cursor()
    query = ("insert into result(wpm,accuracy) values(%s,%s)")
    value = (WPM, accuracy)
    my_cursor.execute(query, value)
    row = my_cursor.fetchone()
    conn.commit()
    conn.close()
    messagebox.showinfo("save", "value is stored")


class start:
    def __init__(self,root):
        self.root = root
        self.root.title("User_imformation")
        self.root.geometry("700x500+300+100")
        root.configure(bg="#ff1a75")
        score = 0
        timeleft = 60
        miss = 0
        WPM = 0
        accuracy = 0
        fontLabel = Label(root, text='ALL THE BEST FOR YOUR TEST', font=('arial', 35, 'italic bold'), fg='#0f0f3e',
                          bg="#6666ff")
        fontLabel.place(x=330, y=10)
        random.shuffle(words)

        wordLabel = Label(root, text=words[0], font=('fontial', 40, 'italic bold'), fg='black', bg='white')
        wordLabel.place(x=400, y=300)

        gameplaydetail = Label(root, text='Fill The Details And Then Enter ', font=('fontial', 20, 'italic bold'),
                               fg='black',
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

        menu_button = Button(root, text='MENU', command=menu, fg='#00e6e6', font=('fontial', 20, 'italic bold'),
                             height=1,
                             width=10, bg="#1a1aff", background="#1a1aff", activebackground="#1a1aff")
        menu_button.place(x=1150, y=20)

        personal_info = Button(root, text='DETAILS', command=pop, fg='#00e6e6', font=('fontial', 20, 'italic bold'),
                               height=1,
                               width=10, bg="#1a1aff", activebackground="#1a1aff")
        personal_info.place(x=1150, y=80)

        certificate = Button(root, text='CERTIFICATE', command=certificate_link, fg='#00e6e6',
                             font=('fontial', 20, 'italic bold'), height=1, width=10, bg="#1a1aff",
                             activebackground="#1a1aff")
        certificate.place(x=1150, y=140)

        save = Button(root, text='SAVE', command=save_information, fg='#00e6e6', font=('fontial', 20, 'italic bold'),
                      height=1,
                      width=10, bg="#1a1aff", activebackground="#1a1aff")
        save.place(x=550, y=600)

        ######################################entry method
        wordEntry = Entry(root, font=('fontial', 35, 'italic bold'), fg='black', bg='white', bd=10, justify="center")
        wordEntry.focus_set()
        wordEntry.place(x=400, y=400)
        wordEntry.focus_set()


if __name__ == '__main__':
    bind("<Return>", startGame)
    ro'''

