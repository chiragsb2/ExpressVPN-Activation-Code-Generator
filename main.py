import requests
import time
import random, string
from discord import Webhook, RequestsWebhookAdapter
import colorama
from colorama import Fore, Back, Style
import os
colorama.init()
# Copyright (c) 2022 fluro#0009 fluorescentxx@protonmail.com
# Using this tool I am not responsible for any damages or bans

                  
print(Fore.CYAN + """

 ______                           __      _______  _   _ 
 |  ____|                          \ \    / /  __ \| \ | |
 | |__  __  ___ __  _ __ ___  ___ __\ \  / /| |__) |  \| |
 |  __| \ \/ / '_ \| '__/ _ \/ __/ __\ \/ / |  ___/| . ` |
 | |____ >  <| |_) | | |  __/\__ \__ \\  /  | |    | |\  |
 |______/_/\_\ .__/|_|  \___||___/___/ \/   |_|    |_| \_|
             | |                                          
             |_|                                    """ + Fore.RESET)

link = input("Webhook link :")
amount = int(input("How many activation codes to generate :"))
for i in range(amount):
    time.sleep(0.3)
    code = "EA" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EB" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EC" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "ED" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EE" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EF" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EG" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EH" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EI" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EJ" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EK" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EL" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EM" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EN" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EO" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EP" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EQ" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "ER" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "ES" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "ET" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EU" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EV" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EW" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EX" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EY" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    code = "EZ" + "".join(random.choices(string.ascii_letters + string.digits, k=20))
    print("[GENERATED] " + code)
    webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
    webhook.send(code)
