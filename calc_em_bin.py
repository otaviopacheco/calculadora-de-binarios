verificador = True
expoenteDoValorUm = 0
conversor = 0
decimal = 0
decimalDois = 0 
vetorDeCalculos = []
expoenteDoValorUm = 0
expoenteDoValorDois = 0
operacoesValidas = [ "S","SOMA","SUB","SUBTRACAO","SUBTRAÇÃO","MULTIPLIÇÃO","M","MULTIPLICACAO","D","DIV","DIVISÃO"]
#  inicio do codigo 
while verificador:

    # Inserindo os valores
    valorUm = str(input("insira o primeiro valor: "))
    expoenteDoValorUm = len(valorUm) -1
    valorDois = str(input("insira o Segundo valor: "))
    expoenteDoValorDois = len(valorDois) -1
    # Bloco de verificação dos caracteres das strings
    # estava com problemas nesse bloco, mas ja foi resolvido
    for casaBinaria in valorUm:
            if casaBinaria != "1" and casaBinaria != "0"    :
                verificador = True
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

        operacao = str(input("Qual operação deseja fazer?:  \nS = Soma\nSub = Subtracao\nM = Multiplicacao\nDiv = Divisao\n")).upper()
        operacao = operacao.upper()
    
        if operacao == operacoesValidas[0] or operacao == operacoesValidas[1]:
            resultado = sum(vetorDeCalculos)
            print("o resultado é: {}".format(bin(resultado)[2::]))

        elif operacao == operacoesValidas[2] or operacao == operacoesValidas[3] or operacao == operacoesValidas[4]: 
            resultado = vetorDeCalculos[0] - vetorDeCalculos[1]
            print("o resultado é: {}".format(bin(resultado)[2::]))

        elif operacao == operacoesValidas[5] or operacao == operacoesValidas[6] or operacao == operacoesValidas[7]: 
            resultado = vetorDeCalculos[0] * vetorDeCalculos[1]
            print("o resultado é: {}".format(bin(resultado)[2::]))

        elif operacao == operacoesValidas[8] or operacao == operacoesValidas[9] or operacao == operacoesValidas[10]:
            if vetorDeCalculos[1] == 0 or vetorDeCalculos[1] == 0:
                print("Não é possivel dividir por zero.")
            else:
                resultado = int(vetorDeCalculos[0] / vetorDeCalculos[1])
                print("o resultado é: {}".format(bin(resultado)[2::]))
        else: 
        
                print("Operação invalida. Tente novamente.")
                
    # quando o usuario optar por finalizar as operações e o programa
        continuacao = str(input("Deseja escolher outra operação?  \nN = Não\nS = Sim\n: "))

        continuacao = continuacao.upper()

        if continuacao != "SIM" and continuacao != "S": 
            # Problema de continuidade resolvido
            # Finaliza o programa inteiro.
            finalizar = str(input("deseja finalizar?: "))
            finalizar = finalizar.upper()
            if finalizar == "S" or finalizar == "SIM" :
                break
            else:
                continue
            
        

# ficou muito grande, como eu pensei q ia ficar, tentei de toda forma reduzir a repetição de codigo mas n rolou 
# deu tanto problema q nem vale apena listar 
# se puderem revisar o codigo e tentar bugar p acharmos mais bugs vai ser otimo 
# nao consegui fazer o codigo se repetir se o usuario colocar q quer repetir e ja to pah das ideia 
