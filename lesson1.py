from tkinter import *

class lesson1():
    def __init__(self,root):
        self.root=root
        self.root.title("Lesson1")
        self.root.geometry("1000x900+250+5")
        root.configure(bg="#e60000")

        headline = Label(root, text="INTRODUCTION AND INTIAL TEST", font=("times new roman", 20, "bold"), fg="white", bg="#990000")
        headline.place(x=250, y=10)

        information= Label(root, text="What is Touch Typing?\nTouch typing is a keyboarding technique used to help\n you type more accurately and efficiently without looking the keyboard.", font=("times new roman", 20, "bold"), fg="white",bg="#990000")
        information.place(x=60, y=80)

        information1 = Label(root,
                            text="It Begins With the Home Keys \nStop bouncing around the keyboard and find the best position for your fingers.\nThe Home Keys, also called the home row,\n are the keys A S D F and J K L.\n They're the starting point for touch typing and the home base for each finger.",
                            font=("times new roman", 20, "bold"), fg="white", bg="#990000")
        information1.place(x=30, y=200)

        information2 = Label(root,text="Position Your Left Hand..\n.Place your left hand on the keyboard, just like in the picture. \nStarting with your little finger on the A, place remaining left hand fingers \non the S, D and F keys.Let your thumb rest on the space bar.",
                            font=("times new roman", 20, "bold"), fg="white", bg="#990000")
        information2.place(x=60, y=380)

        information3 = Label(root,
text="Now, for Your Right Hand...\nPlace your right hand on the keyboard. \nStarting with the index finger, place your fingers on the J, K, L and keys.Again\n rest your thumb on the space bar.",
                             font=("times new roman", 20, "bold"), fg="white", bg="#990000")
        information3.place(x=30, y=520)


if __name__ == '__main__':
    less1=Tk()
    app=lesson1(less1)
    less1.mainloop()