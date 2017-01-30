# Um programa simples de cronometro

import time


# Exibe as instrucoes do programa
print('Pressione ENTER para iniciar. Após um tempo, pressione ENTER novamente para "marcar uma rodada" no cronometro. '
      'Aperte CTRL-C para sair.')


input()  # Tecle ENTER para iniciar
print('Iniciado')
startTime = time.time()  # obtem o horario de inicio da primeira rodada
lastTime = startTime
lapNum = 1

# Comeca a monitorar a duracao das rodadads.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Volta #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reinicia a ultima rodada
except KeyboardInterrupt:
    # Trata a excecao de CTRL-C para evitar que sua mensagem de erro seja exibida
    print('\nTerminado')
