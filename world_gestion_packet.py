
from my_socket import My_socket 
from threading import Thread
from character import Character


class World_gestion_packet():

    def __init__(self,adrresse,GUID,character_name,interface):
        self.character_name = character_name
        self.interface = interface
        self.my_socket = My_socket(adrresse,self.interface)
        self.GUID = GUID
        self.th1 = True
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
                    Thread(None,self.world_packet(ms)).start()
                    
    


    def world_packet(self,msg):
        if msg[:2] == "HG":
            self.my_socket.send_packet("AT"+self.GUID)
        elif msg[:4] == "ATK0":
            pass
            self.my_socket.send_packet("Ak0")
            self.my_socket.send_packet("AV")   
        elif msg[:3] == "AV0":
            self.my_socket.send_packet("Agfr")
            self.my_socket.send_packet("Ai"+"9MyRN8zsktslxxicT2")
            self.my_socket.send_packet("AL")
            self.my_socket.send_packet("Af")
        #packet qui contient le nom id_personnage lvl... besoin de id pour ce connecter a ce personnage
        elif msg[:3] == "ALK":
            msg_data = msg.split("ALK")
            msg_data = msg_data[1].split("|")[2:]
            msg_data = "".join(msg_data).split(";")
            for nb in range(len(msg_data)):
                if msg_data[nb] == self.character_name:
                    self.my_socket.send_packet("AS"+msg_data[nb-1])
                    self.my_socket.send_packet("Af")
                    print("\x00\x00\x00\x00\x00\x00")
                    
            #print("No character named " +self.character_name)
        elif msg[:2] == "al":
            self.my_socket.send_packet("GC1")
        elif msg[:3] == "ASK":
            info_perso = msg[3:].split("|")
            print(info_perso)                              
            self.character = Character(id_ = info_perso[1],pseudo = info_perso[2],lvl = info_perso[3],id_class = info_perso[4],sexe = info_perso[5],gfx = info_perso[6])
            self.interface.create_charater(self.character.gfx,self.character.pseudo,self.character.id_,self.character.lvl)
    
    
    




        
            