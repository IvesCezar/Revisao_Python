#Cadastro de nomes 1

# nomes = []
while True:
    n1 = input("Digite o Primeiro nome: ")
    n2 = input("Digite o Segundo nome: ")
    n3 = input("Digite o Terceiro nome:")
    n4 = input("Digite o Quarto nome: ")
    n5 = input("Digite o Quinto nome: ")
    nomes.append(n1)
    nomes.append(n2)
    nomes.append(n3)
    nomes.append(n4)
    nomes.append(n5)
    print(nomes)
    break
print("Lista concluida")

#Removendo elementos 2
nomes=["maçã", "banana", "Uva", "Laranja"]
nomes.remove("Uva")
nomes.append("Morango")
print(nomes)


#Soma dos Números 3
numeros = []
while True:
    n1 = int(input("Digite o Primeiro número: "))
    n2 = int(input("Digite o Segundo número: "))
    n3 = int(input("Digite o Terceiro número: "))
    n4 = int(input("Digite o Quarto número: "))
    n5 = int(input("Digite o Quinto número: "))
    numeros.append(n1)
    numeros.append(n2)
    numeros.append(n3)
    numeros.append(n4)
    numeros.append(n5)
    print(f"A soma dos números é: {n1 + n2 + n3 + n4 + n5}")
    break

#Numeros pares 4
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(f"Números pares: {pares}")


#Verificação de aluno aprovado 5
lista_notas = []
while True:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    lista_notas.append(nota1)
    lista_notas.append(nota2)
    lista_notas.append(nota3)
    lista_notas.append(nota4)
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print(f"Aluno aprovado com média {media:.2f}")
    else:
        print(f"Aluno reprovado com média {media:.2f}")
    break

#Pesquisa em lista 6
nomes = ["joão", "maria", "ives", "mariana", "gabriel"]
pesquisa = input("Digite o seu nome")
if pesquisa in nomes:
    print("Aluno encontrado")
else:    print("Aluno não encontrado")


#Contagem de elementos 7
lista = [1, 5, 7, 9, 12, 30, 50, 70]
print(f"A quantidade total de elementos é: {len(lista)}")
print(f"O maior número da lista é: {max(lista)}")
print(f"O menor número da lista é: {min(lista)}")


#Sistema simples de tarefas 8
tarefas = []
for i in range(3):
    tarefa = input(f"Digite a {i + 1}ª tarefa: ")
    tarefas.append(tarefa)
print("\nLista de tarefas:")
for i, tarefa in enumerate(tarefas, start=1):
    print(f"{i}. {tarefa}")
remover = input("\nDigite o nome da tarefa que deseja remover: ")
if remover in tarefas:
    tarefas.remove(remover)
    print("Tarefa removida com sucesso!")
else:
    print("Tarefa não encontrada.")
print("\nLista atualizada:")
for i, tarefa in enumerate(tarefas, start=1):
    print(f"{i}. {tarefa}")
