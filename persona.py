class Persona:
    def __init__(self, _nombre, _edad, _altura, _sexo):
        self._nombre = _nombre
        self._edad = _edad
        self._altura = _altura
        self._sexo = _sexo

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getAltura(self):
        return self._altura

    def getSexo(self):
        return self._sexo

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setAltura(self, altura):
        self._altura = altura

    def setSexo(self, sexo):
        self._sexo = sexo