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
'aquaarder-firesor-ColaFerrea':'2','aquaarder-firesor-Cabezazo':'2','aquaarder-firesor-Lluvia':'0','aquaarder-rockdog-ColaFerrea':'2',
'aquaarder-rockdog-Cabezazo':'2','aquaarder-rockdog-Lluvia':'0',
'aquaarder-electder-aquajet':'2','aquaarder-electder-ColaFerrea':'2','aquaarder-electder-Cabezazo':'2','aquaarder-electder-Lluvia':'0',
'aquaarder-splant-aquajet':'2','aquaarder-splant-ColaFerrea':'2','aquaarder-splant-Cabezazo':'2','aquaarder-splant-Lluvia':'0'
}

"""dctAquarder={'aquaarder-aquaarder-aquajet':'3','aquaarder-mousebug-aquajet':'3','aquaarder-aquaarder-ColaFerrea':'2','aquaarder-mousebug-ColaFerrea':'2',
'aquaarder-aquaarder-Cabezazo':'2','aquaarder-mousebug-Cabezazo':'2','aquaarder-firesor-aquajet':'5','aquaarder-rockdog-aquajet':'5',
'aquaarder-firesor-ColaFerrea':'0','aquaarder-firesor-Cabezazo':'0','aquaarder-firesor-Lluvia':'0','aquaarder-rockdog-ColaFerrea':'0',
'aquaarder-rockdog-Cabezazo':'0','aquaarder-rockdog-Lluvia':'0',
'aquaarder-electder-aquajet':'2','aquaarder-electder-ColaFerrea':'0','aquaarder-electder-Cabezazo':'0','aquaarder-electder-Lluvia':'0',
'aquaarder-splant-aquajet':'2','aquaarder-splant-ColaFerrea':'0','aquaarder-splant-Cabezazo':'0','aquaarder-splant-Lluvia':'0'
}"""


dctAquarderWithPower={'aquaarder-aquaarder-aquajet':'5','aquaarder-mousebug-aquajet':'5','aquaarder-firesor-aquajet':'7',
'aquaarder-rockdog-aquajet':'7',
'aquaarder-electder-aquajet':'4','aquaarder-splant-aquajet':'4'
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
'mousebug-splant-Cabezazo':'2','mousebug-splant-Esporas':'0',
'mousebug-rockdog-Picotazo':'5','mousebug-rockdog-Embestida':'0',
'mousebug-rockdog-Cabezazo':'2','mousebug-rockdog-Esporas':'0',
'mousebug-electder-Picotazo':'2','mousebug-electder-Embestida':'0',
'mousebug-electder-Cabezazo':'2','mousebug-electder-Esporas':'0',
'mousebug-firesor-Picotazo':'2','mousebug-firesor-Embestida':'0',
'mousebug-firesor-Cabezazo':'2','mousebug-firesor-Esporas':'0'
}

dctMouseBugWithPower={'mousebug-mousebug-Picotazo':'5','mousebug-aquaarder-Picotazo':'5'
,'mousebug-splant-Picotazo':'7','mousebug-rockdog-Picotazo':'7',
'mousebug-electder-Picotazo':'4','mousebug-firesor-Picotazo':'4'}

dctElectderWithPower ={'electder-firesor-trueno':'5','electder-aquaarder-trueno':'7','electder-electder-trueno':'5','electder-mousebug-trueno':'5','electder-splant-trueno':'4',
'electder-rockdog-trueno':'4'}

dctFiresorWithPower ={'firesor-aquaarder-Llamarada':'4','firesor-electder-Llamarada':'5','firesor-splant-Llamarada':'7','firesor-rockdog-Llamarada':'4'}
dctRockDogWithPower={'rockdog-aquaarder-RocaAfilado':'5','rockdog-aquaarder-RocaAfilado':'4','rockdog-electder-RocaAfilado':'7','rockdog-firesor-RocaAfilado':'7',
'rockdog-mousebug-RocaAfilado':'5', 'rockdog-splant-RocaAfilado':'4','rockdog-rockdog-RocaAfilado':'5'}
dctSplantWithPower = {'splant-aquaarder-HojaNavaja':'5','splant-electder-HojaNavaja':'7', 'splant-firesor-HojaNavaja':'4','splant-mousebug-HojaNavaja':4,
'splant-splant-HojaNavaja':'5','splant-rockdog-HojaNavaja':'7'}

dctElectder={'electder-aquaarder-trueno':'5','electder-mousebug-trueno':'3','electder-aquaarder-ColaFerrea':'2','electder-mousebug-ColaFerrea':'2',
'electder-aquaarder-Cabezazo':'2','electder-mousebug-Cabezazo':'2','electder-firesor-trueno':'5','electder-rockdog-trueno':'5',
'electder-firesor-ColaFerrea':'0','electder-firesor-Cabezazo':'0','electder-firesor-Lluvia':'0','electder-rockdog-ColaFerrea':'0',
'electder-rockdog-Cabezazo':'0','electder-rockdog-Lluvia':'0',
'electder-electder-trueno':'2','electder-electder-ColaFerrea':'0','electder-electder-Cabezazo':'0','electder-electder-Lluvia':'0',
'electder-splant-trueno':'2','electder-splant-ColaFerrea':'0','electder-splant-Cabezazo':'0','electder-splant-Lluvia':'0','electder-mousebug-arañazo':'3'
,'electder-mousebug-mordisco':'3','electder-aquaarder-arañazo':'3','electder-aquaarder-mordisco':'3','electder-electder-arañazo':'3','electder-electder-mordisco':'3',
'electder-firesor-arañazo':'3','electder-firesor-mordisco':'3','electder-firesor-trueno':'3','electder-splant-arañazo':'2','electder-splant-mordisco':'3',
'electder-rockdog-arañazo':'2','electder-rockdog-mordisco':'3','electder-rockdog-arañazo':'3'}

dctFiresor={'firesor-aquaarder-llamarada':'5','firesor-mousebug-llamarada':'3','firesor-aquaarder-mordisco':'2','firesor-mousebug-mordisco':'2',
'firesor-aquaarder-Cabezazo':'2','firesor-mousebug-Cabezazo':'2','firesor-firesor-llamarada':'5','firesor-rockdog-llamarada':'5',
'firesor-firesor-mordisco':'0','firesor-firesor-Cabezazo':'0','firesor-firesor-Lluvia':'0','firesor-rockdog-mordisco':'0',
'firesor-rockdog-Cabezazo':'0','firesor-rockdog-Lluvia':'0',
'firesor-electder-llamarada':'2','firesor-electder-mordisco':'0','firesor-electder-Cabezazo':'0','firesor-electder-Lluvia':'0',
'firesor-splant-llamarada':'2','firesor-splant-mordisco':'0','firesor-splant-Cabezazo':'0','firesor-splant-Lluvia':'0','firesor-mousebug-embestida':'3'
,'firesor-mousebug-Mordisco':'2','firesor-aquaarder-Mordisco':'2','firesor-aquaarder-Llamarada':'2','firesor-aquaarder-Embestida':'2',
'firesor-electder-Llamarada':'3','firesor-electder-Embestida':'2','firesor-electder-Mordisco':'2','firesor-splant-Llamarada':'5','firesor-splant-Embestida':'2','firesor-splant-Mordisco':'2'
,'firesor-rockdog-Llamarada':'3','firesor-rockdog-Embestida':'2','firesor-rockdog-Mordisco':'2','firesor-mousebug-Llamarada':'3','firesor-mousebug-Embestida':'2',
'firesor-mousebug-Mordisco':'2'}

#actions = ['HojaNavaja','Mordisco','Cabezazo','RayoSolar','splant.png']  
dctSplant={'splant-aquaarder-HojaNavaja':'5','splant-mousebug-HojaNavaja':'3','splant-aquaarder-mordisco':'2','splant-mousebug-mordisco':'2',
'splant-aquaarder-Cabezazo':'2','splant-mousebug-Cabezazo':'2','splant-firesor-HojaNavaja':'5','splant-rockdog-HojaNavaja':'5',
'splant-firesor-mordisco':'0','splant-firesor-Cabezazo':'0','splant-firesor-Lluvia':'0','splant-rockdog-mordisco':'0',
'splant-rockdog-Cabezazo':'2','splant-rockdog-Lluvia':'0',
'splant-electder-HojaNavaja':'2','splant-electder-mordisco':'0','splant-electder-Cabezazo':'2','splant-electder-Lluvia':'0',
'splant-splant-HojaNavaja':'3','splant-splant-mordisco':'0','splant-splant-Cabezazo':'0','splant-splant-Lluvia':'0','splant-mousebug-embestida':'3'
,'splant-mousebug-Mordisco':'2','splant-aquaarder-Mordisco':'2','splant-aquaarder-Embestida':'2','splant-electder-Mordisco':'2','splant-firesor-Cabezazo':'2',
'splant-firesor-Mordisco':'2','splant-splant-Mordisco':'3','splant-splant-Mordisco':'2','splant-rockdog-Mordisco':'5'}


dctRockDog={'rockdog-aquaarder-HojaNavaja':'5','rockdog-mousebug-HojaNavaja':'3','rockdog-aquaarder-mordisco':'2','rockdog-mousebug-mordisco':'2',
'rockdog-aquaarder-Cabezazo':'2','rockdog-mousebug-Cabezazo':'2','rockdog-firesor-HojaNavaja':'5','rockdog-rockdog-HojaNavaja':'5',
'rockdog-firesor-mordisco':'0','rockdog-firesor-Cabezazo':'0','rockdog-firesor-Lluvia':'0','rockdog-rockdog-mordisco':'0',
'rockdog-rockdog-Cabezazo':'0','rockdog-rockdog-Lluvia':'0',
'rockdog-electder-HojaNavaja':'2','rockdog-electder-mordisco':'0','rockdog-electder-Cabezazo':'0','rockdog-electder-Lluvia':'0',
'rockdog-splant-HojaNavaja':'2','rockdog-splant-mordisco':'0','rockdog-splant-Cabezazo':'0','rockdog-splant-Lluvia':'0','rockdog-mousebug-embestida':'3'
,'rockdog-mousebug-Mordisco':'2','rockdog-aquaarder-Mordisco':'2','rockdog-aquaarder-HojaNavaja':'2','rockdog-aquaarder-Embestida':'2',
'rockdog-aquaarder-RocaAfilado':'2','rockdog-aquaarder-Velocidad':'2','rockdog-aquaarder-ColaFerrea':'2','rockdog-electder-RocaAfilado':'5',
'rockdog-electder-Velocidad':'2','rockdog-electder-ColaFerrea':'2','rockdog-firesor-RocaAfilado':'3','rockdog-firesor-Velocidad':'2','rockdog-firesor-ColaFerrea':'2',
'rockdog-mousebug-RocaAfilado':'3','rockdog-mousebug-Velocidad':'2','rockdog-mousebug-ColaFerrea':'2','rockdog-splant-RocaAfilado':'2','rockdog-splant-Velocidad':'2','rockdog-splant-ColaFerrea':'2',
'rockdog-rockdog-RocaAfilado':'3','rockdog-rockdog-Velocidad':'2','rockdog-rockdog-ColaFerrea':'2'}







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
           dc = dctFiresor
          
        if user_demon=='electder':
           actions = ['trueno','arañazo','mordisco','campoMagnetico','electder.png']   
           dc = dctElectder
        if user_demon=='mousebug':
           actions = ['Picotazo','Embestida','Cabezazo','Esporas','mousebug.png']                        
           dc = dctMouseBug
        if user_demon=='splant':
           actions = ['HojaNavaja','Mordisco','Cabezazo','RayoSolar','splant.png']
           dc = dctSplant                        
        if user_demon=='rockdog':
           actions = ['RocaAfilado','Velocidad','ColaFerrea','CampoRocoso','rockdog.png'] 
           dc = dctRockDog



       
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
        lblAcction2 = Button(new,text=actions[1],width=25,command=lambda:[lblcpu_score.config(text=hitButton02()),
        lbluser_actions.config(text='you performed: ' +actions[1] ),lbluser_score.config(text=cpu_hitButton01()),lblAcction4.config(bg=hitButton05())])

        lblAcction2.place(x=10,y=50)
        lblAcction2_points = Label(new,text= dc[user_demon+'-'+cpu_demon + '-' +actions[1]],bg='yellow')
        lblAcction2_points.place(x=200,y=55)        
        #-------------     x
        lblAcction3 = Button(new,text=actions[2],width=25,command=lambda:[lblcpu_score.config(text=hitButton03()),
        lbluser_actions.config(text='you performed: ' +actions[2] ),lbluser_score.config(text=cpu_hitButton01()),lblAcction4.config(bg=hitButton05())])
        lblAcction3.place(x=10,y=75)
        lblAcction3_points = Label(new,text=dc[user_demon+'-'+cpu_demon + '-' +actions[2]],bg='yellow')
        lblAcction3_points.place(x=200,y=85)  
        lblAcction4 = Button(new,text=actions[3],width=25,command=lambda:[powerButton(),lblAcction4.config(bg=hitButton05()),
        lblcpu_score.config(text=hitButton04()),lbluser_score.config(text=cpu_hitButton01())])
        lblAcction4.place(x=10,y=100)
        user_hits.append(dc[user_demon+'-'+cpu_demon + '-' +actions[0]])
        user_hits.append(dc[user_demon+'-'+cpu_demon + '-' +actions[1]])
        user_hits.append(dc[user_demon+'-'+cpu_demon + '-' +actions[2]])
        
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
           cpu_dc = dctFiresor
          
        if cpu_demon=='electder':
           cpu_actions = ['trueno','arañazo','mordisco','campoMagnetico','electder.png']    
           cpu_dc = dctElectder
        if cpu_demon=='mousebug':
           cpu_actions = ['Picotazo','Embestida','Cabezazo','Esporas','mousebug.png']                        
           cpu_dc = dctMouseBug
        if cpu_demon=='splant':
           cpu_actions = ['HojaNavaja','Mordisco','Cabezazo','RayoSolar','splant.png']   
           cpu_dc = dctSplant                     
        if cpu_demon=='rockdog':
           cpu_actions = ['RocaAfilado','Velocidad','ColaFerrea','CampoRocoso','rockdog.png'] 
           cpu_dc = dctRockDog

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
        time.sleep(2)
        
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

def hitButton02():
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

        cpu_initial_points -= int(user_hits[1])
    

    print (cpu_initial_points)
    return cpu_initial_points

def hitButton03():
    global turnsFlag
    global turnsCounter
    global turnpop
    global cpu_initial_points
    global dctAquarderWithPower
    global actions

    turnsCounter+=1
    
    if cpu_initial_points <=0:

        return 'You win'
    elif  user_initial_points <=0:
        return 'You Loose'

    
    else:
        if turnsCounter in turns  or len(turnpop)>0:
            turnsFlag = True
            if len(turnpop)<2:
                turnpop.append(1)
                turnpop.append(2)
                
        else:
            turnsFlag = False   

        cpu_initial_points -= int(user_hits[2])
    

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
    global dctAquarderWithPower,dctMouseBugWithPower
    global actions
    global user_demon
    dc={}

    if user_demon =='aquaarder':
        dc = dctAquarderWithPower
    if user_demon =='mousebug':
        dc = dctMouseBugWithPower
    if user_demon =='electder':
        dc = dctElectderWithPower
    if user_demon =='firesor':
        dc =dctFiresorWithPower
    if user_demon =='splant':
        dc=dctSplantWithPower
    if user_demon =='rockdog':
        dc=dctRockDogWithPower



    

    if turnsFlag:
        r = dc[user_demon+'-'+cpu_demon+'-'+actions[0]]
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
    global turnsFlag
    if turnsFlag:
        random_attack=random.randint(0,2)
        global user_initial_points
        global cpu_hits
        user_initial_points -= int(cpu_hits[random_attack])
        print('attack: ' + cpu_hits[random_attack])
        print (user_initial_points)
        return user_initial_points

def demons_Details_aquaarder():
    getDetails('aquaarder')
def demons_Details_firesor():
    getDetails('firesor')
def demons_Details_mousebug():
    getDetails('mousebug')
def demons_Details_splant():
    getDetails('splant')
def demons_Details_rockdog():
    getDetails('rockdog')
def demons_Details_electder():
    getDetails('electder')


 
 

def getDetails(demon):
    
    l=[]
    listAquaarder = ['Nombre: Aquarder Tipo Agua','Desventaja con: Electrico, Planta','Normal con Agua, Escarabajo, Ventaja con Roca y Fuego', 
    'Habilidad | A Normal | A con Vent | A sin vent | potenciador Normal | potenciador con vent| potenciador sin vent',
    'Aquajet    |     3pts       |     5pts        |      2pts       |        5 pts                     |            7pts                    |            4pts       ',
    'Cola-Ferr  |     2pts       |','Cabezazo  |     2pts       |',
    'Lluvia        | Activador de potenciador de campo, Solo se puede utilizar una vez cada 3 turnos y dura dos turnos','aquarder.png']  

    listFiresor = ['Nombre: Firesor Tipo Fuego','Desventaja con: Agua, Roca','Normal con Electrico, Fuego, Ventaja con Planta y Escarabajo', 
    'Habilidad | A Normal | A con Vent | A sin vent | potenciador Normal | potenciador con vent| potenciador sin vent',
    'Llamarada    |     3pts       |     5pts        |      2pts       |        5 pts                     |            7pts                    |            4pts       ',
    'Embestida  |     2pts       |','Mordisco  |     2pts       |',
    'Dia Soleado        | Activador de potenciador de campo, Solo se puede utilizar una vez cada 3 turnos y dura dos turnos','firesor.png']   


    listMouseBug = ['Nombre: Mousebug Tipo Escarabajo','Desventaja con: Fuego, Electrico','Normal con Escarabajo, Agua, Ventaja con Planta y Roca', 
    'Habilidad | A Normal | A con Vent | A sin vent | potenciador Normal | potenciador con vent| potenciador sin vent',
    'Picotazo    |     3pts       |     5pts        |      2pts       |        5 pts                     |            7pts                    |            4pts       ',
    'Embestida  |     2pts       |','Cabezazo  |     2pts       |',
    'Esporas        | Activador de potenciador de campo, Solo se puede utilizar una vez cada 3 turnos y dura dos turnos','mousebug.png']  

    listSplant = ['Nombre: Splant Tipo Planta','Desventaja con: Fuego, Escarabajo','Normal con Planta, ventaja con Planta, Roca', 
    'Habilidad | A Normal | A con Vent | A sin vent | potenciador Normal | potenciador con vent| potenciador sin vent',
    'Hoja Navaja    |     3pts       |     5pts        |      2pts       |        5 pts                     |            7pts                    |            4pts       ',
    'Mordizco  |     2pts       |','Cabezazo  |     2pts       |',
    'Rayo Solar        | Activador de potenciador de campo, Solo se puede utilizar una vez cada 3 turnos y dura dos turnos','splant.png'] 

    listRockDog = ['Nombre: RockDog Tipo Roca','Desventaja con: Agua, Planta','Normal con Roca, Escarabajo, ventaja con Fuego, Electrico', 
    'Habilidad | A Normal | A con Vent | A sin vent | potenciador Normal | potenciador con vent| potenciador sin vent',
    'Roca Afilada    |     3pts       |     5pts        |      2pts       |        5 pts                     |            7pts                    |            4pts       ',
    'Velocidad  |     2pts       |','Cola Ferrea  |     2pts       |',
    'Campo Rocoso        | Activador de potenciador de campo, Solo se puede utilizar una vez cada 3 turnos y dura dos turnos','rockdog.png'] 

    listElectder = ['Nombre: Electder Tipo Electrico','Desventaja con: Roca, Planta','Normal con Electrico, Fuego, ventaja con Agua, Escarabajo', 
    'Habilidad | A Normal | A con Vent | A sin vent | potenciador Normal | potenciador con vent| potenciador sin vent',
    'Trueno    |     3pts       |     5pts        |      2pts       |        5 pts                     |            7pts                    |            4pts       ',
    'Arañazo  |     2pts       |','Mordisco  |     2pts       |',
    'Campo Magnetico        | Activador de potenciador de campo, Solo se puede utilizar una vez cada 3 turnos y dura dos turnos','electder.png'] 

    if demon =='aquaarder':
        l = listAquaarder
    if demon =='firesor':
        l = listFiresor
    if demon =='mousebug':
        l = listMouseBug
    if demon =='splant':
        l = listSplant
    if demon =='rockdog':
        l = listRockDog
    if demon =='electder':
        l = listElectder
        
        
    demonCanvas= Toplevel(root)
    demonCanvas.geometry("1000x250")
    
    demonCanvas.title("Details ")
    lblDemon = Label(demonCanvas,text=l[0])
    lblDemon.place(x=10,y=25)


    lblDemon2 = Label(demonCanvas,text=l[1])
    lblDemon2.place(x=10,y=55)

    lblDemon3 = Label(demonCanvas,text=l[2] )
    lblDemon3.place(x=10,y=85)

    lblDemon4 = Label(demonCanvas,text=l[3] )
    lblDemon4.place(x=10,y=105)

    lblDemon5 = Label(demonCanvas,text=l[4] )
    lblDemon5.place(x=10,y=135)

    lblDemon6 = Label(demonCanvas,text=l[5] )
    lblDemon6.place(x=10,y=165)

    lblDemon7 = Label(demonCanvas,text=l[6] )
    lblDemon7.place(x=10,y=195)

    lblDemon8 = Label(demonCanvas,text=l[7] )
    lblDemon8.place(x=10,y=215)
    i = l[8]
    print(i)
    image1 = Image.open(i)
    image1 = image1.resize((80, 80), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    btnDemon = Button(demonCanvas,image=test)
    btnDemon.place(x=650, y = 10)
    btnDemon.image = test
    

    





   




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
btnAquaDetails = Button(root,text='Details', command=demons_Details_aquaarder)
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
btnElectderDetails = Button(root,text='Details',command=demons_Details_electder)
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
btnFiresorDetails = Button(root,text='Details',command=demons_Details_firesor)
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
btnMouseDetails = Button(root,text='Details',command=demons_Details_mousebug)
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
btnMouseDetails = Button(root,text='Details',command=demons_Details_splant)
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
btnMouseDetails = Button(root,text='Details',command=demons_Details_rockdog)
btnMouseDetails.place(x=370,y=300)


lbluser = Label(root,text='USER: ')
lbluser.place(x=10,y=350)

btnIniciar = Button(root,text='        Start                  ',bg='blue',fg='white',command=BattleField)
btnIniciar.place(x=250,y=350)


root.mainloop()


