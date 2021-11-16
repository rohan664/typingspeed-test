from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import  messagebox
import mysql.connector

class Register():
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()



        self.bg=ImageTk.PhotoImage(file="register background.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=300,y=60,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="white",bg="black")
        register_lbl.place(x=20,y=20)

        #----------------------------------------------------------------------

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="black",fg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email-ID",font=("times new roman",15,"bold"),bg="black",fg="white")
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","your birth place","your bestfriend name","your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370 ,y=270, width=250)

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black",fg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        comfirm_pswd = Label(frame, text=" Comfirm Password", font=("times new roman", 15, "bold"), bg="black",fg="white")
        comfirm_pswd.place(x=370, y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_pswd.place(x=370, y=340, width=250)

        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Term And Condition",font=("times new roman", 15, "bold"), bg="black",fg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        img=Image.open(r"register now.jpeg")
        img=img.resize((200,150),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="black",activebackground="black")
        b1.place(x=15,y=420,width=300)

        img1 = Image.open(r"login now.png")
        img1 = img1.resize((200, 70), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", bg="black",activebackground="black")
        b1.place(x=350, y=460, width=300)

    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()==""or self.var_securityQ.get()=="select":
            messagebox.showerror("error","all field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and comfirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree our term and condition")
        else:
            conn=mysql.connector.connect(host="Localhost",user="root",password="rohandesai664",database="typing_speed")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exits, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                      ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucess","Register Sucessfully")










if __name__ == '__main__':
    root=Tk()
    app=Register(root)
    root.mainloop()