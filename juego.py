import csv
class Juego:

    def __init__(self):
        
        archivo = open('Usuario1.csv','a')
        with archivo:
            escritor = csv.writer(archivo)
        '''    escritor.writerows(a)'''

    def validAdministradorExist(self):
        flag=False
        with open('Usuario1.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for renglon in lector:
                 if len(renglon)>0:
                    if renglon[1] == '10':
                        flag = True
                    else:
                        flag= False
        return  flag
                  
    def creadAdminUser(self, userid,password,level):

        self.userid = '10'
        self.password = password
        self.level = level
        a = [['password','user','level'],[self.userid,self.password, self.level]]
        archivo = open('Usuario1.csv','a')
        try:
            with archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(a)
            return True
        except:
            return False





        


