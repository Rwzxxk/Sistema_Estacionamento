from Carro import Carro


class Estacionamento:
    def __init__(self):
        self.lista_carros = []

    def adicionar_carro(self):
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        cor = input("Digite a cor do carro: ")
        placa = input("Digite a placa do carro: ")


        novo_carro = Carro(marca, modelo, cor, placa)
        self.lista_carros.append(novo_carro)

        print("Carro adicionado com sucesso!")

    def remover_carro(self):
        placa = input("Digite a placa do carro a ser removido: ")

        for carro in self.lista_carros:
            if carro.placa == placa:
                self.lista_carros.remove(carro)
                print("Carro removido com sucesso!")
                return

        print("Carro não encontrado.")

    def listar_carros(self):
        if not self.lista_carros:
            print("Nenhum carro estacionado.")
            return

        for carro in self.lista_carros:
            print(
                f"Marca: {carro.marca}, "
                f"Modelo: {carro.modelo}, "
                f"Cor: {carro.cor}, "
                f"Placa: {carro.placa}"
            )

    def encontrar_carro(self):
        placa = input("Digite a placa do carro a ser encontrado: ")

        for carro in self.lista_carros:
            if carro.placa == placa:
                print(
                    f"Marca: {carro.marca}, "
                    f"Modelo: {carro.modelo}, "
                    f"Cor: {carro.cor}, "
                    f"Placa: {carro.placa}"
                )
                return

        print("Carro não encontrado.")
