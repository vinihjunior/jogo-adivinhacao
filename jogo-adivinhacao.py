from random import randint

while True:
    print("************************************************")
    print("*                                              *")
    print("*          Adivinhe qual é o ANIMAL            *")
    print("*                                              *")
    print("************************************************")
    print("\nDescubra qual é o animal: ")
    lista = []
    lista_animais = open("lista-animais.txt")
    for line in lista_animais:
        line = line.lower()
        lista.append(line)
        end = len(lista)
    lista_animais.close()
    secret = randint(0, end - 1)
    animal = (lista[secret])
    comp = len(animal)
    print(animal)
    print("\n* Que tem", (comp - 1), "letras \n",
          "\n* E começa com a letra", animal[0], "\n")
    resp = input("\n* Digite sua resposta: ")
    print(resp)
    if resp == animal:
        print("\nVocê ACERTOU!! \o/ é", animal, "\n")
        voltar = input("Deseja jogar novamente? (y/n): ")
        if voltar not in ("y" or "Y"):
            break
    else:
        print("\nVocê errou :(\n")
        voltar = input("Deseja jogar novamente? (y/n): ")
        if voltar not in ("y" or "Y"):
            break
