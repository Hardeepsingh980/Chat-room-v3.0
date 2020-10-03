#Used to seprate processes
import _thread
#Used For Connection
import socket
#Used For sending Data
import json

#Establishing Connection ----
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
host="localhost"
port=5000
server.bind((host,port))
server.listen(5)

clients=[]
clients_name = []

def connectNewClient(c):
     while True:
          try:
               #Recieving Data from Clients:
               msg = c.recv(2048).decode('utf-8')
               j = msg.replace("'","\"")
               d = json.loads(j)
               print(d)
               
               #Alerting If The Client Is Online Or Offline
               if d['alert'] == 'Online':
                    clients_name.append(d['username'])
               elif d['alert'] == 'Offline':
                    clients_name.pop(clients_name.index(d['username']))
                    clients.pop(clients.index(c))
               
               to_send_dict = str({'user_list':clients_name,'alert': d['alert'],'message': d['message'],'username':d['username']})
               sendToAll(to_send_dict)
          except:
               pass
         
               
               
               
          
          
def sendToAll(msg):
    for client in clients:
        client.send(msg.encode('utf-8')) 
        
while True:
     try:
         c,ad=server.accept()
         print('Connection Established')
         clients.append(c)
         _thread.start_new_thread(connectNewClient,(c,))
     except:
          continue
