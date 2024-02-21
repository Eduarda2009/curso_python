# programa para calcular IMC
# desenvolvimento por eduarda

print("***************************")
print("  CONSUMO DE COMBUSTIVEL   ")
print("***************************")
print()

# criação das variaveis

modelo_carro = ""
autonomia_carro = 0
distância = 0
combustível = 0.0
combustível_utilizado = 0.0
total = 0.0

# entrada dos dados
modelo_carro = input("Modelo do carro? ")
autonomia_carro = int (input("Autonomia do carro? "))
distância = int(input("Distância da viagem? "))
combustível = float (input("Preço do combustível"))

# processar os valores para obter o IMB

combustível_utilizado = distância / autonomia_carro
total = combustível_utilizado * combustível

# saída do processamento
print()
print("*******************************")
print("           RESULTADO           ")
print("*******************************")
print()
print("Modelo do veículo: " + modelo_carro)
print("autonomia do veículo: " + str(autonomia_carro))
print("distância percorrida: " + str(distância))
print("valor do combustível: " + str(combustível))
print()
print("*******************************")
print("quantidade de combustível utilizado: " + str(combustível_utilizado)+"l")
print("total gasto com a viagem: R$" + str(total))
print("-------------------------------")



      
      
