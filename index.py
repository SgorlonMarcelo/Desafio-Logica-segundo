vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))
saldo = vitorias-derrotas

def rank(saldo):
    if saldo <= 10:
        nivel = "Ferro"
        return nivel
    elif saldo <= 20:
        nivel = "Bronze"
        return nivel
    elif saldo <= 50:
        nivel = "Prata"
        return nivel
    elif saldo <= 80:
        nivel = "Ouro"
        return nivel
    elif saldo <= 90:
        nivel = "Diamante"
        return nivel
    elif saldo <=100:
        nivel = "Lendário"
        return nivel
    else:
        nivel = "Imortal"
        return nivel
nivel = rank(vitorias-derrotas)

print("O Herói tem o saldo de ",saldo, "vitórias e está no nivel ", nivel)
