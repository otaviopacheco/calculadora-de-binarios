verificador = True
expoenteDoValorUm = 0
conversor = 0
decimal = 0
decimalDois = 0 
vetorDeCalculos = []
expoenteDoValorUm = 0
expoenteDoValorDois = 0
#  inicio do codigo 
while verificador:

    # Inserindo os valores
    valorUm = str(input("insira o primeiro valor"))
    expoenteDoValorUm = len(valorUm) -1
    valorDois = str(input("insira o Segundo valor"))
    expoenteDoValorDois = len(valorDois) -1
    # Bloco de verificação dos caracteres das strings
    # estava com problemas nesse bloco, mas ja foi resolvido
    for casaBinaria in valorUm:
            if casaBinaria != "1" and casaBinaria != "0"    :
                verificador = True
                # valorUm = input("O primeiro valor não é binario. Insira novamente")
                print("O primeiro valor não é binario. Inicie o programa novamente.")
                break
            else :
                verificador = False
    for casaBinariaDoSegundoValor in valorDois: 
        if casaBinariaDoSegundoValor != "1" and casaBinariaDoSegundoValor != "0":
            verificador = True
            print("O segundo valor não é Binario. Inicie o programa novamente.")
            break
    if verificador == True:
        break

# bloco para converter os numeros  
    for numero in valorUm: 
        conversor = (int(numero) * (2**expoenteDoValorUm))
        expoenteDoValorUm -= 1
        decimal = decimal + conversor
    vetorDeCalculos.append(decimal)

    for numero in valorDois:  
        conversor = (int(numero) * (2**expoenteDoValorDois))
        expoenteDoValorDois -= 1
        decimalDois = decimalDois + conversor
    vetorDeCalculos.append(decimalDois)

    # Bloco para a seleção das operações
    while True:

        operacao = str(input("Qual operação deseja fazer? \nS = Soma\nSub = Subtracao\nM = Multiplicacao\nDiv = Divisao\n")).upper()
        operacao = operacao.upper()

        if operacao == "S" or operacao == "SOMA":
            resultado = sum(vetorDeCalculos)
            print("o resultado é: {}".format(bin(resultado)))

        elif operacao == "SUB" or operacao == "SUBTRACAO" or operacao == "SUBTRAÇÃO":
            resultado = vetorDeCalculos[0] - vetorDeCalculos[1]
            print("o resultado é: {}".format(bin(resultado)))

        elif operacao ==  "MULTIPLIÇÃO" or  operacao == "M" or "MULTIPLICACAO": 
            resultado = vetorDeCalculos[0] * vetorDeCalculos[1]
            print("o resultado é: {}".format(bin(resultado)))

        elif operacao ==  "D" or operacao == "DIVISAO" or "DIV" or operacao == "DIVISÃO": 
            resultado = vetorDeCalculos[0] / vetorDeCalculos[1]
            print("o resultado é: {}".format(bin(resultado)))
        else: 
            while operacao == operacao:
                print("Operação invalida. Tente novamente")
    # quando o usuario optar por finalizar as operações e o programa
        continuacao = str(input("Deseja escolher outra operação? \nN = Não\nS = Sim"))

        continuacao = continuacao.upper()

        if continuacao != "SIM" or continuacao == "S": 
            break
    # Problema de continuidade resolvido
    # Finaliza o programa inteiro.
    finalizar = str(input("deseja finalizar?"))
    finalizar = finalizar.upper()
    if finalizar != "NAO" or finalizar != "NãO" or finalizar != "N" :
        verificador = False
    else:
        continue
    if verificador == False:
        break

# ficou muito grande, como eu pensei q ia ficar, tentei de toda forma reduzir a repetição de codigo mas n rolou 
# deu tanto problema q nem vale apena listar 
# se puderem revisar o codigo e tentar bugar p acharmos mais bugs vai ser otimo 
# nao consegui fazer o codigo se repetir se o usuario colocar q quer repetir e ja to pah das ideia 
