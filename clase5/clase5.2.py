class animal():
    def hablar(self):
        print("Que idiomas quieres?")

class gato(animal):
    def hablar(self):
        print("miauu")

class perro(animal):
    def hablar(self):
        print("guauu")

def escucharMascota(animal):
    animal.hablar()

if __name__ == "__main__":
    g = gato()
    p = perro()
    g.hablar()
    p.hablar()



class Persona():
    def __init__(self):
        self.cedula = 8725454263
    def mensaje(self):
        print("mensaje desde la clase persona")

