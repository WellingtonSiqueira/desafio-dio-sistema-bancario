# Import de bibliotecas que serão utilizadas
import datetime

# Menu de opções do sistema
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

# Inicialização de variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


# Central de controle do Sistema
while True:
    opcao = input(menu)

    # Opção de depósito
    if opcao == '1':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Falha! O valor informado é inválido.")

    # Opção de saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        agora = datetime.datetime.now()
        dia_da_semana = agora.weekday()
        hora_atual = agora.hour

        # Reduz o limite em 50% se for final de semana ou após as 20 horas
        if dia_da_semana in [5, 6] or hora_atual >= 20:
            limite *= 0.5  

        # Verificações de saque
        if valor > saldo:
            print("Saldo Insuficiente.")
        elif valor > limite:
            print("Falha! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Falha! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Falha! O valor informado é inválido.")

        # Reseta o limite para o valor original após operação
        limite = 500  

    # Opção de extrato
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Opção de sair
    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")