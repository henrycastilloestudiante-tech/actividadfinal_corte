class GPS:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion

    def mostrar_ubicacion(self):
        return f"Ubicación: {self.ubicacion}"


if __name__ == "__main__":
    g = GPS("Riohacha")
    print(g.mostrar_ubicacion())