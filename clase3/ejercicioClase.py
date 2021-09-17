print("Clase #1")

class Persona: 
    def __init__(self, nombreParam, CUIparam, generoParam, nacionalidadParam):
        self.nombre = nombreParam
        self.CUI = CUIparam
        self.genero = generoParam
        self.nacionalidad = nacionalidadParam

persona1 = Persona("Eddison","589754890101", "Masculino", "Guatemalteca")
persona2 = Persona("Wilson","585888890101", "Masculino", "Guatemalteca")

print("Bienvenido", persona1.nombre, "de nacionalidad", persona1.nacionalidad)
print("Bienvenido", persona2.nombre, "de nacionalidad", persona2.nacionalidad)

print()


print("Clase #2")

class SalonDeClases:
    def __init__(self, SalonParam, EscritoriosParam, AreaDelSalonParam, ProyectoresParam):
        self.salon = SalonParam
        self.escritorios = EscritoriosParam
        self.area = AreaDelSalonParam
        self.proyectores = ProyectoresParam 

salon1 = SalonDeClases("C2", "54 Escritorios", "15m2", "2 Proyectores")
salon2 = SalonDeClases("A3", "30 Escritorios", "12m2", "1 Proyector")
salon3 = SalonDeClases("E1", "20 Escritorios", "10m2", "1 Proyector")

print("Bienvenido al salón", salon1.salon, "el cual tiene", salon1.escritorios, "Su area es de:", salon1.area, "Escritorios", salon1.proyectores)
print("Bienvenido al salón", salon2.salon, "el cual tiene", salon2.escritorios, "Su area es de:", salon2.area, "Escritorios", salon2.proyectores)
print("Bienvenido al salón", salon3.salon, "el cual tiene", salon3.escritorios, "Su area es de:", salon3.area, "Escritorios", salon3.proyectores)


print ()



print("Clase 3")

class CursosIngrenieriaPrimerSemestreUSPG:
    def __init__(self, NombreDelCursoParam, HorarioParam, CatedraticoParam, CedeParam):
        self.Curso = NombreDelCursoParam
        self.horario = HorarioParam
        self.catedratico = CatedraticoParam
        self.cede = CedeParam

curso1 = CursosIngrenieriaPrimerSemestreUSPG("Fisica", "11:30 a 12:45", "Crystal Muñoz", "Central")
curso2 = CursosIngrenieriaPrimerSemestreUSPG("Matematicas", "07:10 a 09:30", "Alvaro Sanchez", "Central")
curso3 = CursosIngrenieriaPrimerSemestreUSPG("Comunicacion Oral", "15:30 a 17:40", "Mantha Salazar", "Central")

print("Bienvenido al curso", curso1.Curso, "con horario de:", curso1.horario, "Catedratico a cargo", curso1.catedratico, "en la cede", curso1.cede)
print("Bienvenido al curso", curso2.Curso, "con horario de:", curso2.horario, "Catedratico a cargo", curso2.catedratico, "en la cede", curso2.cede)
print("Bienvenido al curso", curso3.Curso, "con horario de:", curso3.horario, "Catedratico a cargo", curso3.catedratico, "en la cede", curso3.cede)

print()


print("Clase #4")

class PersonalAdministrativo:
    def __init__(self, NombreParam, EdadParam, CodigoDeEmpleadoParam, AreaLaborarParam):
        self.Nombre = NombreParam
        self.edad = EdadParam
        self.codigoDeEmpleado = CodigoDeEmpleadoParam
        self.AreaLaboral = AreaLaborarParam

trabajador1 = PersonalAdministrativo("Carlos Muñoz", "25 años", "10097012", "Contaduria")
trabajador2 = PersonalAdministrativo("Patricio Estrella", "30 años", "10011225", "Reclutamiento")

print("Hola, mi nombre es ", trabajador1.Nombre, " tengo ", trabajador1.edad, " y me identifico con el numero: ", trabajador1.codigoDeEmpleado, " y pertenezco al area de ", trabajador1.AreaLaboral)
print("Hola, mi nombre es ", trabajador2.Nombre, " tengo ", trabajador2.edad, " y me identifico con el numero: ", trabajador2.codigoDeEmpleado, " y pertenezco al area de ", trabajador2.AreaLaboral)

print()


print("Clase 5")

class Pizarras:
    def __init__(self, tamañoParam, AulaParam, EstadoParam):
        self.tamaño = tamañoParam
        self.aula = AulaParam
        self.estado = EstadoParam

pizarra1 = Pizarras("2m x 3m", "D4", "Buena")
pizarra2 = Pizarras("3m x 3m", "F5", "Aceptable")
pizarra3 = Pizarras("1m x 1m", "E2", "Mala")

print("Esta ubicada en el salón", pizarra1.aula, "con un tamaño de", pizarra1.tamaño, " y en una condicion", pizarra1.estado)
print("Esta ubicada en el salón", pizarra2.aula, "con un tamaño de", pizarra2.tamaño, " y en una condicion", pizarra2.estado)
print("Esta ubicada en el salón", pizarra3.aula, "con un tamaño de", pizarra3.tamaño, " y en una condicion", pizarra3.estado)

print()


print("Clase 6")

class CrearCuenta:
    def __init__(self, NombreParam, DPIParam, PINParam):
        self.nombre = NombreParam
        self.DPI = DPIParam
        self.PIN = PINParam

usuario1 = CrearCuenta("Eddison Hernandez", "125487961010", "8561")
usuario2 = CrearCuenta("Wilson Peñate", "128888961010", "1022")
usuario3 = CrearCuenta("Matias Posada", "784562123010", "8899")

print("Bienvenido", usuario1.nombre, "Tu PIN es", usuario1.PIN)
print("Bienvenido", usuario2.nombre, "Tu PIN es", usuario2.PIN)
print("Bienvenido", usuario3.nombre, "Tu PIN es", usuario3.PIN)




