#6
salbase = float(input("Digite o salário base: "))
gratif = float(input("Digite a gratificação: "))


salbruto = salbase + gratif


if salbruto < 1000:
    
    ir = salbruto * (15 / 100)
else:
    
    ir = salbruto * (20 / 100)


salliq = salbruto - ir


print("-" * 30)
print(f"Salário Bruto: R$ {salbruto:.2f}")
print(f"Imposto (IR): R$ {ir:.2f}")
print(f"Salário Líquido: R$ {salliq:.2f}")
