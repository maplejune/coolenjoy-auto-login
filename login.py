import requests, json
import os, logging, logging.handlers

LOG_FILE = os.path.join(os.path.dirname(__file__), 'LOGIN.log')
ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'PASSWORD.txt')

logger = logging.getLogger('COOLENJOY-LOGIN')
logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=10240, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

account = json.load(open(ACCOUNT_FILE))
form = {'s_url': '%2F', 'user_id': account['id'], 'password': account['password']}

response = requests.post('http://www.coolenjoy.net/bbs/login_check.php', data=form)

isLoginSuccess = response.text.find('http-equiv="refresh"') > -1

if isLoginSuccess:
    logger.debug('Login Success!')
else:
    logger.error('Something wrong :(', response.text)