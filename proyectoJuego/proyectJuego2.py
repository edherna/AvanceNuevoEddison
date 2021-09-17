import json
import os 

data={}
data["jugadores"]=[]
data["jugadores"].append({
    "nombre" : "Eddison",
    "apellido" : "Hernandez",
    "usuario" : "edherna",
    "contraseña": 1234
})

with open("data_proyectoJuego.json", "w") as file:
    json.dump(data, file, indent=4) 

DeterminarArch= os.path.exists("data_proyectoJuego.json")
if DeterminarArch == True:
  pass
else:
    print("no hay juego")


