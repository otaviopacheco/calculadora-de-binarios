# receber um número binario
binario=input('Escreva um número binário: ')
# identificar um número não binário
while True:
    for numero in binario:
        if numero !='1' and numero !='0' and numero !=' ':
            print('Erro. O número inserido não é binário.')
            binario=input('Escreva um número binário: ')
            verificador='não'
        else:
            verificador='sim'  
    if verificador == 'sim':
        break

#função para tirar espaços em branco
for numero in binario:
    if numero == ' ':
        print('Erro. Tente novamente sem o espaço.')
        binario=input('Escreva o número: ')
# contar o numero de caracteres para ter o expoente
expoente=len(binario) - 1
decimal=0
#usar o for para percorrer cada string do numero binario
for numero in binario:
    #passar o numero para int para fazer a conta
    binarioParaDecimal=int(numero)*(2**expoente)
    #diminuir o expoente a medida que vai passando pelos numeros
    expoente -=1
    #somar os resultados das expoenciações e multiplicações
    decimal=decimal+binarioParaDecimal
print(decimal)


# teste 1:erro. Esta dando o dobro do valor. Motivo: o expoente estava começando com 1 a mais.
# teste 2:problema resolvido. Foi adicionado -1 ao expoente inicial. 
# teste 3, com espaço:erro. Motivo: O espaço é invalido para conta, então o código não roda.
# teste 4: tentativa de usar a função .strip(), não deu certo.
# teste 5: problrma resolvido. Foi criado um novo for para identificar o espaço e pedir para o usuario digitar o número novamente sem ele.


# teste 6, adicionado o verificador de binário:erro. Os números binários estavam entrando no if. Motivo: operadores errados. 
# teste 7: 
