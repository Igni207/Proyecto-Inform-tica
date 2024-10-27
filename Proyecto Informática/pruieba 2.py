import pygame
import math
import random
import jugador

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((10, 5))  
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10  
        self.direction = direction  

    def update(self):
        self.rect.x += self.speed * math.cos(self.direction)
        self.rect.y += self.speed * math.sin(self.direction)
        if not (0 <= self.rect.x <= 800 and 0 <= self.rect.y <= 600):
            self.kill()

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, color, speed, vida=1):
        super().__init__()
        self.image = pygame.Surface((30, 30))  
        self.image.fill(color)  
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed  
        self.vida = vida  

    def update(self, jugador):
        dx = jugador.rect.centerx - self.rect.centerx
        dy = jugador.rect.centery - self.rect.centery
        angle = math.atan2(dy, dx)

        self.rect.x += self.speed * math.cos(angle)
        self.rect.y += self.speed * math.sin(angle)

        if self.rect.y > 600:
            self.kill()

    def recibir_dano(self):
        self.vida -= 1
        if self.vida <= 0:
            self.kill()  
            return True  
        return False  

class Moneda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))  
        self.image.fill((255, 255, 255))  
        self.rect = self.image.get_rect(center=(x, y))

class Jugador:
    def __init__(self, x, y):
        h = k = 50
        self.rect = pygame.Rect(x, y, h, k)
        self.vida = 3
        self.sprite = pygame.image.load('Proyecto Informática\imagenes\soldi.png')  # Cargar el sprite
        self.sprite = pygame.transform.scale(self.sprite, (h, k))  # Cambiar el tamaño según sea necesario

    '''def update(self, keys):
        speed = 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
        if keys[pygame.K_UP]:
            self.rect.y -= speed
        if keys[pygame.K_DOWN]:
            self.rect.y += speed'''
    
    def dibujar(self, ventana):
        ventana.blit(self.sprite, self.rect.topleft)

    def movimiento(self,delta_x,delta_y):
        self.rect.x = self.rect.x + delta_x
        self.rect.y = self.rect.y + delta_y 

    def perder_vida(self):
        self.vida -= 1
        if self.vida <= 0:
            print("¡El jugador ha perdido todas sus vidas!")
            pygame.quit()
            exit()

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36) 

jugador = Jugador(300, 400)
jugador_group = pygame.sprite.Group(jugador)
proyectiles_group = pygame.sprite.Group()
enemigos_group = pygame.sprite.Group()
monedas_group = pygame.sprite.Group()

monedas_recogidas = 0

def generar_enemigos():
    tipo_enemigo = random.random()
    if tipo_enemigo < 0.05:  
        x, y = random.randint(0, 800), random.randint(-100, -40)
        enemigo = Enemigo(x, y, (0, 0, 255), speed=4)  # enemigo azul, rápido
    elif tipo_enemigo < 0.30:  
        x, y = random.randint(0, 800), random.randint(-100, -40)
        enemigo = Enemigo(x, y, (128, 0, 128), speed=1, vida=3)  # enemigo morado, lento y con más vida
    else:
        x, y = random.randint(0, 800), random.randint(-100, -40)
        enemigo = Enemigo(x, y, (255, 255, 0), speed=2)  # enemigo amarillo estándar

    enemigos_group.add(enemigo)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - jugador.rect.centerx
                dy = mouse_y - jugador.rect.centery
                direction = math.atan2(dy, dx)  

                proyectil = Proyectil(jugador.rect.centerx, jugador.rect.centery, direction)
                proyectiles_group.add(proyectil)

    if random.random() < 0.02:  # generacion de enemigos
        generar_enemigos()

    keys = pygame.key.get_pressed()
    jugador_group.update(keys)
    proyectiles_group.update()
    enemigos_group.update(jugador)
    monedas_group.update()

    for proyectil in proyectiles_group:
        enemigos_golpeados = pygame.sprite.spritecollide(proyectil, enemigos_group, False)
        for enemigo in enemigos_golpeados:
            if enemigo.recibir_dano():  
                if random.random() < 0.20:  # 20% para soltar una moneda (aumentar o bajar la probabilidad del droprate)
                    moneda = Moneda(enemigo.rect.centerx, enemigo.rect.centery)
                    monedas_group.add(moneda)
            proyectil.kill()  

    colisiones_jugador = pygame.sprite.spritecollide(jugador, enemigos_group, True)
    if colisiones_jugador:
        jugador.perder_vida()

    colisiones_monedas = pygame.sprite.spritecollide(jugador, monedas_group, True)
    monedas_recogidas += len(colisiones_monedas)

    if monedas_recogidas >= 7: #condición de victoria
        print("¡Has recogido 7 monedas! ¡Ganaste!")   ##################################### ERROR, NO SE MUESTRA EL PRINT PORQUE EL JUEGO SE CIERRA AL INSTANTE ############################## 
        running = False 

    screen.fill((0, 0, 0))  
    jugador_group.draw(screen)
    proyectiles_group.draw(screen)
    enemigos_group.draw(screen)
    monedas_group.draw(screen)

    vidas_texto = font.render(f"Vidas: {jugador.vida}", True, (255, 255, 255))
    monedas_texto = font.render(f"Monedas: {monedas_recogidas}", True, (255, 255, 255))
    screen.blit(vidas_texto, (10, 10))
    screen.blit(monedas_texto, (10, 50))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
