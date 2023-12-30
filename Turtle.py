#######################
# Importaciones
#######################

#Importar turtle = import turtle

#######################
# Fin Importaciones
#######################

#######################
# Instrucciones
#######################

#Configurar Dimensiones de pantala = turtle.setup(600,600)
#Cambiar velocidad de dibujado = turtle.speed(0)
#Cambiar ancho de dibujo = turtle.width(6)
#Cambiar el color del fondo = turtle.bgcolor("black")
#Cambiar el color de la linea = turtle.color("white") #Linea Blanca
#Avanza 100px hacia adelante = turtle.forward(100) 
#gira 90 grados hacia la derecha = turtle.right(90) 
# Deja de escribir = turtle.up() 
#Comienza a escribir = turtle.down() 
#Comienza el rellenado (Recordar cerrarlo) = turtle.begin_fill() 
#Termina el rellenado = turtle.end_fill()
# Dibujar un circulo de 10px de diametro = turtle.circle(10)
#Esconde la tortuga = turtle.hideturtle()
#Cierra cuando el usuario da click = turtle.exitonclick() 

#######################
# Fin Instrucciones
#######################

#######################
# Funciones
#######################

'''
Dibujar con teclado
'''

#wn=turtle.Screen()
#def arriba():
#	turtle.forward(100)
#def abajo():
#	turtle.right(180)
#	turtle.forward(100)
#def izquierda():
#	turtle.left(90)
#def derecha():
#	turtle.right(90)
#
#wn.listen()
#wn.onkeypress(arriba,"Up")
#wn.onkeypress(abajo,"Down")
#wn.onkeypress(izquierda,"Left")
#wn.onkeypress(derecha,"Right")
#
#while True:
#	wn.update()

'''
Dibujar Triangulos
'''

#final=0
#while final!=1:
#	for i in range(3):
#		turtle.forward(100) #Avanza 100px hacia adelante
#		turtle.left(120) #gira 90 grados hacia la derecha
#	turtle.forward(20)
#	final = final+1
#turtle.exitonclick()

'''
Dibujar Poligonos
'''

#final=0
#lado = 25
#cantLados = 10
#while final!=1:
#	for i in range(cantLados):
#		turtle.forward(lado) #Avanza 100px hacia adelante
#		turtle.left(360/cantLados) #gira 90 grados hacia la derecha
#	turtle.forward(20)
#	final = final+1
#turtle.exitonclick()

'''
Dibujar Circulo de Color
'''

#turtle.begin_fill() 
#turtle.color("red")
#turtle.circle(10)
#turtle.end_fill()
#turtle.hideturtle()

'''
Dibujar Espiral
'''

#final=0
#giro=120
#while final!=3:
#	for i in range(3):
#		turtle.forward(100) #Avanza 100px hacia adelante
#		turtle.left(giro) #gira 90 grados hacia la derecha
#	turtle.left(giro+10)
#	final = final+1
#turtle.exitonclick()

'''
Dibujar Espiral Cuadrada
'''

#for i in range(110):
#	turtle.forward(i*5)
#	turtle.right(90)
#	turtle.Screen().exitonclick()

'''
Dibujo Aleatorio
'''

#forward=random.randint(50,100)
#right=random.randint(10,380)
#for i in range(10):
#	turtle.forward(forward)
#	turtle.right(right)

'''
Dibujo con Circulos
'''

#diametro=10
#for i in range(5):
#	turtle.circle(diametro)
#	turtle.right(90)
#	diametro=diametro+1
#turtle.exitonclick() 

'''
Dibujar Fractal
'''

#final=0
#lado = 25
#cantLados = 3
#while final!=3:
#	for i in range(cantLados):
#		turtle.forward(lado) #Avanza 100px hacia adelante
#		turtle.left(360/cantLados) #gira 90 grados hacia la derecha
#	turtle.left(20)
#	final = final+1
#turtle.exitonclick()

#######################
# Fin Funciones
#######################
