#for cont in range(3):
 # print("meow")
print("MEOW \n"*3, end="")




#miau varias vezes

def main():
  numero = valida_num()
  escreva_miau(numero)

def valida_num():
  while True :
    n = int(input())
    if (n>=0):
      return n
def escreva_miau(n):
  print("miau \n"*n)

main()