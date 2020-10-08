nome = input ('Nome do aluno:')
nota1 = int(input('Primeira nota: '))
nota2 = int (input('Segunda nota: '))
nota3 = int (input('Terceira nota: '))
nota4 = int (input('Quarta nota: '))

soma = nota1 + nota2 + nota3 + nota4 
media = soma /4

print('Media final do aluno: ',media)

if media >=6 :
    print ("O aluno",nome, " foi aprovado")
else:
    print ("O aluno",nome, "foi reprovado")
