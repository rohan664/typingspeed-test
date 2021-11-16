from tkinter import *

class lesson3():
    def __init__(self,root):
        self.root=root
        self.root.title("Lesson3")
        self.root.geometry("1000x900+250+5")
        root.configure(bg="#00ff00")

        headline = Label(root, text="SYMBOLS AND NUMBER KEY", font=("times new roman", 20, "bold"), fg="black",
                         bg="#00b300")
        headline.place(x=300, y=10)

        information = Label(root, text="--Let's Learn Symbols-- \nTouch typing isn't just about typing letters and numbers; \nthere are many special characters that\n you will want to use when typing, !You already use many of them daily \nsuch as question and exclamation marks, or even the \ncharacters used in a web address such as (http://www...) or email\n (symbols_useful@needed.com).Some are used for professional reasons \nsuch as mathematical characters (+-*=) or coding symbols \n{Message = Touch + Typist;}.We'll cover these in the next\n four lessons, so let's get started ",
                            font=("times new roman", 20, "bold"), fg="black", bg="#00b300")
        information.place(x=80, y=80)

        information = Label(root,
                            text="--How to Use the Numeric Keypad-- \nThe numeric keypad is another way to enter numbers using\n touch typing. It is located on the right-hand side of most\n keyboards and is the most efficient way to enter longer series \nof numbers.\nIn this lesson, I'm going to show you how to use the NumPad effectively.\nTIP! When using the the numpad to enter numbers, make sure \nthat the NumLock is enabled.",
                            font=("times new roman", 20, "bold"), fg="black", bg="#00b300")
        information.place(x=80, y=400)



if __name__ == '__main__':
    less3=Tk()
    app=lesson3(less3)
    less3.mainloop()