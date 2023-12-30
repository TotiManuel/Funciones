#region Letras
'''
hola="hola"
print(hola.upper()) #Mayusculas
print(hola.lower()) #Minusculas
print(hola.isupper()) #true o false depende si es mayuscula
print(hola.capitalize()) #capitaliza la palabra
print(hola.swapcase())
print(hola.title())
print(hola)
print(len(hola)) # muestra la longitud de la cadena
print(hola[0:4]) # muestra de la posicion 0 a la 4
print(hola[2:4]) # muestra de la posicion 2 a la 4
hola=hola.replace("o" , "a") # reemplaza un caracter por otro
'''
#endregion
# DIVISION

'''
for letter in hola:
	print(letter)
'''
# DIVISION

'''
cadena1=input("cadena 1 >> ")
cadena2=input("cadena 2 >> ")
if(len(cadena1)>len(cadena2)):
	print(cadena1 + " es mayor")
elif(len(cadena2)>len(cadena1)):
	print(cadena1 + " es mayor")
else:
	print("las cadenas son iguales")
'''

'''
subcadena = "zz"
cadena = "hola mundo"
print(cadena.find(subcadena)) # si no existe te muestra un -1

subcadena = "hola"
cadena = "hola mundo"
print(subcadena in cadena)

google = "google"
print(google.find("l"))
'''
'''
cadena = "arriba la birra birra"
print(cadena.count("birra")) # cantidad de veces que encuentra la palabra
print(cadena.split()) # hace una lista separando cada palabra
cadena=cadena.replace(" ", "") 
if(cadena==cadena[::-1]): # lee de atras hacia adelante para ver si son iguales
	print("es palindromo")
else:
	print("no lo es")

nombre = "julian"
print(f"{nombre} tiene {len(nombre)} letras")
'''
#region filas/columnas
filas = [1,"toti",3,9]
columnas = [["x"]*2]*3
filas.append("juli")
print(filas)
filas.pop(2)
print(filas)
filas.reverse()
#filas.sort() # ordena numeros o letras
print(filas)
print(columnas)
print(filas[1:3])

x=0
for elementos in filas[1:3]:
	x = x+1
	print(f"el elementos {x} de la lista es {elementos}")

#endregion











