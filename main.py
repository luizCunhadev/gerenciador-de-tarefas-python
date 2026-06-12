def adicionar_tarefa(tarefas, nome):
    """
    Adiciona uma nova tarefa à lista de tarefas pendentes.
    :param tarefas: lista de tarefas
    :param nome: nome da tarefa
    :return: lista atualizada
    """
    tarefas.append({"tarefa": nome, "status": "pendente"})
    print("Tarefa adicionada com sucesso!")
    return tarefas


def listar_tarefas(tarefas):
    """
    Lista todas as tarefas cadastradas.
    :param tarefas: lista de tarefas
    """
    if not tarefas:
        print("Nenhuma tarefa pendente.")
    else:
        for i, tarefa in enumerate(tarefas):
            print(f"{i} - {tarefa['tarefa']} (status: {tarefa['status']})")


def concluir_tarefa(tarefas, indice):
    """
    Marca uma tarefa como concluída.
    :param tarefas: lista de tarefas
    :param indice: índice da tarefa
    :return: lista atualizada
    """
    if 0 <= indice < len(tarefas):
        tarefas[indice]["status"] = "concluída"
        print("Tarefa marcada como concluída com sucesso!")
    else:
        print("Tarefa não encontrada.")
    return tarefas


def remover_tarefa(tarefas, indice):
    """
    Remove uma tarefa da lista.
    :param tarefas: lista de tarefas
    :param indice: índice da tarefa
    :return: lista atualizada
    """
    if 0 <= indice < len(tarefas):
        removida = tarefas.pop(indice)
        print(f"Tarefa '{removida['tarefa']}' removida!")
    else:
        print("Índice inválido.")
    return tarefas


def menu():
    """
    Menu principal do sistema de tarefas.
    """
    tarefas_pendentes = []

    while True:
        print("\nMenu de tarefas")
        print("1 - Adicionar Tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar como concluída")
        print("4 - Remover tarefa")
        print("5 - Sair")

        escolher = input("Escolha uma das opções acima: ")

        if escolher == '1':
            tarefa = input("Adicione um nome para sua tarefa: ")
            tarefas_pendentes = adicionar_tarefa(tarefas_pendentes, tarefa)

        elif escolher == '2':
            listar_tarefas(tarefas_pendentes)

        elif escolher == '3':
            indice = int(input("Escolha o número da tarefa concluída: "))
            tarefas_pendentes = concluir_tarefa(tarefas_pendentes, indice)

        elif escolher == '4':
            indice = int(input("Escolha o número da tarefa a ser removida: "))
            tarefas_pendentes = remover_tarefa(tarefas_pendentes, indice)

        elif escolher == '5':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, tente novamente.")


# Executa o menu
menu()
