# python
from Estacionamento import Estacionamento

estacionamento = Estacionamento()
print('--------------------------------------------------')
print("Sistema de Estacionamento")
print('--------------------------------------------------')
print("Digite a opção desejada:")
print("1 - Adicionar carro")
print("2 - Remover carro")
print("3 - Listar carros")
print("4 - Encontrar carro")
print("5 - Sair")

while True:
    opcao = input("Opção: ")
    if opcao == '1':
        estacionamento.adicionar_carro()
    elif opcao == '2':
        estacionamento.remover_carro()
    elif opcao == '3':
        estacionamento.listar_carros()
    elif opcao == '4':
        estacionamento.encontrar_carro()
    elif opcao == '5':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")