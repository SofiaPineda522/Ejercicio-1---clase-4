class Moto:

    def __init__(self, id_propietario, cilindraje, placa, marca):
        self.id_propietario = id_propietario
        self.cilindraje = cilindraje
        self.placa = placa
        self.marca = marca

    def verificar_id(self):
        if self.id_propietario > 0:
            return "Ingreso exitoso."
        else:
            return "El ID debe ser mayor que 0."

    def verificar_cilindraje(self):
        if 125 < self.cilindraje < 200:
            return "La moto es de cilindraje medio."
        elif self.cilindraje <= 125:
            return "La moto es de bajo cilindraje."
        else:
            return "La moto es de alto cilindraje."

    def mostrar_info(self):
        return f"Marca: {self.marca} | Placa: {self.placa} | Cilindraje: {self.cilindraje}"

    def tipo_combustible(self):
        return "Moto de combustión"




class MotoElectrica(Moto):

    def __init__(self, id_propietario, cilindraje, placa, marca, autonomia):
        super().__init__(id_propietario, cilindraje, placa, marca)
        self.autonomia = autonomia

    def tipo_combustible(self):
        return "Moto eléctrica"

    def tipo_bateria(self):
        if self.autonomia > 100:
            return "Moto eléctrica de larga autonomía."
        else:
            return "Moto eléctrica de autonomía estándar."




def menu():
    while True:
        print("\n MENÚ PRINCIPAL")
        print("1. Registrar Moto")
        print("2. Registrar Moto Eléctrica")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_prop = int(input("Ingrese ID del propietario: "))
            cilindraje = int(input("Ingrese cilindraje: "))
            placa = input("Ingrese placa: ")
            marca = input("Ingrese marca: ")

            moto = Moto(id_prop, cilindraje, placa, marca)

            print("\n Información de la Moto")
            print(moto.verificar_id())
            print(moto.verificar_cilindraje())
            print(moto.mostrar_info())
            print(moto.tipo_combustible())

        elif opcion == "2":
            id_prop = int(input("Ingrese ID del propietario: "))
            cilindraje = int(input("Ingrese cilindraje (0 si es eléctrica ): "))
            placa = input("Ingrese placa: ")
            marca = input("Ingrese marca: ")
            autonomia = int(input("Ingrese autonomía en km: "))

            moto_elec = MotoElectrica(id_prop, cilindraje, placa, marca, autonomia)

            print("\n Información de la Moto Eléctrica")
            print(moto_elec.verificar_id())
            print(moto_elec.mostrar_info())
            print(moto_elec.tipo_combustible())
            print(moto_elec.tipo_bateria())

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


menu()