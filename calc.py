# Inicio do codigo: (autor: Otavio)
while True:
    Op =  str(input("deseja continuar?"))  
    if Op == "n":
        break

#Andrei 11/08/2024 5:50am :
try:
    valor=(int(input("Digite um numero: ")))
    if valor>=0:
        valorbin=bin(valor)  
        print("Seu valor escolhido:",valor,"é equivalente à",valorbin[2::],"em binário.")
    elif valor<0 or -0:
      print("Você Digitou um valor invalido, tenta novamente")    
except ValueError: 
    print("O 'Valor' inserido não é um valor válido. Tente novamente utilizando números.")

#até onde entendi basicamente é isso, se debuggar
#vai printar: Seu valor escolhido: 20 é equivalente à 10100 em binário. (usuario escolhe o valor, obvio)
# e caso o monstro insira uma letra inves de um numero vai printar: 
# Digite um numero: a
# O 'Valor' inserido não é um valor válido. Tente novamente utilizando numeros.   

#Andrei saindo, 06:41am.

