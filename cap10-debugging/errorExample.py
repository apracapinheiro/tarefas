def spam():
    bacon()


def bacon():
    raise Exception('Esta é uma mensagem de erro.')

spam()