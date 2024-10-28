import random
import constantes
from type_enemy import EnemigoRapido, EnemigoPesado, EnemigoNormal,EnemigoMinijefe

def Gen_Ene_borde(jugador_pos,oleada):
    lado = random.choice(["izquierda", "derecha", "arriba", "abajo"])

    # Generar coordenadas en el borde
    if lado == "izquierda":
        x, y = 0, random.randint(0, constantes.ALTO_VENTANA - 40)
    elif lado == "derecha":
        x, y = constantes.ANCHO_VENTANA - 40, random.randint(0, constantes.ALTO_VENTANA - 40)
    elif lado == "arriba":
        x, y = random.randint(0, constantes.ANCHO_VENTANA - 40), 0
    else:  # abajo
        x, y = random.randint(0, constantes.ANCHO_VENTANA - 40), constantes.ALTO_VENTANA - 40
    # minijefe
    if oleada % 3 == 0 :
        return EnemigoMinijefe(x,y)
    # condicion minijefe
    if oleada % 4 == 0:
        return EnemigoMinijefe(x,y)
    # tipo de enemigo en funcion de la oleada
    if oleada >= 2 :
        tipo_enemigo = random.choices(["normal", "rapido", "pesado"],probabilidad = [1,min(oleada-1,2),min(oleada-2,3)])[0]
    else:
        tipo_enemigo = "normal"

    # Elegir un tipo de enemigo aleatorio
    tipo_enemigo = random.choice(["normal", "rapido", "pesado"])

    if tipo_enemigo == "normal":
        return EnemigoNormal(x, y)
    elif tipo_enemigo == "rapido":
        return EnemigoRapido(x, y)
    else:  # pesado
        return EnemigoPesado(x, y)
    
def detectar_colisiones(enemigos):
    for i, enemigo1 in enumerate(enemigos):
        for enemigo2 in enemigos[i + 1:]:
            if enemigo1.rect.colliderect(enemigo2.rect):
                resolver_colision(enemigo1, enemigo2)

def resolver_colision(enemigo1, enemigo2):
    # Aquí defines cómo separarlos. Un ejemplo simple:
    desplazamiento = enemigo1.rect.centerx - enemigo2.rect.centerx
    if desplazamiento > 0:
        enemigo1.rect.x += 5  # Se mueve hacia la derecha
        enemigo2.rect.x -= 5  # Se mueve hacia la izquierda
    else:
        enemigo1.rect.x -= 5
        enemigo2.rect.x += 5
