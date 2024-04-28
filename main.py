#mensagens

mensagem_inicial = """
##############################
        SEJA BEM VINDO

    Escolha uma operação:
        1 - Sacar
        2 - Depositar
        3 - Extrato
        4 - Sair
    
##############################
"""
mensagem_sucesso = "Operação realizada com sucesso!"

mensagem_fracasso = "Infelizmente você não é capaz de fazer essa operação!"

mensagem_inicio_extrato_saque = """
-------------------------------
            EXTRATO      
    Visualize suas operações
    de saque e depósito aqui

"""

mensagem_final_extrato_saque = """

-------------------------------
"""

print(mensagem_inicial)

# atribuições

saldo = 0

LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500

quantidade_saques = 0

lista_saques = []
lista_depositos = []

# programa

while True:

    operacao = int(input("O que deseja fazer?"))

    if operacao == 1:

        valor_saque = float(input("Quanto deseja sacar?"))

        if quantidade_saques == LIMITE_SAQUES or valor_saque > LIMITE_POR_SAQUE:
            print(f"{mensagem_fracasso}\nLimites atingidos!")
        elif valor_saque > saldo:
            print(f"{mensagem_fracasso}\nSaldo insuficiente.")
        else:
            saldo -= valor_saque

            quantidade_saques += 1

            lista_saques.append(valor_saque)

            print(mensagem_sucesso)

    if operacao == 2:

        valorDeposito = float(input("Quanto deseja depositar?"))

        saldo += valorDeposito

        lista_depositos.append(valorDeposito)

        print(mensagem_sucesso)

    if operacao == 3:

        print(mensagem_inicio_extrato_saque)

        if lista_saques:
            i = 1
            for saque in lista_saques:
                print(f"Saque n°{i}: {saque}")
                i += 1
        else:
            print("Não há operações de saque!")

        if lista_depositos:
            i = 1
            for deposito in lista_depositos:
                print(f"Depósito n°{i}: {deposito}")
                i += 1
        else:
            print("Não há operações de depósito!")

        print(f"\nSaldo: {saldo}")

        print(mensagem_final_extrato_saque)

    if operacao == 4:
        break