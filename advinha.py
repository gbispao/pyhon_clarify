from random import randint

print("######### JOGO DE ADIVINHAÇÃO #########")
print("1 - Modo Hardcore")
print("2 - Modo Invertido")

modo = input("Escolha um modo: ")

# ==========================
# MODO HARDCORE
# ==========================
if modo == "1":

    print("\n===== MODO HARDCORE =====")

    numero_secreto = randint(0, 100)
    chances = 10

    while chances > 0:

        chute = input("Digite um número entre 0 e 100: ")

        if not chute.isnumeric():
            print("Digite apenas números!")
            continue

        chute = int(chute)
        chances -= 1

        if chute == numero_secreto:
            print(f"\n🏆 Você venceu!")
            print(f"O número era {numero_secreto}.")
            print(f"Restavam {chances} chances.")
            break

        print(f"❌ Errou! Chances restantes: {chances}")

    else:
        print(f"\n💀 Você perdeu!")
        print(f"O número era {numero_secreto}.")

# ==========================
# MODO INVERTIDO
# ==========================
elif modo == "2":

    print("\n===== MODO INVERTIDO =====")
    print("Pense em um número entre 0 e 100.")

    input("Pressione ENTER quando estiver pronto...")

    menor = 0
    maior = 100
    tentativas = 0

    while True:

        chute = (menor + maior) // 2
        tentativas += 1

        print(f"\nTentativa {tentativas}")
        print(f"Meu palpite é: {chute}")

        resposta = input(
            "(m) Seu número é maior\n"
            "(n) Seu número é menor\n"
            "(a) Acertei\n"
            "Resposta: "
        ).lower()

        if resposta == "a":
            print(
                f"\n🤖 Acertei o número {chute} "
                f"em {tentativas} tentativas!"
            )
            break

        elif resposta == "m":
            menor = chute + 1

        elif resposta == "n":
            maior = chute - 1

        else:
            print("Resposta inválida!")

        if menor > maior:
            print("\n⚠️ As informações ficaram inconsistentes.")
            print("Verifique se respondeu corretamente.")
            break

else:
    print("Modo inválido!")

print("\n######### FIM DE JOGO #########")
