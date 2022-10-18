from deportista import Deportista


class Futbolista(Deportista):
    _listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setGolesMarcados(self, nuevo):
        self._golesMarcados = nuevo

    def setTarjetasRojas(self, nuevo):
        self._tarjetasRojas = nuevo

    def setPiernaHabil(self, nuevo):
        self._piernaHabil = nuevo

    def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(
            self.getNombre(), self.getDeporte(), str(self.getEdad()), str(self.getAñosPracticando()))

    @classmethod
    def getListaFutbolistas(cls):
        cls._listaFutbolistas

    @classmethod
    def setListaFutbolistas(cls, nuevo):
        cls._listaFutbolistas = nuevo