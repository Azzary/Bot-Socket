import socket
import time
from hash import Hash
import threading


class My_socket():
    
    def __init__(self,addresse,interface):
        self.interface = interface
        self.my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.my_socket.connect(addresse)
        except socket.error:
            print ("connection failed")
            
    
    def send_packet(self,packet):
        packet += "\n\x00"
        #print("[DEBUG] Paquet Dofus Reçu mais on dirais que non")
        threading.Thread(None,self.print_packet("[DEBUG] Paquet Dofus Envoyé : " +packet)).start
        packet = packet.encode()
        time.sleep(0.0)
        self.my_socket.send(packet)
        
        
    def recv_msg(self):
        packet = self.my_socket.recv(1024).decode()
        threading.Thread(None,self.print_packet("[DEBUG] Paquet Dofus Reçu : " +packet)).start
        return packet
                

    def print_packet(self,packets):
        for packet in packets.split("\x00"):
            if packet != "[DEBUG] Paquet Dofus Reçu : ":
                print(packet)
                self.interface.print_richTextBox1(packet)


    def disconnecte(self):
        self.my_socket.close()
