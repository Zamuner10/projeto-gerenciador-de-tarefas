
import os

def limpa_tela():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\n" * 50)

listas_tarefas = []

def main():
    menu()

def menu():
    limpa_tela()
    while True:
        print(f"{'=' * 35 } ")
        print("\nBem-vindo ao gerênciador de Tarefas\n")
        print(f"{'=' * 35 } ")
        print(f"{' ' * 10 }MENU")
        print(f"{'=' * 35 } ")
        print(f"{' ' * 5 }A - Adicionar tarefas")
        print(f"{' ' * 5 }R - Remover tarefas")
        print(f"{' ' * 5 }M - Mostrar tarefas")
        print(f"{' ' * 5 }S - Sair")
        print(f"{'=' * 35 } ")
        opc = input("Opção: ").strip().lower()
        
        if opc =='s':
            print("Saindo...")
            break
        elif opc == 'a':
            AdicionarTarefa()
        elif opc == 'r':
            ApagarTarefas()
        elif opc == 'm':
            MostrarTarefas()
        else:
            print("Valor invalido !")

def AdicionarTarefa():
    limpa_tela()

    print("\nDigite a quantidade de tarefas a ser adicionada")
    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Digite apenas números inteiros!")
        input("\nPressione Enter para voltar ao menu...")
        return  # volta ao menu    for i in range(quantidade):
    
    for i in range(quantidade):
        tarefa = input(f"Tarefa {i+1}: ").strip().capitalize()
        listas_tarefas.append(tarefa)

    print(f"\n{quantidade} tarefa(s) adicionada(s) com sucesso!")
    input("\nPressione Enter para voltar ao menu...")
    
        

def MostrarTarefas():
    limpa_tela()
    print("\nTarefas a se fazerem durante o dia: ")

    if not listas_tarefas:
        print("Nenhuma tarefa cadastrada")
    else:
        for tarefa in listas_tarefas:
            print("-", tarefa)
    input("\nPressione Enter para voltar ao menu...")

def ApagarTarefas():
    limpa_tela()
    if not listas_tarefas:
        print("Nenhuma tarefa para apagar !")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    print ("\nLista de Tarefas que podem ser apagada: ")
    for i, tarefa in enumerate(listas_tarefas, 1):
        print(f"{i} - {tarefa}")

    item = input("\nDigite o nome exato da tarefa a se apagar: ").strip().capitalize()

    if item in listas_tarefas:
        listas_tarefas.remove(item)
        print("Tarefa Apagada com sucesso !")
    else:
        print("Não existe está tarefa, tente denovo !")

    input("\nPressione Enter para voltar ao menu...")
main()
