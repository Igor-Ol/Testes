a = int(input("Digite o 1º Número: "))
b = int(input("Digite o 2º Número: "))
c = int(input("Digite o 3º Número: "))

if a >= b and a >=c:
    print("O Maior é",a, "a")
elif b >= a and b >= c:
    print("O Maior é",b, "b")

else: print("O Maior é",c, "c")