# c:\>mapit 870 Valencia St, San Francisco, CA 94110

# Inicia um mapa no navegador usando um endereco da linha de comando ou do clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # obtem o endereco da linha de comando
    address = ' '.join(sys.argv[1:])
else:
    # obtem o endereco a partir do clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)