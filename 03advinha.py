from random import randint #Biblioteca random, buscar um aleatorio inteiro

print('######### Iniciando o jogo! ###########')

random = randint(0, 100)
chute = 0 
chances = 10

# < Menor
# > Maior
# == Igual (comparação)
# != Diferente (comparação)
# >= Maior ou igual 
# <= Menor ou igual

while chute != random :
    chute = input('Chute um número entre 0 e 100: ')
    if chute.isnumeric() : #Evitar que o usuário digite algo diferente de um número
        chute = int(chute)
        chances = chances - 1
        if chute == random :
            print('')
            print('Parabéns, você venceu! O numero era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break
        else :
            print('')
            if chute > random :
                print('Você errou! Dica: É um número menor.')
            else :
                print('Você errou! Dica: É um número maior.')
            print('VocÊ possui ainda {} chances'.format(chances))
            print('')
        if chances == 0 :
            print('')
            print('Suas chances acabaram, você perdeu! O número era: {}'.format(random))
            print('')
            break

print('######### Fim de jogo! ###########')
    
            