coolenjoy-auto-login
=========================

[![Build Status](https://travis-ci.org/maplejune/coolenjoy-auto-login.svg?branch=master)](https://travis-ci.org/maplejune/coolenjoy-auto-login)
[![Coverage Status](https://coveralls.io/repos/github/maplejune/coolenjoy-auto-login/badge.svg?branch=master)](https://coveralls.io/github/maplejune/coolenjoy-auto-login?branch=master)

쿨엔조이 (http://coolenjoy.net) 로그인 포인트 획득 자동화

## 사용법
auto_login/account.txt 파일을 생성합니다.

    쿨엔조이ID,쿨엔조이PASSWORD

auto_login/telegram.txt 파일을 생성합니다.

    텔레그램_bot_token,텔레그램_chat_id

crontab 설정을 하루 주기로 설정해둡니다.

    0 0 * * * python ~/coolenjoy-auto-login/auto_login/auto_login.py

이제 매일 로그인 포인트가 획득 되는 것을 확인할 수 있습니다!


