# coding=utf-8
import os
import re

import requests


def get_account_info(file_path):
    account_file = open(file_path, 'r')
    account_id, account_password = account_file.read().split(',', 2)
    account_file.close()

    return account_id, account_password


def get_login_response(account_id, account_password):
    form_data = {'url': 'http%3A%2F%2Fwww.coolenjoy.kr', 'mb_id': account_id, 'mb_password': account_password}
    login_response = requests.post('http://www.coolenjoy.kr/login_check', allow_redirects=False, data=form_data)

    if login_response.cookies.get('PHPSESSID'):
        cookies = dict(PHPSESSID=login_response.cookies.get('PHPSESSID'))

        return requests.get('http://www.coolenjoy.kr', cookies=cookies)
    else:
        return login_response


def is_login_success(login_response):
    if re.search(u'총점:(\d+)', login_response.text):
        return True
    else:
        return False


def lambda_handler(event, context):
    account_path = os.path.join(os.path.dirname(__file__), 'account.txt')
    response = get_login_response(*get_account_info(account_path))

    if is_login_success(response):
        current_point = re.search(u'총점:(\d+),', response.text).group(1)

        print u'Current point : ' + current_point
        return current_point
    else:
        raise Exception(response.text)
