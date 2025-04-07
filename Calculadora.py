def adicao (x, y):
    return x + y

def subtracao (x, y):
    return x - y

def multiplicacao (x, y):
    return x * y

def divisao (x, y):
    return x / y


print("Selecione a operação.")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:

    escolha = input("Escolha uma das opções(1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Coloque o primeiro número: "))
            num2 = float(input("Coloque o segundo número: "))
        except ValueError:
            print("Caractere inválido. Por favor coloque um número válido.")
            continue

        if escolha == '1':
            print(num1, "+", num2, "=", adicao(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicacao(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divisao(num1, num2))
        

        proximoCalc = input("Deseja fazer mais um cálculo? (S/N): ")
        if proximoCalc == "N":
          break
    else:
        print("Caractere inválido")
