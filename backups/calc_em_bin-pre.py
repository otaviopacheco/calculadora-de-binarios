# variaveis utilizadas para controle e verificação
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
    valorUm = str(input("insira o primeiro valor: "))
    expoenteDoValorUm = len(valorUm) -1
    valorDois = str(input("insira o Segundo valor: "))
    expoenteDoValorDois = len(valorDois) -1
    # Bloco de verificação dos caracteres das strings

    for casaBinaria in valorUm:
    
        if casaBinaria != "1" and casaBinaria != "0"    :
            verificador = True
            # valorUm = input("O primeiro valor não é binario. Insira novamente")
            print("O primeiro valor não é binario. Insira novamente")
            break

    for casaBinariaDoSegundoValor in valorDois: 
        if casaBinariaDoSegundoValor != "1" and casaBinariaDoSegundoValor != "0":
            verificador = True
            # valorDois=input("O segundo valor não é Binario. Insira os numeros novamente")
            print("O segundo valor não é Binario. Insira os numeros novamente")
            break
        verificador = False
    if verificador == False:
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

    if operacao == "S" or "SOMA":
        resultado = sum(vetorDeCalculos)
        print("o resultado é: {}".format(bin(resultado)))

    elif operacao == "SUB" or "SUBTRACAO" or operacao == "SUBTRAÇÃO":
        resultado = vetorDeCalculos[0] - vetorDeCalculos[1]
        print("o resultado é: {}".format(bin(resultado)))

    elif operacao ==  "MULTIPLIÇÃO" or "M" or "MULTIPLICACAO": 
        resultado = vetorDeCalculos[0] * vetorDeCalculos[1]
        print("o resultado é: {}".format(bin(resultado)))

    elif operacao ==  "D" or "DIVISAO" or "DIV" or operacao == "DIVISÃO": 
        resultado = vetorDeCalculos[0] / vetorDeCalculos[1]
        print("o resultado é: {}".format(bin(resultado)))
    else:
        operacao=input("opcao invalida insira novamente: ")
# quando o usuario optar por finalizar as operações e o programa
    continuacao = str(input("Deseja escolher outra operação?:  \nN = Não\nS = Sim"))

    continuacao = continuacao.upper()

    if continuacao == "NÃO" or continuacao == "N" or continuacao == "NAO": 

        print("Fim do programa")
        break
    elif continuacao == "SIM" or continuacao == "S": 

        continue       
    else:
        continuacao = input("opcao invalida insira novamente: ")

#faz o def na mâo pai
#
    
# ficou muito grande, como eu pensei q ia ficar, tentei de toda forma reduzir a repetição de codigo mas n rolou 
# deu tanto problema q nem vale apena listar 
# se puderem revisar o codigo e tentar bugar p acharmos mais bugs vai ser otimo 
# nao consegui fazer o codigo se repetir se o usuario colocar q quer repetir e ja to pah das ideia 