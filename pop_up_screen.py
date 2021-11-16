from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
import mysql.connector
from menu_page import menu_form
import webbrowser
import re



import os



class pop_up():
    def __init__(self,root):
        self.root=root
        self.root.title("User_imformation")
        self.root.geometry("700x500+300+100")
        root.configure(bg="#ff1a75")

        headline  = Label(root, text="PERSONAL INFORMATION", font=("times new roman", 25, "bold"), fg="white", bg="#ff1a75")
        headline.place(x=170, y=10)

        name = lbl = Label(root, text="NAME :", font=("times new roman", 20, "bold"), fg="white", bg="#ff1a75")
        name.place(x=80, y=100)

        phone_number = lbl = Label(root, text="PHONE NO.:", font=("times new roman", 20, "bold"), fg="white", bg="#ff1a75")
        phone_number.place(x=80, y=240)

        email = lbl = Label(root, text="EMAIL :", font=("times new roman", 20, "bold"), fg="white", bg="#ff1a75")
        email.place(x=80, y=170)



        self.txtname = ttk.Entry(root, font=("times new roman", 20, "bold"))
        self.txtname.place(x=250, y=100, width=350)

        self.txtemailid = ttk.Entry(root, font=("times new roman", 20, "bold"))
        self.txtemailid.place(x=250, y=170, width=350)

        self.txtphoneno = ttk.Entry(root, font=("times new roman", 20, "bold"))
        self.txtphoneno.place(x=250, y=240, width=350)

        save_info = Button(root, text="SAVE", command=self.save_imformation,font=("times new roman", 13, "bold"), borderwidth=0, fg="white", bg="red",
                           activeforeground="white", activebackground="red")
        save_info.place(x=300, y=350, width=150, height=50)




    def save_imformation(self):
        if self.txtname.get() == "" or self.txtemailid.get() == "" or self.txtphoneno.get() == "":
            messagebox.showerror("error", "all field are required")
        elif len(str(self.txtphoneno.get()))<10 or len(str(self.txtphoneno.get()))>10:
            messagebox.showinfo("Phone","phone number should contain 10 digits")

        else:
            conn = mysql.connector.connect(host="Localhost", user="root", password="rohandesai664", database="typing_speed")
            my_cursor = conn.cursor()
            query = "insert into user_details (user_name,email,phone)values(%s,%s,%s)"
            value=(self.txtname.get(),self.txtemailid.get(),self.txtphoneno.get())
            my_cursor.execute(query,value)
            conn.commit()
            conn.close()


'''open_main = messagebox.askyesno("yesno", "Access only admin")
if open_main > 0:
    self.new_window = Toplevel(self.root)
    self.app = search(self.new_window, self.txtuser.get())
else:
    if not open_main:
        return'''

if __name__ == '__main__':
    show=Tk()
    app = pop_up(show)
    show.mainloop()
    import main_form