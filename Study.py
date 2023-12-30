################################
def saludar(nombre):
    print(f"Hola, {nombre}")
saludar("julian")
################################

class Cachorro():
    def __init__(self, nombre, juguete):
        self.nombre = nombre
        self.juguete = juguete
        
    def jugar(self):
        print(self.nombre + " Esta jugando con el " + self.juguete)
        
Marbel = Cachorro("Marbel" , "Oso de peluche")
Marbel.jugar()

Onix = Cachorro("Onix" , "Pito de goma")
Onix.jugar()

##################################
import random

numeros = [1,2,3,4,5]
random.shuffle(numeros)
print(numeros)

numero = random.choice(numeros)
print(numero)
print(type(numero))
##################################

Lenguaje = "Python", "Html", "Java"
for elemento in Lenguaje:
    if elemento == "Html":
        continue
    print(elemento)

####################################
for element in range(5):
    print(element)

####################################
i = 10
while i <= 100:
    print(i)
    i=i+10

####################################

i = 1
while i <=5:
    print(i)
    i = i + 1
    if i == 3:
        break

####################################

Lenguaje = ["python", "java", "html"]
for index in range(len(Lenguaje)):
    print("Indice: ", index)
    print("Elemento: ", Lenguaje[index])

####################################

i = 0
while i < len(Lenguaje):
    print(Lenguaje[i])
    i=i+1

####################################

Diccionario = {
    "nombre": "python",
    "Creador": "Julian"
}

for llave in Diccionario:
    print("Llave: ", llave)
    print("Valor: ", Diccionario[llave])

####################################

for element in Diccionario.keys():
    print(element)

for element in Diccionario.values():
    print(element)

for element in Diccionario.items():
    print(element)

for llave, valor in Diccionario.items():
    print(llave, valor)

####################################

APELLIDO = "Mandaio"
def funcion():
    nombre="julian"
    print(nombre, APELLIDO)
    return "Toti"
funcion()
print(funcion())

####################################



####################################

####################################

####################################

####################################