import random
import constantes
from type_enemy import EnemigoRapido, EnemigoPesado, EnemigoNormal

def Gen_Ene_borde(jugador_pos):
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

    # Elegir un tipo de enemigo aleatorio
    tipo_enemigo = random.choice(["normal", "rapido", "pesado"])
    
    if tipo_enemigo == "normal":
        return EnemigoNormal(x, y)
    elif tipo_enemigo == "rapido":
        return EnemigoRapido(x, y)
    else:  # pesado
        return EnemigoPesado(x, y)
