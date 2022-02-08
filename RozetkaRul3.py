#!/usr/bin/env python3

import json
import socket
import broadlink
import time
import os
from netifaces import interfaces, ifaddresses, AF_INET
from broadlink import Device

p2fws = os.path.dirname(os.path.abspath(__file__))+'/settings.json'
with open(p2fws, 'r') as f:
    txtsett = json.load(f)
    f.close()

broadlink.setup(txtsett['wifi_name'], txtsett['wifi_pass'], 3)

def checkrozetkastate(ipadr, pwrlim):
    try:
        device: Device = broadlink.hello(ipadr)
        device.auth()
        pwrstate = device.check_power()
        if not pwrstate:
            device.set_power(True)
            print(f'{ipadr} была выключена. Включаем.')
        else:
            state: object = device.get_energy()
            print(f'{ipadr} на сей час мощность составляет {state} Ватт. А вот порог установлен на {pwrlim} Ватт')
            if state <= pwrlim:
                device.set_power(False)
                time.sleep(30)
                device.set_power(True)
                print(f'{ipadr} порог{pwrlim},а сей час{state}. Перезагрузка светит')
    except Exception:
        print(f'Не получилось соединиться с {ipadr}')

for roz in txtsett['rozetki']:
    checkrozetkastate(roz['ipadr'], roz['pwrlmt'])
