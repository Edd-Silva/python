#Este programa diz bem vindo e pergunta seu nome.
#Este programa é baseado no livro "Atomatize tarefas macantes com python"

print ('Bem vindo!')
print ('Qual o seu nome?') #pergunta o nome
meuNome = input()
print ('É bom conhecer você,\n' + meuNome)#Concatena a string com a variavel meuNome
print ('O comprimento do seu nome é:')
print (len(meuNome))# A função "len", conta a quantidade de caracteres existente no nome fornecido.
print ('Qual a sua idade?')#pergunta sua idade
minhaIdade = input()
print ('Você terá, ' + str(int(minhaIdade) + 1) + ' em um ano.')
