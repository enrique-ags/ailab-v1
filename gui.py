from tkinter import *
from tkinter import messagebox

from click import command

from juego import Juego

def openNewWindow():     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(ventana)
    newWindow.title("Create new user")
    newWindow.geometry("300x500")
    newWindow.config(bg='#FAEBD7')
    l3 = Label(newWindow,text='Type new user: ')
    l3.place(x=10,y=5)
    l4 = Label(newWindow,text='Type password: ')
    l4.place(x=10,y=35)
    l5 = Label(newWindow,text='Confirm password: ')
    l5.place(x=10,y=65)
    e3 = Entry(newWindow)
    e3.place(x=130,y=5)
    e4 = Entry(newWindow,show='*')
    e4.place(x=130,y=35)
    e5 = Entry(newWindow,show='*')
    e5.place(x=130,y=65)  
    #buttons
    b4 = Button(newWindow, text='Acceder')
    b4.place(x=10, y = 95)
    b5 = Button(newWindow, text='Cancelar', command=newWindow.destroy)
    b5.place(x=90, y = 95)



ventana = Tk()
ventana.geometry("800x600")
ventana.title("GameZone")
ventana.config(bg='#D0E4F5')


#entrada de los datos

l1 = Label(ventana, text='Usuario')
l1.place(x=10,y=5)
l1.config(bg='#D0E4F5',font='Courier')
e1 = Entry(ventana)
e1.place(x=11,y=26)
e1.config(font='Courier')

l2 = Label(ventana, text='Contraseña')
l2.place(x=10,y=50)
l2.config(bg='#D0E4F5',font='Courier')

e2 = Entry(ventana,show='*')
e2.place(x=10,y=69)
e2.config(font='Courier')

b1 = Button(ventana, text='Acceder')
b1.place(x=10, y = 95)

b2 = Button(ventana, text='Cancelar', command=ventana.destroy)
b2.place(x=90, y = 95)

b3 = Button(ventana, text='New User', command=openNewWindow)
b3.place(x=160, y = 95)


p = Juego()
adminExist = p.validAdministradorExist()
if adminExist:
    print('Admin exists')
else:
    MsgBox = messagebox.askquestion ('Admin not created','Seems it´s first time running game, create admin?',icon = 'question')
    if MsgBox=='yes':
        result=p.creadAdminUser('10','10','10')
        if result:
            messagebox.showinfo('gamer zone','Admin created succesfully!')

ventana.mainloop()


