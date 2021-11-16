from tkinter import *
from PIL import ImageTk,Image

class about_us():
    def __init__(self,root):
        self.root = root
        self.root.title("About_Us")
        self.root.geometry("700x500+300+100")
        root.configure(bg="#ff1a75")

        headline = Label(root, text="ABOUT US", font=("times new roman", 30, "bold"), fg="#99003d", bg="#ff1a75")
        headline.place(x=225, y=1)

        img1 = Image.open(r"about_image.jpeg")
        img1 = img1.resize((600, 500), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Label(root, image=self.photoimage1, borderwidth=0)
        b1.place(x=50, y=45)


if __name__ == '__main__':
    about=Tk()
    app=about_us(about)
    about.mainloop()