import login
import main

f = open('isLog.txt',"r")
to_read = f.read(1024).split(',')
if to_read[0] == 'logged in':
    main.main_loop(to_read[1])
else:
    login.login()
