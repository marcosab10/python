# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

todo = []
todo_removed = []

def desfazer(todo, todo_removed):
    if not todo:
        print('Nenhuma tarefa para desfazer')
        return
    item = todo.pop()
    todo_removed.append(item)

def adiciona_tarefa(todo, item):
    if not item.strip():
        print('Você não adicionou uma tarefa.')
        return
    todo.append(item)

def refazer(todo, todo_removed):
    if not todo_removed:
        print('Nenhuma tarefa para refazer')
        return
    item = todo_removed.pop()
    todo.append(item)


def imprimir(todo):
    print()
    print('TAREFAS:')
    print(*todo, sep="\n")
    print()

while True:
    print('Comandos: listar, desfazer, refazer, sair')
    acao = input('Digite uma tarefa ou comando: ')

    if acao == 'listar':
        imprimir(todo)
    elif acao == 'desfazer':
        desfazer(todo, todo_removed)
        imprimir(todo)
    elif acao == 'refazer':
        refazer(todo, todo_removed)
        imprimir(todo)
    elif acao == 'clear':
        os.system('cls')
    elif acao == 'sair':
        break
    else:
        adiciona_tarefa(todo, acao)
        imprimir(todo)




