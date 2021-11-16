from tkinter import *
root=Tk()
root.geometry('800x600+400+100')
root.configure(bg='light blue')
root.title("TYPING SPEED ")
def next():
    nx = Tk()
    nx .geometry('800x600+400+100')
    nx.configure(bg='light blue')
    nx.title('typing speed test')
################################label method
    fontLabel = Label(root, text='SIGNUP ', font=('fontial', 35, 'italic bold'), fg='white', bg='light blue')
    fontLabel.place(x=600, y=10)

    fontLabel = Label(root, text='PLEASE ENTER DETAILS', font=('fontial', 25, 'bold'), fg='white', bg='light blue')
    fontLabel.place(x=500, y=90)

    fontLabel = Label(root, text='USERNAME:\n\nPASSWORD:\n\nEMAIL ID:', font=('fontial', 25, 'italic bold'), fg='black',
                      bg='light blue')
    fontLabel.place(x=300, y=200)

    ############################button method
    b1 = Button(root, text='ENTER', fg='red', font=('fontial', 25, 'italic bold'))
    b1.place(x=600, y=600)

    b2 = Button(root, text='BACK <-', fg='red', font=('fontial', 10, 'italic bold'))
    b2.place(x=10, y=20)

    ######################################entry method
    wordEntry = Entry(root, font=('fontial', 25, 'italic bold'), fg='black', bg='white', bd=10)
    wordEntry.place(x=530, y=200)

    wordEntry = Entry(root, font=('fontial', 25, 'italic bold'), fg='black', bg='white', bd=10)
    wordEntry.place(x=530, y=280)

    wordEntry = Entry(root, font=('fontial', 25, 'italic bold'), fg='black', bg='white', bd=10)
    wordEntry.place(x=530, y=360)



fontLabel=Label(root,text='LOGIN FORM',font=('fontial',35,'italic bold'),fg='white',bg='light blue')
fontLabel.place(x=500,y=10)

fontLabel=Label(root,text='PLEASE ENTER DETAILS',font=('fontial',25,'bold'),fg='white',bg='light blue')
fontLabel.place(x=450,y=100)

fontLabel=Label(root,text='USERNAME:\n\nPASSWORD: ',font=('fontial',25,'italic bold'),fg='black',bg='light blue')
fontLabel.place(x=300,y=200)


b1=Button(root,text='ENTER',fg='red',font=('fontial',20,'italic bold'))
b1.place(x=570,y=450)

b2=Button(root,text='REGISTER',fg='red',font=('fontial',10,'italic bold'),command=next)
b2.place(x=1200,y=20)



wordEntry=Entry(root,font=('fontial',25,'italic bold'),fg='black',bg='white',bd=10)
wordEntry.place(x=530,y=200)

wordEntry=Entry(root,font=('fontial',25,'italic bold'),fg='black',bg='white',bd=10)
wordEntry.place(x=530,y=280)
root.mainloop()





