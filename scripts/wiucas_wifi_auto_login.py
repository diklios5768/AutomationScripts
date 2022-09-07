# -*- encoding: utf-8 -*-
"""
@File Name      :   wiucas_wifi_auto_login.py
@Create Time    :   2022/9/7 17:57
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

import click
import requests

base_url = 'http://192.168.200.251:8008'
login_url = f'{base_url}/portal.cgi'
login_page_url = f'{base_url}/user_auth_verify.cgi'


@click.command()
@click.argument('username', type=str)
@click.argument('password', type=str)
def main(username, password):
    login_page = requests.post(login_page_url, data={
        'submit': 'submit'
    })
    code = login_page.json()['code']
    print(f'code:{code}')
    data = {
        'username': username,
        'password': password,
        'uplcyid': '1',
        'language': '0',
        'code': code,
        'submit': 'submit'
    }
    login = requests.post(login_url, data=data)
    login.encoding = 'utf-8'
    print(login.text)


if __name__ == '__main__':
    """
    usage: python wiucas_wifi_auto_login.py username password
    if have special character in password, use '' to wrap it
    """
    main()
