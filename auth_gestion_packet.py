from hash import Hash
from my_socket import My_socket 
from get_account import Get_account
from threading import Thread
import world_gestion_packet
import time
from interface import Interface



class Auth_gestion_packet():

    def __init__(self,adrresse,ndc):
        Thread(None,).start()
        self.interface = Interface()
        self.my_socket = My_socket(adrresse,self.interface)
        self.hash = Hash()
        get_account = Get_account(ndc)
        self.account_data = get_account.get_data()
        self.th1 = True
        self.packet()
        Thread(None,self.packet).start()
        
    def packet(self):
        i = 0
        while self.th1 == True:
            i += 1
            if i == 10:
                break
            msg = self.my_socket.recv_msg()
            for ms in msg.split("\x00"):
                if ms != "":
                    i = 0
                    Thread(None,self.auth_packet(ms)).start()
                    
                    
                    
                
            
            
    
    def auth_packet(self,msg):
        #first packet sent by the server to encrypt the password 
            if msg[0:2] == "HC":
                self.my_socket.send_packet("1.31.2")
                self.my_socket.send_packet(self.account_data[0]+"\n"+ self.hash.crypt_password(self.account_data[1],msg[2:]))
                self.my_socket.send_packet("Af")
            #Al"xx" = error (ban,bad pass...) xx = cause of the error, and deco
            elif msg[0:2] == "Al":
                if msg[2:4] == "Ef":
                    print("Password incorrect")
                elif msg[2:4] == "Eb":
                    print("Account ban")
                elif msg[2:4] == "Ev":
                    print("bad version... version needed : "+msg[4:])
                elif msg[2:4] == "Ek":
                    date = msg[4:].split("|")
                    print(f"votre compte est banni {date[0]} jour(s) {date[1]} heure(s) {date[2]} minute(s)") 
                if msg[2:4] != "K0":
                    self.th1 = False 
                    self.my_socket.my_socket.close()             
            #client send the list of servers available  
            elif msg[:2] == "AQ":
                pass
                #send this to receive the servers on which we have a character
                #can be sent all the time when choosing the server 
                self.my_socket.send_packet("Ax")
            #list of servers with a character 
            elif msg[0:3] == "AxK":
                #serveurs = msg[4:].split("|")         #split the list of the server_id,nb_character
                #id_serv = serveurs[1].split(",")[0]   #Split the server_id of character 
                self.my_socket.send_packet("AX"+self.account_data[2])        #Connect to the server with the id = id_serv 
            elif msg[0:3] == "AXK": # Need to change the ip of the socket to be connected to the world serveur(Actualy connecter to the auth)
                self.th1 = False
                data = msg[3:].replace("\x00","")
                self.my_socket.disconnecte()
                world_gestion_packet.World_gestion_packet((self.hash.decrypt_IP(data[:8]),5555),data[11:],self.account_data[3],self.interface)
            elif msg[0:2] == "AX":
                if msg[2:4]:
                    print("Impossible to connect to this server because you are not sub")    
                
            
if __name__ == "__main__":
    fr = Auth_gestion_packet(("34.251.172.139",5555),"nomDeCompte")

    

    