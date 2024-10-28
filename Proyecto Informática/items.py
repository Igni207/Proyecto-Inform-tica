#import pygame.sprite

#class Item(pygame.sprite.Sprite):
    #def __init__(self, x, y, item_type,):
        #pygame.sprite.Sprite.__init__(self)
        #h = k = 30
        #self.item_type = item_type # 1= moneda,  2= pocion de vida
        #self.imagen = pygame.image.load ("imagenes\coin.png")
        #if self.item_type == 1:
            #self.imagen = pygame.image.load ("E://Proyecto-Inform-tica-PINFOAlphaV0.0.2//Proyecto Informática//imagenes//coin")
            #self.imagen = pygame.transform.scale(self.imagen, (h, k))
        #if self.item_type == 2:
            #self.imagen = pygame.image.load ("E://Proyecto-Inform-tica-PINFOAlphaV0.0.2//Proyecto Informática//Imagenes//pocion_vida")
            #self.imagen = pygame.transform.scale(self.imagen, (h, k))
        #self.rect = self.imagen.get_rect()
        #self.rect = (x, y, h, k)

    #def dibujar(self, ventana):
        #ventana.blit(self.imagen, self.rect.topleft)


import pygame
#mi personaje
class Item:
    def __init__(self, x, y, item_type):
        h = k = 50
        self.rect = pygame.Rect(x, y, h, k)
        self.item_type = item_type
        if item_type == 1:
            self.sprite = pygame.image.load('E://Proyecto-Inform-tica-PINFOAlphaV0.0.3//Proyecto Informática//imagenes//monedas.png')  # Cargar el sprite
            self.sprite = pygame.transform.scale(self.sprite, (h, k))  # Cambiar el tamaño según sea necesario
        if item_type == 2:
            self.sprite = pygame.image.load('E://Proyecto-Inform-tica-PINFOAlphaV0.0.3//Proyecto Informática//imagenes//pocion_vida.png')
            self.sprite = pygame.transform.scale(self.sprite, (h, k))  # Cambiar el tamaño según sea necesario
        #self.sprite = pygame.image.load('E://Proyecto-Inform-tica-PINFOAlphaV0.0.2//Proyecto Informática//Imagenes//coin.png')  # Cargar el sprite
        #self.sprite = pygame.transform.scale(self.sprite, (h, k))  # Cambiar el tamaño según sea necesario
        #self.sprite = pygame.image.load('E://Proyecto-Inform-tica-PINFOAlphaV0.0.2//Proyecto Informática//Imagenes//pocion_vida.png')

    def dibujar(self, ventana):
        ventana.blit(self.sprite, self.rect.topleft)
