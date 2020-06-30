# isso é uma calculadora
def soma (a, b):
  x = a + b
  return x 

def subtração (a, b):
  x = a - b
  return x

a = int(input("Digite o numero: "))
b = int(input("Digite outro numero: "))
op = int(input("1 soma | 2 subtração: "))

if (op == 1):
  soma(a, b)

if (op == 2):
  subtração(a, b)
