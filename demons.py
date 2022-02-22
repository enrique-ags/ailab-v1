from tkinter import *
from tkinter import messagebox
from turtle import bgcolor
from juego import Juego
from PIL import ImageTk, Image

#globals
#actions = ['aquajet','ColaFerrea','Cabezazo','Lluvia','aquarder.png']
#ventaja Roca, Fuego
#Desventaja Electrico, Planta
dctAquarder={'aquaarder-aquaarder-aquajet':'3','aquaarder-mousebug-aquajet':'3','aquaarder-aquaarder-ColaFerrea':'2','aquaarder-mousebug-ColaFerrea':'2',
'aquaarder-aquaarder-Cabezazo':'2','aquaarder-mousebug-Cabezazo':'2','aquaarder-firesor-aquajet':'5','aquaarder-rockdog-aquajet':'5',
'aquaarder-firesor-ColaFerrea':'0','aquaarder-firesor-Cabezazo':'0','aquaarder-firesor-Lluvia':'0','aquaarder-rockdog-ColaFerrea':'0',
'aquaarder-rockdog-Cabezazo':'0','aquaarder-rockdog-Lluvia':'0'
}
flag_demon = False
user_demon=''
cpu_demon=''

def new_tournament():
   new= Toplevel(root)
   new.geometry("750x250")
   new.title("New Tournament")



def backgroundButton01(): #aquaarder
    global flag_demon
    global user_demon
    global cpu_demon
    if not flag_demon:
        user_demon = 'aquaarder'
    else:
        cpu_demon = 'aquaarder'    
    btn01.config(bg='red')
    btn02.config(bg='white')
    btn03.config(bg='white')
    btn04.config(bg='white')
    btn05.config(bg='white')
    btn06.config(bg='white')
    if flag_demon == False:
        a = messagebox.askquestion ('Training Mode','Pick oponent?',icon = 'info')
        if a=='yes':
            flag_demon = True
            
        else:
            root.destroy()
    lbluser.configure(text="User: " +  user_demon + " VS. " + "CPU: " + cpu_demon) 
    print(user_demon + ' ' + cpu_demon)
    

                


def backgroundButton02():   #electder
    global flag_demon
    global user_demon
    global cpu_demon
    
    if not flag_demon:
        user_demon = 'electder'
    else:
        cpu_demon = 'electder'
    if flag_demon == False:
        a = messagebox.askquestion ('Training Mode','Pick oponent?',icon = 'info')
        if a=='yes':
            flag_demon = True
            
        else:
            root.destroy()
    lbluser.configure(text="User: " +  user_demon + " VS. " + "CPU: " + cpu_demon) 
    print(user_demon + ' ' + cpu_demon)
    

    btn01.config(bg='white')
    btn02.config(bg='red')
    btn03.config(bg='white')
    btn04.config(bg='white')
    btn05.config(bg='white')
    btn06.config(bg='white')
def backgroundButton03():   #firesor
    global flag_demon
    global user_demon
    global cpu_demon
    
    if not flag_demon:
        user_demon = 'firesor'
    else:
        cpu_demon = 'firesor'
    if flag_demon == False:
        a = messagebox.askquestion ('Training Mode','Pick oponent?',icon = 'info')
        if a=='yes':
            flag_demon = True
            
        else:
            root.destroy()
    lbluser.configure(text="User: " +  user_demon + " VS. " + "CPU: " + cpu_demon)       
    print(user_demon + ' ' + cpu_demon)

    btn01.config(bg='white')
    btn02.config(bg='white')
    btn03.config(bg='red')
    btn04.config(bg='white')
    btn05.config(bg='white')
    btn06.config(bg='white')
def backgroundButton04():   #mousebug
    global flag_demon
    global user_demon
    global cpu_demon
    
    if not flag_demon:
        user_demon = 'mousebug'
    else:
        cpu_demon = 'mousebug'
    if flag_demon == False:
        a = messagebox.askquestion ('Training Mode','Pick oponent?',icon = 'info')
        if a=='yes':
            flag_demon = True
            
        else:
            root.destroy()
    lbluser.configure(text="User: " +  user_demon + " VS. " + "CPU: " + cpu_demon) 
    print(user_demon + ' ' + cpu_demon)
    
    btn01.config(bg='white')
    btn02.config(bg='white')
    btn03.config(bg='white')
    btn04.config(bg='red')
    btn05.config(bg='white')
    btn06.config(bg='white')
def backgroundButton05(): #splant  
    global flag_demon
    global user_demon
    global cpu_demon
    
    if not flag_demon:
        user_demon = 'splant'
    else:
        cpu_demon = 'splant'
    if flag_demon == False:
        a = messagebox.askquestion ('Training Mode','Pick oponent?',icon = 'info')
        if a=='yes':
            flag_demon = True
            
        else:
            root.destroy()
    lbluser.configure(text="User: " +  user_demon + " VS. " + "CPU: " + cpu_demon) 
    print(user_demon + ' ' + cpu_demon)
        
    btn01.config(bg='white')
    btn02.config(bg='white')
    btn03.config(bg='white')
    btn04.config(bg='white')
    btn05.config(bg='red')
    btn06.config(bg='white')   
def backgroundButton06():   #rockdog
    global flag_demon
    global user_demon
    global cpu_demon
    
    if not flag_demon:
        user_demon = 'rockdog'
    else:
        cpu_demon = 'rockdog'
    if flag_demon == False:
        a = messagebox.askquestion ('Training Mode','Pick oponent?',icon = 'info')
        if a=='yes':
            flag_demon = True
            
        else:
            root.destroy()
    lbluser.configure(text="User: " +  user_demon + " VS. " + "CPU: " + cpu_demon) 
    print(user_demon + ' ' + cpu_demon)
        
    btn01.config(bg='white')
    btn02.config(bg='white')
    btn03.config(bg='white')
    btn04.config(bg='white')
    btn05.config(bg='white')
    btn06.config(bg='red')    

def BattleField():
    global dctAquarder
    if  (len(user_demon) >0 and len(cpu_demon)  > 0 ):

        if user_demon=='aquaarder':
            actions = ['aquajet','ColaFerrea','Cabezazo','Lluvia','aquarder.png']
            dc = dctAquarder
            
        if user_demon=='firesor':
           actions = ['Llamarada','Embestida','Mordisco','DiaSoleado','firesor.png']  
           dc = dctAquarder             
        if user_demon=='electder':
           actions = ['Trueno','Arañazo','Mordisco','CampoMagnetico','electder.png']   
        if user_demon=='mousebug':
           actions = ['Picotazo','Embestida','Cabezazo','Esporas','mousebug.png']                        
        if user_demon=='splant':
           actions = ['HojaNavaja','Mordisco','Cabezazo','RayoSolar','splant.png']                        
        if user_demon=='rockdog':
           actions = ['RocaAfilado','Velocidad','ColaFerrea','CampoRocoso','splant.png']                        



        new= Toplevel(root)
        new.geometry("750x250")
        new.title("Battle ground")
        lblBattleuser = Label(new,text=user_demon,fg='blue')
        lblBattleuser.place(x=300,y=25)
        lblCpuUser = Label(new,text=cpu_demon,fg='red')
        lblCpuUser.place(x=550,y=25)  
        #-------------      
        lblAcction1 = Button(new,text=actions[0],width=25)
        lblAcction1.place(x=10,y=25)
        lblAcction1_points = Label(new,text='Points: ' + dc[user_demon+'-'+cpu_demon + '-' +actions[0]],bg='yellow')
        lblAcction1_points.place(x=200,y=25)   
        #-------------     
        lblAcction2 = Button(new,text=actions[1],width=25)
        lblAcction2.place(x=10,y=50)
        lblAcction2_points = Label(new,text='Points: ' + dc[user_demon+'-'+cpu_demon + '-' +actions[1]],bg='yellow')
        lblAcction2_points.place(x=200,y=55)        
        #-------------     
        lblAcction3 = Button(new,text=actions[2],width=25)
        lblAcction3.place(x=10,y=75)
        lblAcction3_points = Label(new,text='Points: ' + dc[user_demon+'-'+cpu_demon + '-' +actions[2]],bg='yellow')
        lblAcction3_points.place(x=200,y=85)  
        lblAcction4 = Button(new,text=actions[3],width=25)
        lblAcction4.place(x=10,y=100)
        #------------- 
        
        #user demon
        image1 = Image.open(actions[4])
        image1 = image1.resize((80, 80), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        btnUserDemon = Button(new,image=test,bg='#ffffff', activebackground='red')
        btnUserDemon.place(x=300,y=50)
        btnUserDemon.image = test

        #cpu demon
        image2 = Image.open(cpu_demon + '.png')
        image2 = image2.resize((80, 80), Image.ANTIALIAS)
        test2 = ImageTk.PhotoImage(image2)
        btnCPUDemon = Button(new,image=test2,bg='#ffffff', activebackground='red')
        btnCPUDemon.place(x=500,y=50)
        btnCPUDemon.image = test2



        
    else:
        messagebox.showwarning('Missing values',"Pick a demon")



root = Tk()
root.geometry("600x400")
root.title("Pick your demon")
##Aquarder
lblAqua = Label(root,text='Aquarder')
lblAqua.place(x=10,y=10)
image1 = Image.open("aquarder.png")
image1 = image1.resize((80, 80), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
btn01 = Button(image=test,bg='#ffffff', activebackground='red',command=backgroundButton01)
btn01.image = test
btn01.place(x=20,y=40)
btnAquaDetails = Button(root,text='Details')
btnAquaDetails.place(x=30,y=140)

##Electder
lblElectder = Label(root,text='Electder')
lblElectder.place(x=180,y=10)
image1 = Image.open("electder.png")
image1 = image1.resize((80, 80), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
btn02 = Button(image=test,bg='#ffffff', activebackground='red',command=backgroundButton02)
btn02.image = test
btn02.place(x=180,y=40)
btnElectderDetails = Button(root,text='Details')
btnElectderDetails.place(x=180,y=140)
##Firesor
lblFiresor = Label(root,text='Firesor')
lblFiresor.place(x=350,y=10)
image1 = Image.open("Firesor.png")
image1 = image1.resize((80, 80), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
btn03 = Button(image=test,bg='#ffffff', activebackground='red',command=backgroundButton03)
btn03.image = test
btn03.place(x=350,y=40)
btnFiresorDetails = Button(root,text='Details')
btnFiresorDetails.place(x=350,y=140)

##MouseBug
lblMouse = Label(root,text='MouseBug')
lblMouse.place(x=10,y=180)
image1 = Image.open("mousebug.png")
image1 = image1.resize((80, 80), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
btn04 = Button(image=test,bg='#ffffff', activebackground='red',command=backgroundButton04)
btn04.image = test
btn04.place(x=10,y=200)
btnMouseDetails = Button(root,text='Details')
btnMouseDetails.place(x=10,y=300)

##Splant
lblSplant = Label(root,text='Splant')
lblSplant.place(x=180,y=180)
image1 = Image.open("splant.png")
image1 = image1.resize((80, 80), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
btn05 = Button(image=test,bg='#ffffff', activebackground='red',command=backgroundButton05)
btn05.image = test
btn05.place(x=180,y=200)
btnMouseDetails = Button(root,text='Details')
btnMouseDetails.place(x=180,y=300)

##RockDog
lblSplant = Label(root,text='RockDog')
lblSplant.place(x=350,y=180)
image1 = Image.open("rockdog.png")
image1 = image1.resize((80, 80), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
btn06 = Button(image=test,bg='#ffffff', activebackground='red',command=backgroundButton06)
btn06.image = test
btn06.place(x=350,y=200)
btnMouseDetails = Button(root,text='Details')
btnMouseDetails.place(x=370,y=300)


lbluser = Label(root,text='USER: ')
lbluser.place(x=10,y=350)

btnIniciar = Button(root,text='        Start                  ',bg='blue',fg='white',command=BattleField)
btnIniciar.place(x=250,y=350)






    


root.mainloop()


