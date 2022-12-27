salario = int(input())
reajuste = 0
if salario <= 600:
    reajuste = 0.17
elif salario <= 900:
    reajuste = 0.13
elif salario <= 1500:
    reajuste = 0.12
elif salario <= 2000:
    reajuste = 0.10
else:
    reajuste = 0.05
       
novo_salario= (salario *reajuste) + salario 
print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {salario * reajuste:.2f}\nEm percentual: {reajuste * 100:.0f} %") 