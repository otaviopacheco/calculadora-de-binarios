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
    flagDeEspaço = 0



    # Inserindo os valores
    valorUm = str(input("insira o primeiro valor"))
    expoenteDoValorUm = len(valorUm) -1
    valorDois = str(input("insira o Segundo valor"))
    expoenteDoValorDois = len(valorDois) -1
    # Bloco de verificação dos caracteres das strings



    for casaBinaria in valorUm:
        # a cada interação o verificador deve ser definido como false  
        if casaBinaria != "1" and casaBinaria != "0" and casaBinaria == " ":
            verificador = True
            print("O primeiro valor não é binario. Insira novamente")
            if casaBinaria == " ":
                flagDeEspaço += 1
                continue
    for casaBinariaDoSegundoValor in valorDois: 
        if casaBinariaDoSegundoValor != "1" and casaBinariaDoSegundoValor != "0" and casaBinariaDoSegundoValor != " ":
            verificador = True
            print("O segundo valor não é Binario. Insira os numeros novamente")
            if casaBinariaDoSegundoValor !=" ":
                flagDeEspaço += 1
                continue
        verificador = False
    if flagDeEspaço > 0:
        print("Os valores contém espaço em branco. Insira os numeros novamente sem espaço")
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
    operacao = str(input("Qual operação deseja fazer? \nS = Soma\nSub = Subtracao\nM = Multiplicacao\nDiv = Divisao\n")).upper()
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

# quando o usuario optar por finalizar as operações 
    continuacao = str(input("Deseja escolher outra operação? \nN = Não\nS = Sim"))

    continuacao = continuacao.upper()

    if continuacao == "NÃO" or continuacao == "N" or continuacao == "NAO": 

        print("Fim do programa")
        break