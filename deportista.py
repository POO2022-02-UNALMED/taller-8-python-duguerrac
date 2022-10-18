from persona import Persona


class Deportista(Persona):

    def __init__(self, nombre, edad, altura, sexo, deporte, añosPracticando):
        super().__init__(nombre, edad, altura, sexo)
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setDeporte(self, deporte):
        self._deporte = deporte

    def serAñosPracticando(self, años):
        self._añosPracticando = años