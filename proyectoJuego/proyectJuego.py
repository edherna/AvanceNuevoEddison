print("Inventario parte #1")
OPTIONS: 0
def menu():
    print("0. Cargar")
    print("1. Productos en bodega")
    print("2. Total de productos todas las bodegas")
    print("3.Promedio de productos ingresados al mes")
    print("4. Con más existencias en una bodega")
    print("5.Productos en una bodega CSV")
    print("6.Productos por bodega HTML")
    print("7.Salir")

def ContarTodo():
    f=open("inventarioData.txt","r")
    lines= f.readlines()
    data = []
    for item in lines:
        item = item.replace("\n","").replace("\r","")
        linea = item.split("|")
        data.append(linea)
    TAMAÑO = len(data)
    return TAMAÑO

def PROMEDIO():
    f=open("inventarioData.txt","r")
    lines= f.readlines()
    data = []
    contador2= 0

    for item in lines:
        item = item.replace("\n","").replace("\r","")
        linea = item.split("|")
        data.append(linea)

    for d in data:
        if int(d[2]) > 0:
            contador2 = int(d[2]) + contador2
    promedio = contador2 / 12
    return promedio

def bodega1001():
  f=open("inventarioData.txt","r")
  lines= f.readlines()
  data = []
  contador=0
  contador2 = 0
  contador3 = 0 
  bodega = input("Ingrese el numero de bodega: ")

  for item in lines:
      item = item.replace("\n","").replace("\r","")
      linea = item.split("|")
      data.append(linea)
  for dato in data:
    if dato[0] == bodega:
      if "1001" == dato[1]:
          contador= contador + int(dato[2])
      elif "1002" == dato[1]:
          contador2= contador2 + int(dato[2])
      elif "1003" == dato[1]:
          contador3= contador3 + int(dato[2])
  if contador > contador2 and contador > contador3:
      bodega1001 = "Mayor existencia es de 1001"
      return bodega1001
  elif contador2 > contador and contador2 > contador3:
      bodega1001 = "Mayor existencia es de 1002"
      return bodega1001
  elif contador3 > contador and contador3 > contador2:
      bodega1001 = "Mayor existencia es de 1003"
      return bodega1001
def invecsv():
  f=open("inventarioData.txt","r")
  lines= f.readlines()
  f.close()

  f=open("inventarioEddison.csv","a+")
  data = []
  bodega = input("Ingrese el numero de bodega: ")

  for item in lines:
      item = item.replace("\n","").replace("\r","")
      linea = item.split("|")
      data.append(linea)
  for dato in data:
    if dato[0] == bodega:
       f.write(dato[0]+";"+dato[1]+";"+dato[2]+";"+dato[3]+";"+dato[4]+";"+dato[5]+"\n")
  f.close()

def MiHTML ():
        f=open("inventarioData.txt","r")
        lines= f.readlines()
        f.close()

        f=open("inventarioEddison.html","a+")
        Estructura1 = """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <style type="text/css">
                body {font-family: 'Times New Roman';}
                
                table {     font-family: "Times New Roman", "Times New Roman", Sans-Serif;
                    font-size: 12px;    margin: 45px;     width: 480px; text-align: left;    border-collapse: collapse; }
                
                th {     font-size: 13px;     font-weight: normal;     padding: 8px;     background: #021b6b;
                    border-top: 4px solid #03208a;    border-bottom: 1px solid #fff; color: rgb(239, 241, 247); }
                
                td {    padding: 8px;     background: #e8edff;     border-bottom: 1px solid #fff;
                    color: rgb(4, 4, 90);    border-top: 1px solid transparent; }
                
                tr:hover td { background: #d0dafd; color: #339; }
                </style>
        </head>
        <body>
            <table >
                <caption>TABLA DE BODEGA 1</caption>
                <!-- Estos son los encabezados -->
                <tr> 
                    <th>Codigo de Bodega</th> 
                    <th>Codigo de producto</th> 
                    <th>Cantidad de producto</th> 
                    <th> Dia Calendario</th>
                    <th>Mes</th> 
                    <th>Anio</th> 
                    <th>Dia de la semana</th>
                </tr>
                <!-- estas son las columnas  --> """
            
        f.write(Estructura1)
        data = []
        for item in lines:
            item = item.replace("\n","").replace("\r","")
            linea = item.split("|")
            data.append(linea)
        for dato in data:
            if dato[0] == "1":
                f.write(f"<tr> <td>{dato[0]}</td> <td>{dato[1]}</td> <td>{dato[2]}</td> <td>{dato[3]}</td> <td>{dato[4]}</td> <td>{dato[5]}</td> <td>{dato[6]}</td> </tr>")
        EstructuraDeCierre = """ </table>"""
        f.write(EstructuraDeCierre)
        Estructura2 = """    <table >
                <caption>TABLA DE BODEGA 2</caption>
                <!-- Estos son los encabezados -->
                <tr> 
                    <th>Codigo de Bodega</th> 
                    <th>Codigo de producto</th> 
                    <th>Cantidad de producto</th> 
                    <th> Dia Calendario</th>
                    <th>Mes</th> 
                    <th>Anio</th> 
                    <th>Dia de la semana</th>
                </tr>
                <!-- estas son las columnas  --> """
        f.write(Estructura2)
        for dato in data:
            if dato[0] == "2":
                f.write(f"<tr> <td>{dato[0]}</td> <td>{dato[1]}</td> <td>{dato[2]}</td> <td>{dato[3]}</td> <td>{dato[4]}</td> <td>{dato[5]}</td> <td>{dato[6]}</td> </tr>")

        EstructuraDeCierre3 = """ </table>"""
        f.write(EstructuraDeCierre3)
        Estructura4 = """<table >
                <caption>TABLA DE BODEGA 3</caption>
                <!-- Estos son los encabezados -->
                <tr> 
                    <th>Codigo de Bodega</th> 
                    <th>Codigo de producto</th> 
                    <th>Cantidad de producto</th> 
                    <th> Dia Calendario</th>
                    <th>Mes</th> 
                    <th>Anio</th> 
                    <th>Dia de la semana</th>
                </tr>
                <!-- estas son las columnas  -->"""

        f.write(Estructura4)
        for dato in data:
            if dato[0] == "3":
                f.write(f"<tr> <td>{dato[0]}</td> <td>{dato[1]}</td> <td>{dato[2]}</td> <td>{dato[3]}</td> <td>{dato[4]}</td> <td>{dato[5]}</td> <td>{dato[6]}</td> </tr>")

        EstructuraDeCierre4 = """ </table>"""
        f.write(EstructuraDeCierre4)


        EstructuraDeCierrehtml = """ </body> </html>"""
        f.write(EstructuraDeCierrehtml)
        f.close()

while True:
    menu()
    OPTIONS = int(input("Ingrese la oppcióon: "))
    if OPTIONS == 0:
        f=open("inventarioData.txt","r")
        f.seek(0)
        lines= f.readlines()
        dato = lines.split("|")
        f.close()
        print("Cargando, presione una tecla para continuar")
    elif OPTIONS == 1:
        f=open("inventarioData.txt","r")
        lines= f.readlines()

        data = []
        for item in lines:
            item = item.replace("\n","").replace("\r","")
            linea = item.split("|")
            data.append(linea)

        GrupoABuscar = int(input("Ingrese el codigo de bodega: "))
        contador = 0
        for i in data:
            if GrupoABuscar == int(i[0]):
                contador = contador + int(i[2])
        print("La cantidad de elementos encontrados son:", contador)
    elif OPTIONS == 2:
        CONT = ContarTodo()
        print("El total de productos todas las bodegas es:", CONT)
    elif OPTIONS == 3:
        PROM = PROMEDIO()
        print("El promedio de productos ingresados al mes es:", PROM)
    elif OPTIONS == 4:
        MAXIMO = bodega1001()
        print("Los productos Con más existencias en una bodega son:", MAXIMO)

    elif OPTIONS == 5:
        print("Los productos en una bodega CSV son:")
        invecsv()
    elif OPTIONS == 6:

        print("Los productos por bodega HTML:")
        MiHTML ()
    elif OPTIONS == 7:
        break
print("Fin del programa")









#modulo para importar  metodo abstracto 
from abc import ABC, abstractclassmethod
#herenicias de metodos Abstract
class ConceptAbstracBaseData(ABC):
  #decoradores para funciones abstractas CREAR
  @abstractclassmethod
  def CreatorUserDataBase():
    pass
  #decoradores para funciones abstractas ASIGNAR
  @abstractclassmethod
  def SetterUserData():
    pass   
  #decoradores para funciones abstractas OBTENER
  @abstractclassmethod
  def GetterUserData():
    pass









































