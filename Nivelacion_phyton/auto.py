from vehiculo2 import Vehiculo
from gps import GPS
from radio import Radio

class Auto(Vehiculo, GPS, Radio):

    def __init__(self, marca, modelo, ubicacion, emisora, velocidad):
        Vehiculo.__init__(self, marca, modelo)
        GPS.__init__(self, ubicacion)
        Radio.__init__(self, emisora)
        self._velocidad = velocidad

    def encender(self):
        return "El auto está encendido"

    def __str__(self):
        return f"{self.marca} {self.modelo} - Velocidad: {self._velocidad}"

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, valor):
        if valor >= 0:
            self._velocidad = valor
        else:
            print("Error: velocidad negativa")