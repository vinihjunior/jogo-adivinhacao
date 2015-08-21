#!/usr/bin/env python
#
# Um simples jogo de adivinhação com dicas.
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

    lista_principal = []
    lista_animais = open("lista-animais.txt")
    lista = (lista_animais.read() )
    lista = lista.split()
    for line in lista:
        line = line.lower()
        lista_principal.append(line)
    lista_animais.close()
    end = len(lista_principal)
    secret = randint(0, end - 1)
    animal = (lista_principal[secret])
    comp = len(animal)
    print(animal)

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
