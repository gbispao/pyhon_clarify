```python
from random import randint
import time

print('######### Iniciando o jogo! ###########')

numero_secreto = randint(0, 100)
chute = 0
chances = 10

# Inicia o cronômetro
inicio = time.time()

while chute != numero_secreto:
    chute = input('Chute um número entre 0 e 100: ')

    if chute.isnumeric():  # Evita que o usuário digite algo diferente de um número
        chute = int(chute)
        chances -= 1

        if chute == numero_secreto:
            # Finaliza o cronômetro
            fim = time.time()
            tempo_total = fim - inicio

            print('')
            print(
                'Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(
                    numero_secreto, chances
                )
            )
            print('Tempo de jogo: {:.2f} segundos'.format(tempo_total))
            print('')
            break

        else:
            print('')

            if chute > numero_secreto:
                print('Você errou! Dica: É um número menor.')
            else:
                print('Você errou! Dica: É um número maior.')

            print('Você possui ainda {} chances'.format(chances))
            print('')

        if chances == 0:
            # Finaliza o cronômetro
            fim = time.time()
            tempo_total = fim - inicio

            print('')
            print(
                'Suas chances acabaram, você perdeu! O número era: {}'.format(
                    numero_secreto
                )
            )
            print('Tempo de jogo: {:.2f} segundos'.format(tempo_total))
            print('')
            break

    else:
        print('')
        print('Digite apenas números!')
        print('')

print('######### Fim de jogo! ###########')
```

    
            
