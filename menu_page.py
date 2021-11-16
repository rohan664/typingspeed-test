from  tkinter import  *
from tkinter import ttk
from typing_course import course
from tricks import tricks
from  about_us import about_us
from search import search
import webbrowser
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer




class menu_form():
        def __init__(self,root):
            self.root=root
            self.root.title("Menu_page")
            self.root.geometry("700x500+300+100")
            root.configure(bg="#ff0066")

            headline = Label(root, text="TYPINGTEST", font=("times new roman", 30, "bold"), fg="white", bg="#ff0066")
            headline.place(x=10, y=10)

            headline1 = Label(root, text=".com", font=("times new roman", 25, "bold"), fg="white", bg="#ff0066")
            headline1.place(x=280, y=15)

            course = Button(root, text="Typing Course", command=course_details,font=("times new roman", 15, "bold"), fg="white", bg="#b30047",height=1,width=20)
            course.place(x=250, y=100)

            keys = Button(root, text="Typing Keys",command=Tricks_page, font=("times new roman", 15, "bold"), fg="white", bg="#b30047",height=1,width=20)
            keys.place(x=250, y=170)

            about_us = Button(root, text="About us ",command=abt, font=("times new roman", 15, "bold"), fg="white", bg="#b30047",height=1,width=20)
            about_us.place(x=250, y=240)

            blog = Button(root, text="Search ",command=search_method, font=("times new roman", 15, "bold"), fg="white", bg="#b30047", height=1, width=20)
            blog.place(x=250, y=310)


            '''video = Button(root, text="video",command=PlayVideo, font=("times new roman", 15, "bold"), fg="white",
                          bg="#b30047", height=1, width=20)
            video.place(x=250, y=380)'''

            enquiry=Button(root,text="CONTACT US : supporttest123@gmail.com",command=mail,font=("times new roman", 15, "bold"),fg="white", bg="#ff0066",activebackground="#ff0066")
            enquiry.place(x=10,y=400)

def mail():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=shreyasdesai3013")



def course_details():
    type_course = Tk()
    app = course(type_course)
    type_course.mainloop()

def Tricks_page():
    tricky = Toplevel()
    app = tricks(tricky)
    tricky.mainloop()

def abt():
    about = Toplevel()
    app = about_us(about)
    about.mainloop()

def search_method():
    search_box = Toplevel()
    app = search(search_box)
    search_box.mainloop()


def PlayVideo():
    video_path = "C:\\Users\\rohit desai\\PycharmProjects\\helloword\\typing_video.mp4"
    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
    if val != 'eof' and audio_frame is not None:
        # audio
        img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    menu=Tk()
    app=menu_form(menu)
    menu.mainloop()
