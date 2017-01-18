import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Inicio do programa')

def factorial(n):
    logging.debug('Inicio do fatorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i é ' + str(i) + ', total é ' + str(total))

    logging.debug('Fim do fatorial(%s%%)' % (n))
    return total


print(factorial(5))
logging.debug('Fim do Programa')