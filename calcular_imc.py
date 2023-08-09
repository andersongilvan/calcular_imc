# programa que calcula o IMC (ÍNDICE DE MASSA CORPÓREA) de uma pessoa #

# Solicita a entrada da altura e converte para um valor de ponto flutuante (float)
altura = float(input("Digite sua altutra: "))
# Solicita a entrada do peso e converte para um valor de ponto flutuante (float)
peso = float(input("digite o seu peso: "))
# Calcula o IMC dividindo o peso pelo quadrado da altura
imc = peso / (altura**2)


print("O seu IMC é de {:.2f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso!")

elif imc <= 25:
    print("Peso ideal!")

elif imc <= 30:
    print("Você está SOBREPESO!")

elif imc <= 40:
    print("OBESIDADE! CUIDE-SE!")

else:
    imc > 40
    print("PERIGO! OBESIDADE MÓRBIDA!")
