class Usuario:
  def __init__(self, nombreParam, pinParam, cuentaParam, saldoParam):
    self.nombre = nombreParam
    self.pin = pinParam
    self.cuenta = cuentaParam
    self.saldo = saldoParam
    self.activo = True

  def desactivar(self):
    self.activo = False

  def debitar(self, cantidad):
    if self.activo:
      self.saldo = self.saldo - cantidad

  def acreditar(self, cantidad):
    if self.activo:
      self.saldo = self.saldo + cantidad



usuario1 = Usuario("Mynor", "1234", "002568745", 10000)
usuario2 = Usuario("Luis", "4321", "554651323", 1000)

#print(usuario1.activo)
print("Bienvenido ", usuario1.nombre)

print("Su saldo es ", usuario1.saldo)

usuario1.debitar(5000)

usuario1.desactivar()

usuario1.debitar(1000)

print("Su saldo es ", usuario1.saldo)

#usuario1.desactivar()

#print(usuario1.activo)

