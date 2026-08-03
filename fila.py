'''Neste módulo, você aprendeu sobre as três principais estruturas de dados da Ciência da Computação, as quais estão presentes nas mais diversas aplicações que utilizamos cotidianamente.

Aprender estruturas de dados é indispensável para qualquer estudante de Computação, pois elas fornecem os alicerces para a resolução eficiente de problemas no desenvolvimento de software. Dominar essas estruturas de dados é um dos requisitos para um bom programador se transformar em um ótimo programador.

Sua tarefa é criar um programa em Python que implemente uma Fila e suas principais operações.

Orientações para elaboração e entrega da atividade:

Crie um novo script em Python.
Implemente uma função enfileirar() para inserir elementos no final da fila.
Implemente uma função desenfileirar() para remover elementos no início da fila.
Implemente uma função consultar() para exibir o elemento do início da fila, sem removê-lo.
Implemente uma função contar() para exibir a quantidade de elementos na fila.
Crie uma fila na qual serão executadas as operações.
Elabore um menu de console que permita ao usuário o acesso a essas funções.
Envie o código Python (.py) desenvolvido por você pelo AVA.
Bons estudos!

Prof. Rafael Canteri.'''


# Inicialização da fila vazia
fila = []


def enfileirar(item):
    """Insere um elemento no final da fila."""
    fila.append(item)
    print(f"Elemento '{item}' adicionado ao final da fila.")


def desenfileirar():
    """Remove e retorna o elemento do início da fila."""
    if len(fila) == 0:
        print("A fila está vazia! Nenhum elemento para remover.")
    else:
        removido = fila.pop(0)
        print(f"Elemento '{removido}' removido do início da fila.")


def consultar():
    """Exibe o elemento do início da fila sem removê-lo."""
    if len(fila) == 0:
        print("A fila está vazia!")
    else:
        print(f"Elemento no início da fila: {fila[0]}")


def contar():
    """Exibe a quantidade total de elementos na fila."""
    print(f"Quantidade de elementos na fila: {len(fila)}")


def menu():
    """Exibe o menu de opções e gerencia a navegação do usuário."""
    while True:
        print("\n" + "=" * 30)
        print("      GERENCIADOR DE FILA")
        print("=" * 30)
        print("1. Enfileirar (Inserir)")
        print("2. Desenfileirar (Remover)")
        print("3. Consultar início")
        print("4. Contar elementos")
        print("5. Sair")
        print("=" * 30)

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            elemento = input("Digite o elemento a ser adicionado: ")
            enfileirar(elemento)
        elif opcao == "2":
            desenfileirar()
        elif opcao == "3":
            consultar()
        elif opcao == "4":
            contar()
        elif opcao == "5":
            print("Saindo do programa... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    menu()