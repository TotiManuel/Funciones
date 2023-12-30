from Figuras.cuadrado import area_cuadrado, perimetro_cuadrado
from Figuras.circulo import area_circulo, perimetro_circulo

lado = 4
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}
print("cuadrado: ", cuadrado)

radio = 5
circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}

print(circulo)