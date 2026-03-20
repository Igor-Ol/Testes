#5
h = float(input("Digite sua altura: "))

while True:
    sexo = input("Digite seu gênero (M ou F): ").lower().strip()

    if sexo == "m":
        peso_ideal = (72.7 * h) - 58
        break 
    elif sexo == "f":
        peso_ideal = (62.1 * h) - 44.7
        break 
    else:
        print("Sexo inválido! Tente novamente.") 

print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
