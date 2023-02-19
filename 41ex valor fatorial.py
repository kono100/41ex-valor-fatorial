

# 41. Faça um programa que leia um número inteiro, calcule o fatorial dele. Por exemplo 5! = 5*4*3*2*1=120



def main():
    n = int(input("Digite um valor: "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    print()
    print("O valor %d! é =" %n,fat)
    print()
    
main()