setup.py
#!/bin/env python3
# code by : Dagi Tech

"""
you can re run setup.py
if you have added some wrong value
"""
import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
        os.system('clear')
        print(f"""
        {re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
        {re}╚═╗{cy}├┤  │ │ │├─┘
        {re}╚═╝{cy}└─┘ ┴ └─┘┴

                   Version : 1.01
        {re}Subscribe Dagi Tech on Youtube
        {cy}www.youtube.com/c/Dagitech
        """)
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] enter api ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] enter hash ID : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] enter phone number : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] setup complete !")
print(gr+"[+] now you can run any tool !")
print(gr+"[+] make sure to read docs 4 installation & api >
print(gr+"[+] https://github.com/termuxprofessor/TeleGram->