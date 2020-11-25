class FlorLinda_Valdivia:
    def __init__(self, ):
pass

class PlantaDeProduccion(FlorLinda_Valdivia):
pass

class Bodega(PlantaDeProduccion):
pass

class Flores:
    def __init__(self, especie_flor, tamano_flor):
        self.especie_flor = especie_flor
        self.tamano_flor = tamano_flor
pass

class Ramo(Flores):
    def __init__(self, nombre_ramo, tamano_ramo, diseno_ramo):
        self.nombre_ramo = nombre_ramo
        self.tamano_ramo = tamano_ramo
        self.diseno_ramo = diseno_ramo
pass


#Especificaciones de formato entrada/salida


