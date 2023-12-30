#####################
# Importaciones
#####################
import pygame

#####################
# Defino Colores
#####################
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)

#####################
# Configuraciones del juego
#####################
pygame.init()

dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi primer juego con pygame")

hecho = False

reloj = pygame.time.Clock() #se usa para ver cuan rapido se actualiza la pantalla
#####################
# dibujos del programa
#####################
pantalla.fill(BLANCO) # Pone la pantalla en el color deseado
pygame.draw.rect(pantalla, VERDE, (100, 50, 100,50)) #Dibuja un rectangulo (Lugar, Color, ejes, dimenciones)
pygame.draw.line(pantalla, NEGRO, (100, 104), (199,104), 10) #Dibuja una linea (Lugar, Color, ejex,inclinacion izquierda,teminacion, inclinacion derecha, ancho en pixel)
pygame.draw.circle(pantalla, VERDE, (122,250), 20,0)#Dibuja un circulo (Lugar, Color, ejes, radio, vacio)
pygame.draw.ellipse(pantalla, VERDE, (275,200, 40,80))#Dibuja un circulo (Lugar, Color, ejes, radio, vacio)
#####################
# Bucle principal del programa
#####################
while not hecho:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			hecho = True
	pygame.display.update() #Va actualizando la pantalla
pygame.QUIT()
