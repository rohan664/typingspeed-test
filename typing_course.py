from tkinter import *
from PIL import ImageTk,Image
from lesson1 import lesson1
from  lesson2 import lesson2
from lesson3 import lesson3
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer




class course():
    def __init__(self,root):
        self.root=root
        self.root.title("Typing course")
        self.root.geometry("700x500+300+100")
        root.configure(bg="#b31aff")

        headline = Label(root, text="TYPING COURSES", font=("times new roman", 30, "bold"), fg="#440066",
                         bg="#b31aff")
        headline.place(x=170, y=10)

        lesson1 = Button(root, text="LESSON1 \n\nIntroduction and Initial test",command=chapter, font=("times new roman", 15, "bold"), fg="white", bg="#66004d",height=5, width=20,activebackground="#66004d")
        lesson1.place(x=40, y=100)

        lesson2 = Button(root, text="LESSON2 \n\nFocus on the home row",command=chapter1, font=("times new roman", 15, "bold"),fg="white", bg="#66004d", height=5, width=20, activebackground="#66004d")
        lesson2.place(x=400, y=100)

        lesson3 = Button(root, text="LESSON3 \n\n  Symbols and Number Key ",command=chapter2, font=("times new roman", 15, "bold"),fg="white", bg="#66004d", height=5, width=20, activebackground="#66004d")
        lesson3.place(x=200, y=300)

        video = Button(root, text="Watch Video",command=PlayVideo,font=("times new roman", 15, "bold"), fg="white", bg="#66004d", height=1, width=10,
                         activebackground="#66004d")
        video.place(x=550, y=450)

def chapter():
    less1 = Tk()
    app = lesson1(less1)
    less1.mainloop()

def chapter1():
        less2 = Toplevel()
        app = lesson2(less2)
        less2.mainloop()


def chapter2():
    less3 = Toplevel()
    app = lesson3(less3)
    less3.mainloop()

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
    type_course=Tk()
    app=course(type_course)
    type_course.mainloop()