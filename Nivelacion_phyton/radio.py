class Radio:
    def __init__(self, emisora):
        self.emisora = emisora

    def reproducir(self):
        return f"Emisora: {self.emisora}"


if __name__ == "__main__":
    r = Radio("La Mega")
    print(r.reproducir())