from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox as mb
from tkinter import filedialog
import tkinter.scrolledtext as tks
from csv import DictReader
import _thread
import login
import socket
import json
import account


counter = 1



def main_loop(username):

    def add_all_users_to_list():
        db = mysql.connect(host='localhost',user='root',passwd='deep',database='login_app')
        c = db.cursor()
        c.execute(f'select name from log_details')
        p = c.fetchall()
        for i in p:
            all_user_listbox.insert(END,i[0])

    


    def connect_with_server():
        global c
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        host = 'localhost'
        port = 5000
        c.connect((host,port))
        msg = {'username':username,'alert':'Online','message':'None'}
        c.send(str(msg).encode('utf-8'))
        global client
        client = c
        _thread.start_new_thread(recievingMessage, (c,) )



    def recievingMessage (c): 
        while True :
            msg=c.recv(2048).decode('ascii')
            j = msg.replace("'","\"")
            d = json.loads(j)
            print(d)
            if d['alert'] == 'Online':
                to_write = f'                                 {d["username"]} is Online'
                print(to_write)
                t = chat_text.get(1.0,END)
                chat_text.delete(1.0,END)
                chat_text.insert(INSERT,t+to_write+'\n')
                chat_text.yview('end')
                list_insert(d['user_list'])
            elif d['alert'] == 'Offline':
                to_write = f'                                 {d["username"]} is Offline'
                print(to_write)
                t = chat_text.get(1.0,END)
                chat_text.delete(1.0,END)
                chat_text.insert(INSERT,t+to_write+'\n')
                chat_text.yview('end')
                list_insert(d['user_list'])

            if d['message'] != 'None':
                to_write = f'{d["username"]} :- {d["message"]}'
                t = chat_text.get(1.0,END)
                chat_text.delete(1.0,END)
                chat_text.insert(INSERT,t+to_write+'\n')
                chat_text.yview('end')


            



    def list_insert(l):
        active_user_listbox.delete(0,END)
        for i in l:
            active_user_listbox.insert(END,i)
            


    def sendMessage (*args):
        msg = msg_entry.get()
        msg = str({'username':username,'alert':'None','message':msg})
        global c
        c.send(msg.encode('ascii'))
        


    

    def account_func():
        account.account_func(username)



    def menu_operate_func():
        global counter
        if counter%2 == 0:
            menu_func()
            counter += 1
        else:
            home_func()
            counter += 1





    def logout_func():
        f =open('isLog.txt',"w")
        to_write = 'Logged Off,'
        f.write(to_write)
        f.close()
        msg = {'username':username,'alert':'Offline','message':'None'}
        c.send(str(msg).encode('utf-8'))
        win.destroy()
        login.login()





    def about_func():
        mb.showinfo('About', 'This is an exclusive distribution of DeeChat created By Hardeep Singh. This application was designed to have group chats. This has features like sending messages, showing all users in database, showing all the active users, working in real-time, responsive, managing account settings, login, logout, register. Hope you like the application. Please share your feedbacks.')





    def user_l_func():
        global counter
        counter += 1
        menu_func()
        win.geometry('600x487')
        title_label.place(x=500,y=2)







    def menu_func():
        ## Log Bg
        log_bg.place(x=1000)
        log_img.place(x=1000)
        log_in_as.place(x=1000)
        name.place(x=1000)

        ## Menu Options
        menu_bg.place(x=1000)
        group_b.place(x=1000)
        user_l_b.place(x=1000)
        setting_b.place(x=1000)
        about_b.place(x=1000)
        logout_b.place(x=1000)

    def hide_list_func():
        win.geometry('450x487')
        title_label.place(x=350,y=2)



    def home_func():
        ## Log Bg
        log_bg.place(x=0,y=33)
        log_img.place(x=50,y=50)
        log_in_as.place(x=40,y=120)
        name.place(x=35,y=145)

        ## Menu Options
        menu_bg.place(x=0,y=32)
        group_b.place(x=10,y=200)
        user_l_b.place(x=5,y=250)
        setting_b.place(x=5,y=300)
        about_b.place(x=10,y=360)

        logout_b.place(x=10,y=410)



    bg = '#408080'

    win = Tk()
    win.geometry('450x487')
    win.resizable(0,0)
    win.title('DeeChat')

    Label(win, text='',bg=bg,width=450,font=('arial black',15,'bold'),relief='groove').pack()
    title_label = Label(win, text='DeeChat',bg=bg,fg='white',font=('arial black',12,'bold'))
    title_label.place(x=350,y=2)

    menu_img = PhotoImage(file='resources/menu.png')
    Button(win, image=menu_img,bg=bg,bd=0,command=menu_operate_func).place(x=8,y=7)





    ## Group Chat
    chat_text = tks.ScrolledText(win, height=18, width=47,font=('Cambria',13))
    chat_text.place(x=10,y=50)
    chat_text.yview('end')
    msg_entry = Entry(win, font=('Cambria',15),width=30)
    msg_entry.place(x=10,y=430)
    send_b = Button(win,fg='white',font=('arial black',10,'bold'),text='Send',bg=bg,width=8,command=sendMessage).place(x=354,y=427)


    ## User List
    hide_list = Button(win,fg='white',font=('arial black',10,'bold'),text='Hide User Lists',bg=bg,width=15,command=hide_list_func).place(x=450,y=427)




    ##Menu Bar

    menu_bg = Label(win, text='',bg=bg,width=15,font=('arial black',15,'bold'),relief='groove',height=16)
    log_bg = Label(win,bg=bg,width=30,height=9,relief='groove')
    login_img =PhotoImage(file='resources/login.png')
    log_img = Label(win,image=login_img,bg=bg)
    log_in_as = Label(win, text='Logged In As : ',bg=bg,font=('',13),fg='white')
    name = Label(win, text=username,bg=bg,font=('',10,'bold'),fg='white')
##    if len(username) > 25:
##        name['font'] = ('',9,'bold')
    mail_img = PhotoImage(file='resources/chat-4-24.png')
    group_b = Button(win, image=mail_img, bg=bg,bd=0,text=' Group Chat',compound='left',fg='white',font=('arial black',10,'bold'),command=menu_operate_func)
    mul_mail_img = PhotoImage(file='resources/user-4-24.png')
    user_l_b = Button(win, image=mul_mail_img, bg=bg,bd=0,text=' User Lists',compound='left',fg='white',font=('arial black',10,'bold'),command=user_l_func)
    setting_img = PhotoImage(file='resources/camera-settings-icon-white-300x300.png')
    setting_b = Button(win, image=setting_img, bg=bg,bd=0,text=' Account Settings',compound='left',fg='white',font=('arial black',10,'bold'),command=account_func)
    about_img = PhotoImage(file='resources/about.png')
    about_b = Button(win, image=about_img, bg=bg,bd=0,text=' About',compound='left',fg='white',font=('arial black',10,'bold'),command=about_func)
    logout_img = PhotoImage(file='resources/logout-24.png')
    logout_b = Button(win, image=logout_img, bg=bg,bd=0,text=' Log Out',compound='left',fg='white',font=('arial black',10,'bold'),command=logout_func)


    ## User List
    Label(win, bg=bg, width=14, text='All Users', fg='White',font=('Cambria',13)).place(x=460,y=50)
    all_user_listbox = Listbox(win, width=14, height=7,font=('Cambria',13))
    all_user_listbox.place(x=460,y=75)
    Label(win, bg=bg, width=14, text='Active Users', fg='White',font=('Cambria',13)).place(x=460,y=250)
    active_user_listbox = Listbox(win, width=14, height=6,font=('Cambria',13))
    active_user_listbox.place(x=460,y=275)



    connect_with_server()
    add_all_users_to_list()
    

    def on_closing():
        res = mb.askyesnocancel('Exit','Do you want to logout and Exit?')
        if res == True:
            f =open('isLog.txt',"w")
            to_write = 'Logged Off,'
            f.write(to_write)
            f.close()
            win.destroy()
            msg = {'username':username,'alert':'Offline','message':'None'}
            c.send(str(msg).encode('utf-8'))
            
        elif res == False:
            win.destroy()
            msg = {'username':username,'alert':'Offline','message':'None'}
            c.send(str(msg).encode('utf-8'))
            
            


    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()

##main_loop('Hardeep Singh')

