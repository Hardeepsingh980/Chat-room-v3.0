import mysql.connector as mysql
from tkinter import *
from tkinter import messagebox as mb

def account_func(username):
    db = mysql.connect(host='localhost',user='root',passwd='deep',database='login_app')
    c = db.cursor()

    def change_info(arg):
        c.execute(f'select password from log_details where name = "{username}"')
        p = c.fetchone()[0]
        print(p)
        print(cur_pass.get(), 'done')

        if cur_pass.get() == p:
            req = req_pass.get()
            c.execute(f'update log_details set {arg} = "{req}" where name="{username}"')
            mb.showinfo('Done',f'{arg} Updated.\n Please Logout and login again to see changes.')
            db.commit()
        else:
            mb.showerror('Failed','Password Is Incorrect')

    def change_avatar():

        def set_av(no):
            av.destroy()
            no = str(no)
            c.execute(f'update log_details set avatar = "{no}.png" where name="{username}"')
            db.commit()
            c.execute(f'select avatar from log_details where name = "{username}"')
            avar_no = c.fetchone()[0]
            avatar = PhotoImage(file=f'avatars\\{avar_no}')
            av_button.configure(image=avatar)
            mb.showinfo('success','Avatar Changed.')
            pro.destroy()

            


        
        
        av = Toplevel()
        av.geometry('400x420')
        av.resizable(0,0)
        av.configure(bg=bg)

        Label(av, text='Choose Avatar',bg=bg,font=('Calibri Light',20,'bold'),fg='white').grid(row=0,columnspan=3)

        img_0 = PhotoImage(file='avatars\\0.png')
        Button(av,image=img_0,bg=bg,bd=0,command=lambda : set_av(0)).grid(row=1,column=0)

        img_1 = PhotoImage(file='avatars\\1.png')
        Button(av,image=img_1,bg=bg,bd=0,command=lambda : set_av(1)).grid(row=1,column=1)

        img_2 = PhotoImage(file='avatars\\2.png')
        Button(av,image=img_2,bg=bg,bd=0,command=lambda : set_av(2)).grid(row=1,column=2)

        img_3 = PhotoImage(file='avatars\\3.png')
        Button(av,image=img_3,bg=bg,bd=0,command=lambda : set_av(3)).grid(row=2,column=0)

        img_4 = PhotoImage(file='avatars\\4.png')
        Button(av,image=img_4,bg=bg,bd=0,command=lambda : set_av(4)).grid(row=2,column=1)

        img_5 = PhotoImage(file='avatars\\5.png')
        Button(av,image=img_5,bg=bg,bd=0,command=lambda : set_av(5)).grid(row=2,column=2)

        img_6 = PhotoImage(file='avatars\\6.png')
        Button(av,image=img_6,bg=bg,bd=0,command=lambda : set_av(6)).grid(row=3,column=0)

        img_7 = PhotoImage(file='avatars\\7.png')
        Button(av,image=img_7,bg=bg,bd=0,command=lambda : set_av(7)).grid(row=3,column=1)

        img_8 = PhotoImage(file='avatars\\8.png')
        Button(av,image=img_8,bg=bg,bd=0,command=lambda : set_av(8)).grid(row=3,column=2)

        av.mainloop()

    def del_func():
        res = mb.askquestion('Confirm', 'Are You Sure That You Want To Delete Your Account.',icon='error')
        if res == 'yes':
            c.execute(f'delete from log_details where name = "{username}"')
            db.commit()
        pro.destroy()
        

    def name_func(arg):
        name = Tk()
        name.geometry('250x200')
        name.title(f'Change {arg}')
        name.configure(bg=bg)

        Label(name, text=f'Change {arg}',font=('Calibri Light',20,'bold'),bg=bg,fg='white').pack()

        Label(name, text='Enter Your Current Password.',font=('Calibri Light',13),bg=bg,fg='white').place(x=5,y=40)

        global cur_pass
        cur_pass = Entry(name,font=('Calibri Light',10,'bold'),show='*')
        cur_pass.place(x=5,y=70)

        Label(name, text=f'Enter {arg} You Want To Set.',font=('Calibri Light',13),bg=bg,fg='white').place(x=5,y=100)

        global req_pass
        req_pass = Entry(name,font=('Calibri Light',10,'bold'))
        req_pass.place(x=5,y=130)

        Button(name, text='Apply Changes',bd=0,bg='White',fg='black',font=('Calibri Light',10,'bold'),command=lambda:change_info(arg)).place(x=50,y=170)

    
    

    bg = '#408080'
    
    pro = Toplevel()
    pro.geometry('325x425')
    pro.resizable(0,0)
    pro.title('Profile')
    pro.configure(bg=bg)

    c.execute(f'select avatar from log_details where name = "{username}"')

    avar_no = c.fetchone()[0]

    avatar = PhotoImage(file=f'avatars\\{avar_no}')

    av_button = Button(pro, image=avatar,bg=bg,bd=0,command=change_avatar)
    av_button.place(x=110,y=30)

    c.execute(f'select username from log_details where name = "{username}"')
    user = c.fetchone()[0]

    pencil = PhotoImage(file='resources\\pencil-32.png')

    Label(pro,text='@'+user,font=('Calibri Light',16),bg=bg,fg='white').place(x=90,y=170)


    Label(pro,text=username.title(),font=('Calibri Light',20,'bold'),bg=bg,fg='white').place(x=90,y=140)

    Label(pro, text= 'Change Name',font=('Calibri Light',20),bg=bg,fg='white').place(x=10,y=220)

    Button(pro, image=pencil,bg=bg,bd=0,command=lambda : name_func('Name'),fg='white').place(x=280,y=220)

    Label(pro, text= 'Change Username',font=('Calibri Light',20),bg=bg,fg='white').place(x=10,y=270)

    Button(pro, image=pencil,bg=bg,bd=0,command=lambda : name_func('Username'),fg='white').place(x=280,y=270)

    Label(pro, text= 'Change Password',font=('Calibri Light',20),bg=bg,fg='white').place(x=10,y=320)

    Button(pro, image=pencil,bg=bg,bd=0,command=lambda : name_func('Password'),fg='white').place(x=280,y=320)

    Label(pro, text= 'Delete Account',font=('Calibri Light',20),bg=bg,fg='white').place(x=10,y=370)

    delete = PhotoImage(file='resources\\delete-32.gif')

    Button(pro, image=delete,bg=bg,bd=0,command=del_func,fg='white').place(x=280,y=370)
    

    pro.mainloop()


##account_func('Hardeep Singh')
