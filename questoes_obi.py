#questões_obi

# Questão var obi 2023. nivel 1
x = int(input())
y = int(input())

if (x > 8) or (x < -8):
  print("N")

elif (y > 8) or (y < 0):
  print("N")

else:
  print("S")


#questão pandemia obi 2023. nivel junior

N = int(input())
R = int(input())
P = int(input())
i = 0
d = 0

while (i < P):
  i = i + N*R
  d = d+1
print(d)



#exercicio
#######################
# Leitura dos dados
N = int(input())  # infectados no dia 0
R = int(input())  # fator reprodutivo
P = int(input())  # número alvo de pessoas infectadas

# Inicialização
total_infectados = N
novos_infectados = N
dias = 0

# Simulação dia a dia
while total_infectados < P:
    dias += 1
    novos_infectados = novos_infectados * R
    total_infectados += novos_infectados

# Resultado
print(dias)
