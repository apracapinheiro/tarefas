import random
guess = ''


def palpite(guess):
    if guess == 'cara':
        return 1
    elif guess == 'coroa':
        return 0

while guess not in ('cara', 'coroa'):
    print('Advinhe o lancamento da moeda! Entre com cara ou coroa')
    guess = input()




lancamento = random.randint(0, 1) # 0 é coroa e 1 é cara

if lancamento == palpite(guess):
    print("Voce acertou!!")
else:
    print("Tente novamente!")
    guess = input()

    if lancamento == palpite(guess):
        print("Voce acertou!")
    else:
        print("Voce errou novamente!")