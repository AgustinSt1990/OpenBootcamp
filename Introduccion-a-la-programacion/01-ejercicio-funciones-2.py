class Coche:
    puertas = 0

    def agregar_puerta(self):
        self.puertas += 1


def main():
    c1 = Coche()
    c1.agregar_puerta()
    print(c1.puertas)


if __name__ == "__main__":
    main()
