from tkinter import *
from  tkinter import  ttk
from PIL import ImageTk,Image
from tkinter import  messagebox
import  mysql.connector

class search():
    def __init__(self,root):
        self.root=root

        self.root.geometry('800x600+300+50')
        self.root.title("SEARCH FORM")
        root.configure(bg="#00ff55")

        self.search_name = ttk.Entry(root, font=("times new roman", 30, "bold"))
        self.search_name.place(x=250, y=10, width=400)

        img1 = Image.open(r"search photo1 (1).png")
        img1 = img1.resize((50,50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(root, image=self.photoimage1,command=self.search_text, borderwidth=0)
        b1.place(x=200, y=10)

        name = Label(root, text="Name", font=("times new roman", 20, "bold"), bg="#00ff55", fg="#003311")
        name.place(x=50, y=150)

        email = Label(root, text="Email", font=("times new roman", 20, "bold"), bg="#00ff55", fg="#003311")
        email.place(x=250, y=150)

        wpm = Label(root, text="WPM", font=("times new roman", 20, "bold"), bg="#00ff55", fg="#003311")
        wpm.place(x=500, y=150)

        accuracy = Label(root, text="Score", font=("times new roman", 20, "bold"), bg="#00ff55", fg="#003311")
        accuracy.place(x=650, y=150)

        Straight = Label(root,
                         text="-------------------------------------------------------------------------------",
                         font=("times new roman", 20, "bold"), bg="#00ff55", fg="#003311")
        Straight.place(x=50, y=180)

        blog = Button(root, text="Reset ", command=self.clear_btn, font=("times new roman", 15, "bold"), fg="white",
                      bg="black", height=1, width=20)
        blog.place(x=280, y=400)

    def search_text(self):

                if self.search_name.get() == "":
                    messagebox.showerror("Error", "please enter your name in search box ")
                else:
                    conn = mysql.connector.connect(host="Localhost", user="root", password="rohandesai664",
                                                   database="typing_speed")
                    my_cursor = conn.cursor()
                    query = ("select name,email,wpm,accuracy from register where name=%s")
                    value = (self.search_name.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()
                    self.result1 = Label(self.root, font=("times new roman", 15, "bold"), fg="#003311", bg="#00ff55")
                    self.result1.place(x=50, y=250)
                    self.result2 = Label(self.root, font=("times new roman", 15, "bold"), fg="#003311", bg="#00ff55")
                    self.result2.place(x=250, y=250)
                    self.result3 = Label(self.root, font=("times new roman", 15, "bold"), fg="#003311", bg="#00ff55")
                    self.result3.place(x=500, y=250)
                    self.result4 = Label(self.root, font=("times new roman", 15, "bold"), fg="#003311", bg="#00ff55")
                    self.result4.place(x=650, y=250)

                    conn.commit()
                    conn.close()
                    name,email,wpm,accuracy = row
                    self.result1['text'] = name
                    self.result2['text'] = email
                    self.result3['text'] = wpm
                    self.result4['text'] = accuracy

    def clear_btn(self):
        self.result1.config(text="")
        self.result2.config(text="")
        self.result3.config(text="")
        self.result4.config(text="")
        self.search_name.delete(0,"end")



if __name__ == '__main__':
    search_box=Tk()
    app=search(search_box)
    search_box.mainloop()





