class Documento:
    nombre = ''
    tamano = 0
    codificacion = ''
    def __init__(self, nombre, tamano, codificacion):
        self.nombre = nombre
        self.tamano = tamano
        self.codificacion = codificacion