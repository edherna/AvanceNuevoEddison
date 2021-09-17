from ProectoParcial import CuentaHabientes
from Clases import ManejadorArchivos

print("Cajero Bancario")

Validador=input("Posee un usuario")
NuevoUsuario=ManejadorArchivos.CreadorUsuario()

if Validador.upper() =="NO":
  print("crear usuario")
  Nombre=input("ingrese nombre")
  Apellido=input("ingrese Apellido")
  pin=int(input("ingrese Contraseña"))
  Saldo=int(input("ingrese Primer Deposito"))
  NuevoUsuario.NuevoUsuario(Nombre,Apellido,pin,Saldo)
  NuevoUsuario.VerUsuarios()
elif Validador.upper() =="SI":
  print("Bienvenido")
#Ejemplo de objeto
trabajdor1=EjemploHerencia.CuentaHabientes()
trabajdor1.SetCuentaHabientes("holi","shit",12,1234564123)
trabajdor1.GetCuentaHabientes()