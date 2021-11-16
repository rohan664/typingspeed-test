from tkinter import *


##############################root method
root=Tk()
root.geometry('800x600+400+100')
root.configure(bg='light blue')
root.title('typing speed test')
##root.iconbitmap('typingspeed.ico')

################################label method
fontLabel=Label(root,text='SIGNUP ',font=('fontial',35,'italic bold'),fg='white',bg='light blue')
fontLabel.place(x=600,y=10)

fontLabel=Label(root,text='PLEASE ENTER DETAILS',font=('fontial',25,'bold'),fg='white',bg='light blue')
fontLabel.place(x=500,y=90)

fontLabel=Label(root,text='USERNAME:\n\nPASSWORD:\n\nEMAIL ID:',font=('fontial',25,'italic bold'),fg='black',bg='light blue')
fontLabel.place(x=300,y=200)


############################button method
b1=Button(root,text='ENTER',fg='red',font=('fontial',25,'italic bold'))
b1.place(x=600,y=600)

b2=Button(root,text='BACK <-',fg='red',font=('fontial',10,'italic bold'))
b2.place(x=10,y=20)


######################################entry method
wordEntry=Entry(root,font=('fontial',25,'italic bold'),fg='black',bg='white',bd=10)
wordEntry.place(x=530,y=200)

wordEntry=Entry(root,font=('fontial',25,'italic bold'),fg='black',bg='white',bd=10)
wordEntry.place(x=530,y=280)

wordEntry=Entry(root,font=('fontial',25,'italic bold'),fg='black',bg='white',bd=10)
wordEntry.place(x=530,y=360)






root.mainloop()