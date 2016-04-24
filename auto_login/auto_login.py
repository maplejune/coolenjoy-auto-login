# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import requests

import notifier


def get_account_info(file_path='../account.txt'):
    account_file = open(file_path, 'r')
    account_id, account_password = account_file.read().split(',', 2)
    account_file.close()

    return account_id, account_password


def get_login_response(account_id, account_password):
    form_data = {'s_url': '%2Fmobile_web.html', 'user_id': account_id, 'password': account_password}
    login_response = requests.post('http://www.coolenjoy.net/bbs/login_check.php', data=form_data)

    if login_response.cookies:
        cookies = dict(PHPSESSID=login_response.cookies['PHPSESSID'])

        return requests.get('http://www.coolenjoy.net/mobile_web.html', cookies=cookies)
    else:
        return login_response


def is_login_success(login_response):
    if re.search(u'(\d+) 점수', login_response.text):
        return True
    else:
        return False


if __name__ == '__main__':
    response = get_login_response(*get_account_info())

    if is_login_success(response):
        notifier.send_message(u'쿨엔조이 로그인 성공 : ' + re.search(u'(\d+) 점수', response.text).group(1) + u'포인트')
    else:
        notifier.send_message(response.text)
