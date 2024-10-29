from estructure_enemy import Enemigo
# enemigo pesado
class EnemigoPesado(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidad=1, vida=6)  #Menor velocidad y más vida

# enemigo normal
class EnemigoNormal(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidad=2, vida=3)  #Velocidad y vida para enemigos normales

# enemigo rapido
class EnemigoRapido(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidad=3, vida=1)  #Mayor velocidad y menos vida

class EnemigoMinijefe(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidad=2, vida=8)
#cada 3 oleadas hay que ponerlo