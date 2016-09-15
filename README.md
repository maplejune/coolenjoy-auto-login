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

cron 또는 AWS 람다를 이용하여 auto_login.py이 주기적으로 실행되도록 설정해둡니다.

이제 매일 로그인 포인트가 획득 되는 것을 확인할 수 있습니다!


