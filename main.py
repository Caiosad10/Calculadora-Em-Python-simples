def calculadora(num1, num2):
  operacao = input('Qual operação voce gostaria de fazer (+; -; *; /)? ')
  if operacao == '+':
    return f'O resultado da soma é {num1 + num2}'
  elif operacao == '-':
    return f'O resultado da subtração é {num1 - num2}'
  elif operacao == '*':
    return f'O resultado da multiplicação é {num1 * num2}'
  elif operacao == '/':
    return f'O resultado da divisão é {num1 / num2}'

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

print(calculadora(num1, num2))