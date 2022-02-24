from tkinter import *
from tkinter import messagebox
from turtle import bgcolor

from click import command
from juego import Juego
from PIL import ImageTk, Image
import debugpy
import time
import random

#globals
#actions = ['aquajet','ColaFerrea','Cabezazo','Lluvia','aquarder.png']
#ventaja Roca, Fuego
#Desventaja Electrico, Planta
#aquaarder-mousebug-aquajet
dctAquarder={'aquaarder-aquaarder-aquajet':'3','aquaarder-mousebug-aquajet':'3','aquaarder-aquaarder-ColaFerrea':'2','aquaarder-mousebug-ColaFerrea':'2',
'aquaarder-aquaarder-Cabezazo':'2','aquaarder-mousebug-Cabezazo':'2','aquaarder-firesor-aquajet':'5','aquaarder-rockdog-aquajet':'5',
'aquaarder-firesor-ColaFerrea':'0','aquaarder-firesor-Cabezazo':'0','aquaarder-firesor-Lluvia':'0','aquaarder-rockdog-ColaFerrea':'0',
'aquaarder-rockdog-Cabezazo':'0','aquaarder-rockdog-Lluvia':'0',
'aquaarder-electder-aquajet':'2','aquaarder-electder-ColaFerrea':'0','aquaarder-electder-Cabezazo':'0','aquaarder-electder-Lluvia':'0',
'aquaarder-splant-aquajet':'2','aquaarder-splant-ColaFerrea':'0','aquaarder-splant-Cabezazo':'0','aquaarder-splant-Lluvia':'0',
'aquaarder-aquaarder-aquajet-True':'5','aquaarder-aquaarder-Lluvia-True':'5'
}

dctAquarderWithPower={'aquaarder-aquaarder-aquajet':'5','aquaarder-mousebug-aquajet':'5','aquaarder-aquaarder-ColaFerrea':'2','aquaarder-mousebug-ColaFerrea':'2',
'aquaarder-aquaarder-Cabezazo':'2','aquaarder-mousebug-Cabezazo':'2','aquaarder-firesor-aquajet':'5','aquaarder-rockdog-aquajet':'5',
'aquaarder-firesor-ColaFerrea':'0','aquaarder-firesor-Cabezazo':'0','aquaarder-firesor-Lluvia':'0','aquaarder-rockdog-ColaFerrea':'0',
'aquaarder-rockdog-Cabezazo':'0','aquaarder-rockdog-Lluvia':'0',
'aquaarder-electder-aquajet':'2','aquaarder-electder-ColaFerrea':'0','aquaarder-electder-Cabezazo':'0','aquaarder-electder-Lluvia':'0',
'aquaarder-splant-aquajet':'2','aquaarder-splant-ColaFerrea':'0','aquaarder-splant-Cabezazo':'0','aquaarder-splant-Lluvia':'0',
'aquaarder-aquaarder-aquajet-True':'5','aquaarder-aquaarder-Lluvia-True':'5'
}




#ventaja Planta,Roca
#Desventaja Fuego, Electrico
#Normal Escarabajo,agua
#actions = ['Picotazo','Embestida','Cabezazo','Esporas','mousebug.png']                        
dctMouseBug={'mousebug-mousebug-Picotazo':'3','mousebug-mousebug-Embestida':'2',
'mousebug-mousebug-Cabezazo':'2','mousebug-mousebug-Esporas':'0',
'mousebug-aquaarder-Picotazo':'3','mousebug-aquaarder-Embestida':'2',
'mousebug-aquaarder-Cabezazo':'2','mousebug-aquaarder-Esporas':'0',
'mousebug-splant-Picotazo':'5','mousebug-splant-Embestida':'0',
'mousebug-splant-Cabezazo':'0','mousebug-splant-Esporas':'0',
'mousebug-rockdog-Picotazo':'5','mousebug-rockdog-Embestida':'0',
'mousebug-rockdog-Cabezazo':'0','mousebug-rockdog-Esporas':'0',
'mousebug-electder-Picotazo':'2','mousebug-electder-Embestida':'0',
'mousebug-electder-Cabezazo':'0','mousebug-electder-Esporas':'0',
'mousebug-firesor-Picotazo':'2','mousebug-firesor-Embestida':'0',
'mousebug-firesor-Cabezazo':'0','mousebug-firesor-Esporas':'0'
}

flag_demon = False
user_demon=''
cpu_demon=''
user_initial_points = 25
cpu_initial_points = 25
user_hits = []
cpu_hits = []
#administrar turnos
turns = [3,5,7,9,11,13,15,17,19,21,23,25,27,29]
turnpop = []
turnsCounter = 0
turnsFlag = False
actions=[]



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
def backgroundButton05():   #splant  
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
    global turnsFlag
    global dctAquarder
    global user_initial_points
    global cpu_initial_points
    global user_hits, cpu_hits,actions

    if  (len(user_demon) >0 and len(cpu_demon)  > 0 ):

        if user_demon=='aquaarder':
            actions = ['aquajet','ColaFerrea','Cabezazo','Lluvia','aquarder.png']
            dc = dctAquarder


            
        if user_demon=='firesor':
           actions = ['Llamarada','Embestida','Mordisco','DiaSoleado','firesor.png']  
          
        if user_demon=='electder':
           actions = ['Trueno','Arañazo','Mordisco','CampoMagnetico','electder.png']   
        if user_demon=='mousebug':
           actions = ['Picotazo','Embestida','Cabezazo','Esporas','mousebug.png']                        
           dc = dctMouseBug
        if user_demon=='splant':
           actions = ['HojaNavaja','Mordisco','Cabezazo','RayoSolar','splant.png']                        
        if user_demon=='rockdog':
           actions = ['RocaAfilado','Velocidad','ColaFerrea','CampoRocoso','splant.png'] 



       
        new= Toplevel(root)
        new.geometry("750x450")
        new.title("Battle ground")
        lblBattleuser = Label(new,text=user_demon,fg='blue' ,font=("Arial", 25))
        lblBattleuser.place(x=300,y=150)
        lblCpuUser = Label(new,text=cpu_demon,fg='red',font=("Arial", 25))
        lblCpuUser.place(x=500,y=150)  

        # User Score Labels
        lbluser_score = Label(new,text=str(user_initial_points) + ' Hp',fg='blue',font=("Arial", 25))
        lbluser_score.place(x=300, y = 200)

        lblcpu_score = Label(new,text=str(cpu_initial_points) + ' Hp',fg='red',font=("Arial", 25))
        lblcpu_score.place(x=500, y = 200)

        #user actions label
        lbluser_actions = Label(new,text='',fg='blue',font=("Courier", 20))
        lbluser_actions.place(x=150, y = 350)


            
        lblAcction1 = Button(new,text=actions[0],width=25,command=lambda:[lblcpu_score.config(text=hitButton01()),
        lbluser_actions.config(text='you performed: ' +actions[0] ),lbluser_score.config(text=cpu_hitButton01()),lblAcction4.config(bg=hitButton05())])

        lblAcction1.place(x=10,y=25)
        lblAcction1_points = Label(new,text= dc[user_demon+'-'+cpu_demon + '-' +actions[0]],bg='yellow')
        lblAcction1_points.place(x=200,y=25)   
      
        #-------------     
        lblAcction2 = Button(new,text=actions[1],width=25)
        lblAcction2.place(x=10,y=50)
        lblAcction2_points = Label(new,text= dc[user_demon+'-'+cpu_demon + '-' +actions[1]],bg='yellow')
        lblAcction2_points.place(x=200,y=55)        
        #-------------     x
        lblAcction3 = Button(new,text=actions[2],width=25)
        lblAcction3.place(x=10,y=75)
        lblAcction3_points = Label(new,text=dc[user_demon+'-'+cpu_demon + '-' +actions[2]],bg='yellow')
        lblAcction3_points.place(x=200,y=85)  
        lblAcction4 = Button(new,text=actions[3],width=25,command=lambda:[powerButton(),lblAcction4.config(bg=hitButton05()),lblcpu_score.config(text=hitButton04())])
        lblAcction4.place(x=10,y=100)
        user_hits.append(dc[user_demon+'-'+cpu_demon + '-' +actions[0]])
        user_hits.append(dc[user_demon+'-'+cpu_demon + '-' +actions[1]])
        user_hits.append(dc[user_demon+'-'+cpu_demon + '-' +actions[2]])
        user_hits.append(dc[user_demon+'-'+cpu_demon + '-' +actions[3]+'-'+'True'])
        #------------- 
        
        

 

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
        #lbl action points for CPU
        if cpu_demon=='aquaarder':
            cpu_actions = ['aquajet','ColaFerrea','Cabezazo','Lluvia','aquarder.png']
            cpu_dc = dctAquarder
        if cpu_demon=='firesor':
           cpu_actions = ['Llamarada','Embestida','Mordisco','DiaSoleado','firesor.png']  
          
        if cpu_demon=='electder':
           cpu_actions = ['Trueno','Arañazo','Mordisco','CampoMagnetico','electder.png']   
        if cpu_demon=='mousebug':
           cpu_actions = ['Picotazo','Embestida','Cabezazo','Esporas','mousebug.png']                        
           cpu_dc = dctMouseBug
        if cpu_demon=='splant':
           cpu_actions = ['HojaNavaja','Mordisco','Cabezazo','RayoSolar','splant.png']                        
        if cpu_demon=='rockdog':
           cpu_actions = ['RocaAfilado','Velocidad','ColaFerrea','CampoRocoso','splant.png'] 

        lblAcction4_points = Label(new,text='CPU Points: ' + cpu_dc[cpu_demon +'-'+user_demon+'-'+cpu_actions[0]],bg='yellow')
        lblAcction4_points.place(x=650,y=25)  
        lblAcction5_points = Label(new,text='CPU Points: ' + cpu_dc[cpu_demon +'-'+user_demon+'-'+cpu_actions[1]],bg='yellow')
        lblAcction5_points.place(x=650,y=55)  
        lblAcction6_points = Label(new,text='CPU Points: ' + cpu_dc[cpu_demon +'-'+user_demon+'-'+cpu_actions[2]],bg='yellow')
        lblAcction6_points.place(x=650,y=85)
        cpu_hits.append(cpu_dc[cpu_demon +'-'+user_demon+'-'+cpu_actions[0]])
        cpu_hits.append(cpu_dc[cpu_demon +'-'+user_demon+'-'+cpu_actions[1]])
        cpu_hits.append(cpu_dc[cpu_demon +'-'+user_demon +'-'+cpu_actions[2]])



        
    else:
        messagebox.showwarning('Missing values',"Pick a demon")

def hitButton01():
    global turnsFlag
    global turnsCounter
    global turnpop
    global cpu_initial_points
    global dctAquarderWithPower
    global actions

    turnsCounter+=1
    
    if cpu_initial_points <=0:

        return 'You win'
    
    else:
        if turnsCounter in turns  or len(turnpop)>0:
            turnsFlag = True
            if len(turnpop)<2:
                turnpop.append(1)
                turnpop.append(2)
                
        else:
            turnsFlag = False   

        cpu_initial_points -= int(user_hits[0])
    

    print (cpu_initial_points)
    return cpu_initial_points

def powerButton():
    
    global turnpop
    global turnsFlag
    print(turnpop)
    if len(turnpop)>0:
        turnpop.pop()

    else:
        turnsFlag  = False





def hitButton04():
    global turnsFlag
    global turnsCounter
    global turnpop
    global cpu_initial_points
    global dctAquarderWithPower
    global actions

    if turnsFlag:
        r = dctAquarderWithPower[user_demon+'-'+cpu_demon+'-'+actions[0]]
        cpu_initial_points -= int(r)
        print (cpu_initial_points)
        return  cpu_initial_points


def hitButton05():
    global turnsFlag

    if turnsFlag:
        return 'Orange'
    else:
        return 'Gray'
    




def cpu_hitButton01():

    random_attack=random.randint(0,2)
    global user_initial_points
    global cpu_hits
    user_initial_points -= int(cpu_hits[random_attack])
    print('attack: ' + cpu_hits[random_attack])
    print (user_initial_points)
    return user_initial_points






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
btn01.place(x=10,y=40)
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


