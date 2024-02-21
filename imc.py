# programa para calcuclar IMC
# desenvolvimento por eduarda

print("***********************************")
print("*       CALCULADORA DE IMC        *")
print("***********************************")
print()


# CRIAÇÃO DAS VARIAVEIS

nome = ""
peso = 0
altura = 0.0
imc = 0.0

# ENTRADA DOS DADOS
nome = input("digite o seu nome: ")
peso = int (input("digite o seu peso: "))
altura = float (input("digite a sua altura: "))

# PROCESSAR OS VALORES PARA OBTER O IMC
imc = peso / altura ** 2

# SAÍDA DO PROCESSAMENTO
print()
print("*********************************")
print("*            RESULTADO           ")
print("*********************************")
print("*                               *")
print("NOME: " + nome)
print("PESO: " + str(peso) + "kg")
print("ALTURA: " + str(altura) + "m")
print("IMC: " + str(imc))

print (imc)















