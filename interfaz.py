
import pygame
import constantes

#Intento de Corazones

class BarraVida:
    def __init__(self, vida_max, pos):
        self.vida_max = vida_max
        self.vida_actual = vida_max
        self.pos = pos
        #cargo las imagenes, las podemos cambiar sin drama
        self.vida_full = pygame.image.load("imagenes/corazon_vivo.png")
        self.vida_vacia = pygame.image.load("imagenes/corazon_muerto.png")
        #tamañooo
        self.vida_full = pygame.transform.scale(self.vida_full, (40, 40))
        self.vida_vacia= pygame.transform.scale(self.vida_vacia, (40, 40))
    def dibujo_cor(self, screen):
        for i in range (self.vida_max):
            if i < self.vida_actual:
                #para q salgan en la pantalla principal
                screen.blit(self.vida_full, (self.pos[0] + i * 50, self.pos[1]))
            else:
                screen.blit(self.vida_vacia, (self.pos[0] + i * 50, self.pos[1]))
    #recibir daño
    def recibir_daño(self):
        if self.vida_actual > 0:
            self.vida_actual -=1
            

class ContadorOleadas:
    def __init__(self, pos):
        self.oleada = 1 #primera oleada
        self.pos = pos
        self.fuente = pygame.font.Font("Fuente/AncientModernTales-a7Po.ttf", 40)
    def siguiente_oleada(self):
        self.oleada += 1 #contador de oleadas
    def dibujar(self, screen):
        texto_oleada = self.fuente.render(f"Oleada: {self.oleada}", True, (255, 255, 255))
        screen.blit(texto_oleada , self.pos)

class ContadorMonedas:
    def __init__(self, pos):
        self.monedas = 0
        self.pos = pos
        self.fuente = pygame.font.Font("Fuente/AncientModernTales-a7Po.ttf", 40)
    
    def recoger_moneda(self):
        self.monedas += 1  #contador de monedas 
    
    def dibujar(self, screen):
        texto_monedas = self.fuente.render(f"Monedas: {self.monedas}", True, (255, 255, 225)) 
        screen.blit(texto_monedas, self.pos)


