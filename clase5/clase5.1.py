class gato():
    def hablar(self):
        print("miauu")

class perro():
    def hablar(self):
        print("guauu")

def escucharMascota(animal):
    animal.hablar()

if __name__ == "__main__":
    g = gato()
    p = perro()
    g.hablar()
    p.hablar()


