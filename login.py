# -*- coding:UTF-8 -*-

import requests, json
import re, os, logging, logging.handlers

LOG_FILE = os.path.join(os.path.dirname(__file__), 'LOGIN.log')
ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'PASSWORD.txt')

logger = logging.getLogger('COOLENJOY-LOGIN')
logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=10240, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

account = json.load(open(ACCOUNT_FILE))
form = {'s_url': '%2Fmobile_web.html', 'user_id': account['id'], 'password': account['password']}

response = requests.post('http://www.coolenjoy.net/bbs/login_check.php', data=form)

sessionKey = response.cookies['PHPSESSID']
cookies = dict(PHPSESSID=sessionKey)

response = requests.get('http://www.coolenjoy.net/mobile_web.html', cookies=cookies)
result = re.search(u'(\d+) 점수', response.text)

if result:
    point = result.groups()[0]
    
    logger.debug('Login success! : ' + point)
else:
    logger.error(response.text)
