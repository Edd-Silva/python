#Este programa diz bem vindo e pergunta seu nome.

print ('Bem vindo!')
print ('Qual o seu nome?') #pergunta o nome
meuNome = input()
print ('É bom conhecer você,\n' + meuNome)#Concatena a string com a variavel meuNome
print ('O comprimento do seu nome é:')
print (len(meuNome))
print ('Qual a sua idade?')#pergunta sua idade
minhaIdade = input()
print ('Você terá, ' + str(int(minhaIdade) + 1) + ' em um ano.')