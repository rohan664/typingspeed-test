from  tkinter import  *
from PIL import ImageTk,Image

class tricks():
    def __init__(self,root):
        self.root=root
        self.root.title("Trick")
        self.root.geometry("1000x800+250+5")
        root.configure(bg="#ff0066")

        headline = Label(root, text="TYPING TRICKS", font=("times new roman", 30, "bold"), fg="white",
                         bg="#ff0066")
        headline.place(x=350, y=10)

        information = Label(root, text="--Sitting posture for typing-- \n1. Sit straight and remember to keep your back straight.\n2. Keep your elbows bent at the right angle.\n3. Face the screen with your head slightly tilted forward.\n4. Keep at least 45 - 70 cm of distance between your eyes and the screen.\n5. Еxpose the shoulder, arm, and wrist muscles to the least possible strain.", font=("times new roman", 15, "bold"), fg="white",
                         bg="#ff0066")
        information.place(x=10, y=100)

        row=Label(root,text="----------------------------------------------------------------------",bg="#ff0066",font=("times new roman", 20, "bold"))
        row.place(x=10,y=290)

        information1 = Label(root,
                            text="--Home row position --\n position Curve your fingers a little and put them on the ASDF and JKL; \nkeys which are located in the middle row of the letter keys. \nThis row is called HOME ROW because you always start\n from these keys and always return to them.",
                            font=("times new roman", 15, "bold"), fg="white",
                            bg="#ff0066")
        information1.place(x=10, y=330)

        row=Label(root,text="----------------------------------------------------------------------",bg="#ff0066",font=("times new roman", 20, "bold"))
        row.place(x=10,y=490)

        information2 = Label(root,
                    text="--Finger Motion--\nLimit your hand and finger movement only to what is\n necessary to press a specific key.\n Keep your hands and fingers close to the base position. \nThis improves typing speed and reduces stress on the hands.",
                             font=("times new roman", 15, "bold"), fg="white",
                             bg="#ff0066")
        information2.place(x=10, y=530)

        img1 = Image.open(r"sitting_pos.jpeg")
        img1 = img1.resize((300, 200), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Label(root, image=self.photoimage1, borderwidth=0, bg="#730099",
                   activebackground="#730099")
        b1.place(x=650, y=100)

        img2 = Image.open(r"row_position.jpeg")
        img2 = img2.resize((300, 100), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        b1 = Label(root, image=self.photoimage2, borderwidth=0, bg="#730099",
                   activebackground="#730099")
        b1.place(x=650, y=330)

        img3 = Image.open(r"keyBoard_pos.jpeg")
        img3 = img3.resize((300, 150), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        b1 = Label(root, image=self.photoimage3, borderwidth=0, bg="#730099",
                   activebackground="#730099")
        b1.place(x=650, y=530)


if __name__ == '__main__':
    tricky = Tk()
    app = tricks(tricky)
    tricky.mainloop()