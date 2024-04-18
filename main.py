import os
try:
    import Aminofix
except ImportError:
    os.system("pip uninstall Aminofix")
    os.system("pip install tqdm")
try:
    import BotAmino
except ImportError:
    os.system("pip uninstall BotAmino")
    os.system("pip install https://github.com/ThePhoenix78/BotAmino/archive/master.zip")
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
try:
    import colored
except ImportError:
    os.system("pip install colored")
try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import pystyle
except ImportError:
    os.system("pip install pystyle")
    
import marshal
with open('blog.py', 'rb') as file:
    codigo_ofuscado = file.read()

codigo_compilado = marshal.loads(codigo_ofuscado)
exec(codigo_compilado)
