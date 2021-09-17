import json 

#definimos nodo raiz 
data = {}

#definimos nodos 
data ["clientes"] = []

#cargo los datos 
data ["clientes"].append({
    "nombre" : "Eddison", 
    "primer_apellido" :"Hernandez",
    "pin" : 2754,
    "saldo" : 23.25})

#guardar datos en archivo 
with open("data_proyecto.json", "w") as file:
    json.dump(data, file, indent=4) 