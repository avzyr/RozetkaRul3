#!/usr/bin/env python3

import json
import broadlink
import time
import os

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
        state: object = device.get_energy()
        print(f'{ipadr} sei chas imeet {state} sily. A vot porog ustanovlen na {pwrlim} sily')
        if state <= pwrlim:
            device.set_power(False)
            time.sleep(30)
            device.set_power(True)
            print(f'{ipadr} porog{pwrlim},a sei chas{state}. Perezagruzka svetit')
    except Exception:
        print(f'Ne konnekt k {ipadr}')

for roz in txtsett['rozetki']:
    checkrozetkastate(roz['ipadr'], roz['pwrlmt'])
