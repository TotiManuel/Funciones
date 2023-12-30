class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños #{self.edad} {self.nombre}")

class Empleado(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def trabajar(self, horas_trabajadas):
        self.horas_totales = horas_trabajadas * 5
        print(f"{self.nombre}, trabajo {horas_trabajadas} horas")
        print(f"Horas Totales: {self.horas_totales}")

paco = Empleado(nombre="paco", edad=20)
paco.trabajar(horas_trabajadas=8)
paco.cumplir_anios()