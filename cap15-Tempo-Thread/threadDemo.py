import threading
import time

print('Inicio do programa')


def takeANap():
    time.sleep(5)
    print('Acordando!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('Fim do programa')