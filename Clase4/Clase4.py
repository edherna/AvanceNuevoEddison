class Persona:
    def __init__(self, nombre, dpi):
        self.nombre = nombre 
        self.dpi = dpi

    def hablar(self, *palabras):
        for frase in palabras: 
            print (self.nombre, ":", frase)

luis = Persona("Luis", "548798457454")
luis.hablar("hola", "soy Luis", "mucho gusto.")

class Cuentahabiente(Persona):
    def __init__(self, cuenta, saldo, nombre):
        self.numeroCuenta = cuenta 
        self.saldo = saldo
        self.nombre = nombre

    def consultarSaldo(self):
        return self.saldo

Cuentahabiente1 = Cuentahabiente("2334343424", 0, "Mario")
Cuentahabiente1.nombre = "Mario"
Cuentahabiente1.dpi = "111111111111"
saldo = Cuentahabiente1.consultarSaldo()
print(Cuentahabiente1.nombre, "Tu saldo es", saldo)

