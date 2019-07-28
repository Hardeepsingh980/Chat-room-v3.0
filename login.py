from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as sql
import main
import _thread


    



def login():
    try:
        reg.destroy()
    except:
        pass
    global log
    log = Tk()
    log.title('Login')
    log.geometry('300x300+220+170')
    log.configure(bg='white')
    log.resizable(0,0)

    log_label = Label(log, text='Login', width=20, height=1, font=('Arial Black',20,'bold'))
    log_label.pack()

    u = Label(log, text='Username :', font=('Arial Black',14,'bold'),bg='white')
    u.place(x=10,y=50)
    
    user_entry = Entry(log, font=('Arial Black',10,'bold'),  width=25,bg='powder blue')
    user_entry.place(x=10, y=80)


    p = Label(log, text='Password :', font=('Arial Black',14,'bold'),bg='white')
    p.place(x=10,y=110)
    
    pass_entry = Entry(log,show='*', font=('Arial Black',10,'bold'),  width=25,bg='powder blue')
    pass_entry.place(x=10, y=140)

    resp = Label(log, text='',font=('Arial Black',10,'bold'),bg='white')
    resp.place(x=10, y=250)

    

    
    def log_func(*args):

        data_base = sql.connect(host='localhost',port=3306,user='root',passwd='deep',database='login_app')
        c = data_base.cursor()

        user = user_entry.get()
        password = pass_entry.get()

        try:
            c.execute(f'select Password from log_details where Username = "{user}" ')

            b = c.fetchall()

            for i in b:
                passw = i[0]

            if password == passw:
                c.execute(f'select name from log_details where Username= "{user}"')
                b = c.fetchall()[0][0]
                username_name = b
                resp.configure(text=f'Login Successful\n Welcome {b} ', fg='green')
                log.destroy()
                f = open('isLog.txt','w')
                to_write = 'logged in,'+b
                f.write(to_write)
                f.close()
                main.main_loop(b)

                    
                    
                    

                    


            else:
                resp.configure(text='Wrong Password', fg='red')
                

        except UnboundLocalError:
            resp.configure(text=f'Username {user} Does Not Exist', fg='red')


    submit = Button(log, text='Submit',font=('Arial Black',10,'bold'), width=14, bg='green', command=log_func,bd=0,fg='white')
    submit.place(x=10, y=180)

    Label(log, text='Dont\'t Have An Account.',bg='white').place(x=30,y=210)

    Button(log,text='Register',font=('',10,'underline'),bg='white',fg='blue',command=register).place(x=170,y=210)

    log.bind('<Return>', log_func)

    log.mainloop()






    




def register():
    try:
        log.destroy()
    except:
        pass

    
    
    global reg
    reg = Tk()
    reg.title('Register')
    reg.configure(bg='white')
    reg.geometry('300x300+220+170')
    reg.resizable(0,0)

    reg_label = Label(reg, text='Register',fg='black', width=20, height=1, font=('Arial Black',20,'bold'))
    reg_label.pack()


    n = Label(reg, text='Name :', font=('Arial Black',14,'bold'),bg='white')
    n.place(x=10,y=50)
    
    name_entry = Entry(reg, font=('Arial Black',10,'bold'),  width=25,bg='powder blue')
    name_entry.place(x=10,y=80)

    u = Label(reg, text='Username :', font=('Arial Black',14,'bold'),bg='white')
    u.place(x=10,y=110)
    
    user_entry = Entry(reg, font=('Arial Black',10,'bold'),  width=25,bg='powder blue')
    user_entry.place(x=10, y=140)


    p = Label(reg, text='New Password :', font=('Arial Black',14,'bold'),bg='white')
    p.place(x=10,y=170)
    
    pass_entry = Entry(reg,show='*', font=('Arial Black',10,'bold'),  width=25,bg='powder blue')
    pass_entry.place(x=10, y=200)


    def reg_func(*args):

        data_base = sql.connect(host='localhost',user='root',passwd='deep',database='login_app')
        c = data_base.cursor()

        name = name_entry.get().title()
        user = user_entry.get()
        password = pass_entry.get()

        if name != '' and user != '' and password != '':

            c.execute('select Username from log_details')

            l = c.fetchall()

            for i in l:
                if user == i[0]:
                    ex_t = True
                    break
                else:
                    ex_t = False
                    
            if ex_t == True:

                mb.showerror('Register',f'{user} Already Exist.')
            else:                
                c.execute(f'insert into log_details values("{name}","{user}","{password}","0.png")')


                data_base.commit()
                name_entry.delete(0, END)
                user_entry.delete(0, END)
                pass_entry.delete(0, END)
                global username_name
                username_name = name
                reg.destroy()
                f = open('isLog.txt','w')
                to_write = 'logged in,'+username_name
                f.write(to_write)
                f.close()
                main.main_loop(username_name)

                


        else:
            mb.showerror('Register','Please Fill All The Fields.')
        
        

        

    submit = Button(reg, text='Submit',font=('Arial Black',10,'bold'), width=14, bg='green', command=reg_func,bd=0,fg='white')
    submit.place(x=10, y=240)

    Label(reg, text='Already Had A Account.',bg='white').place(x=30,y=275)

    Button(reg,text='Log_In',font=('',10,'underline'),bg='white',fg='blue',command=login).place(x=170,y=270)

    reg.bind('<Return>', reg_func)


    reg.mainloop()



##register()


