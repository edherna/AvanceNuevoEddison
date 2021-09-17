class Persons:
    def __init__(self):
        self.nombre=""
        self.edad=0
  
    def SetDatos(self,Datonombre,edad):
        self.nombre=Datonombre
        self.edad=edad
  
    def getDatos(self):
        print(self.nombre ,self.edad )
        print()
   