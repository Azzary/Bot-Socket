import threading
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import os


class Interface(threading.Thread):

    def __init__(self):
        threading.Thread(None,self.launch).start()

    def create_charater(self,gfx,speudo ,id_,lvl = ""):
         #os.path.dirname(os.path.abspath(__file__))
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),f"gfx\\{gfx}.png")
        
        image = Image.open(dir_path) 
        photo = ImageTk.PhotoImage(image)

        self.canvas.place(relx=0.03, rely=0.1, relwidth=1, relheight=1)
        self.canvas.create_image(photo.width()/4.5,photo.height()/2,image=photo)
        self.canvas.image = photo
        speudo_and_id ="SPEUDO: "+ speudo +"        ID: "+ id_ + "        LEVEL: "+ lvl
        name = Label(self.o2, text = speudo_and_id, relief = RAISED )
        name.place(relx=0.01, rely=0.017,relwidth=0.4, relheight=0.09)
        



    def create_notebook(self):
        self.onglets = ttk.Notebook(self.bot)   # Création du système d'onglets
        self.onglets.pack()
        self.onglets.place(relx=0.15, rely=0.05, relwidth=0.83, relheight=0.93)


        #onglet pour les packets
        self.o1 = ttk.Frame(self.onglets)       
        self.o1.pack()
        self.onglets.add(self.o1, text='Packet')
        
        #onglet pour le personnage
        self.o2 = ttk.Frame(self.onglets)      
        self.o2.pack()
        self.onglets.add(self.o2, text='character')     

    def create_text(self):
        self.richTextBox1=Text(self.o1,font = '{MS Sans Serif} 10')
        self.richTextBox1.place(relx=0.05, rely=0.07, relwidth=0.85, relheight=0.75)
        self.scrollbar = Scrollbar(self.richTextBox1)
        self.scrollbar.pack( side = RIGHT, fill=Y)

    def create_canvas(self):
        self.canvas = Canvas(self.o2,width=256,height=450)
        self.create_charater(gfx=0,speudo="no_name",id_ = "None")


        
        
        

    def launch(self):
        self.bot = Tk()
        self.bot.title('bot')
        self.bot.geometry('900x600+100+100')

        self.create_notebook()
        self.create_text()
        self.create_canvas()
        
        #Button(o2, text='En attente', command=None).pack(padx=100, pady=100)

        self.bot.mainloop()
        


    def print_richTextBox1(self,text):
        self.richTextBox1.insert(END,text+"\n\n")
        self.richTextBox1.see("end")
        

        


            

    
       
  
