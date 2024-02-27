class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        numTV += 1

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        self._canal = canal

    def getCanal(self):
        return self._canal
    
    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, volumen):
        self._volumen = volumen

    def getVolumen(self):
        return self._volumen
    
    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control
    
    @classmethod
    def setNumTV(cls, numero):
        cls._numTV = numero

    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False