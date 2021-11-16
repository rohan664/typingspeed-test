from tkinter import *
from  PIL import ImageTk,Image


class lesson2():
    def __init__(self,root):
        self.root=root
        self.root.title("Lesson2")
        self.root.geometry("1000x900+250+5")
        root.configure(bg="#d24dff")

        headline = Label(root, text="FOCUS ON THE HOME ROW", font=("times new roman", 20, "bold"), fg="white",
                         bg="#730099")
        headline.place(x=300, y=10)

        information = Label(root,text="Typing Speed: Practice Makes Perfect!\nDid you know that increasing your typing speed requires regular practice? \nIn addition to daily typing, try completing this six lesson course for extra training.\nIn lesson 2, we'll begin by reviewing the\n home keys and typing sentences that put emphasis on these keys.\nIn lessons 2 to 5, we'll type sentences using keys from the upper and lower\n extension rows; placing emphasis on one finger at a time.\nIn the last lesson, we'll focus on typing commonly used words \nand those that are often misspelled.",
                            font=("times new roman", 20, "bold"), fg="white", bg="#730099")
        information.place(x=30, y=80)

        img1 = Image.open(r"typing_image.png")
        img1 = img1.resize((800, 300), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 =Button(root, image=self.photoimage1, borderwidth=0)
        b1.place(x=100, y=380)






if __name__ == '__main__':
    less2=Tk()
    app=lesson2(less2)
    less2.mainloop()