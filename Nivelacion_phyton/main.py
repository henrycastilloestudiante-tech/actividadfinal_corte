from auto import Auto

if __name__ == "__main__":

    auto1 = Auto("Toyota", "Corolla", "Riohacha", "La Mega", 60)
    auto2 = Auto("Mazda", "3", "Maicao", "RCN", 80)
    auto3 = Auto("Chevrolet", "Spark", "Valledupar", "Caracol", 50)

    print(auto1.encender())
    print(auto2.encender())
    print(auto3.encender())

    print(auto1)
    print(auto2)
    print(auto3)

    print(auto1.mostrar_ubicacion())
    print(auto1.reproducir())

    print("Velocidad:", auto1.velocidad)

    auto1.velocidad = 100
    print("Nueva velocidad:", auto1.velocidad)

    auto1.velocidad = -5