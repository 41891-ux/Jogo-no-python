import random
import time

def roleta():
    print("🎰 Bem-vindo ao Cassino da Roleta! 🎰")
    saldo = 100

    while True:
        print(f"\nSeu saldo atual é: R${saldo}")
        try:
            aposta = int(input("Quanto deseja apostar? R$ "))
            if aposta <= 0 or aposta > saldo:
                print("Aposta inválida.")
                continue
        except ValueError:
            print("Digite um valor numérico.")
            continue

        try:
            numero = int(input("Escolha um número entre 0 e 36: "))
            if numero < 0 or numero > 36:
                print("Número fora do intervalo.")
                continue
        except ValueError:
            print("Digite um número válido.")
            continue

        print("\nGirando a roleta...")
        time.sleep(2)
        resultado = random.randint(0, 36)
        print(f"A roleta parou no número: {resultado}")

        if numero == resultado:
            ganho = aposta * 35
            saldo += ganho
            print(f"🎉 Parabéns! Você ganhou R${ganho}!")
        else:
            saldo -= aposta
            print("💸 Que pena! Você perdeu a aposta.")

        if saldo <= 0:
            print("Você ficou sem saldo! Fim de jogo.")
            break

        continuar = input("Deseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print(f"Você saiu com R${saldo}. Obrigado por jogar!")
            break

roleta()

