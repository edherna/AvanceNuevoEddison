class Usuario:
  def __init__(self, nombre, pin, cuenta, saldo):
    self.nombre = nombre
    self.pin = pin
    self.cuenta = cuenta
    self.saldo = saldo
    self.activo = True

    def desactivar(self):
    self.activo = False

    def debitar(self, cantidad):
        self.saldo = self.saldo - cantidad
    
    def acreditar(self, cantidad):
        self.saldo = self.saldo + cantidad

usuario1 = Usuario("Eddison", "1234", "5897456215", "10000")

print(usuario1.activo)
print("Bienvenido", usuario1.nombre)

#usuario1.desactivar()

#print(usuario1.activo)

