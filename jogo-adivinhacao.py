#!/usr/bin/env python
#
# Um simples jogo de adinhação com dicas.
#
# Vinicius Júnior
# @VinihJunior
# vinicius.dphelippe@gmail.com


from random import randint

while True:
    print("************************************************")
    print("*                                              *")
    print("*        Adivinhe qual é o ANIMAL \o/          *")
    print("*                                              *")
    print("************************************************")
    print("\nDescubra qual é o animal: ")
    lista = []                                # cria uma lista dos nomes da "lista-animais.txt" atribuidos em "line"
    lista_animais = open("lista-animais.txt") # abre o arquivo .txt
    for line in lista_animais:                # */
        line = line.lower()                   # deixa todas as letras minúsculas
        lista.append(line)                    # agrega todos os nomes da "lista_animais" em "line" /*
        end = len(lista)                      # conta a quantidade de nomes da "lista" e atribui a variável "end"
    lista_animais.close()                     # fecha o arquivo .txt
    secret = randint(0, end - 1)              # faz o sorteio de um número de 0 á o valor atribuído em "end"
    animal = (lista[secret])                  # sorteia o nome do animal da lista
    comp = len(animal)
    print("\n* Que tem", (comp - 1), "letras \n",
          "\n* E começa com a letra", animal[0], "\n")
    resp = input("\n* Digite sua resposta: ")
    if resp == animal:                        # compara a resposta com o nome sorteado.
        print("\nVocê ACERTOU!! \o/ é", animal, "\n")
        voltar = input("Deseja jogar novamente? (y/n): ")
        if voltar not in ("y" or "Y"):
            break
    else:
        print("\nVocê errou :(\n")
        voltar = input("Deseja jogar novamente? (y/n): ")
        if voltar not in ("y" or "Y"):
            break
