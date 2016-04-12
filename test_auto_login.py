# -*- coding: utf-8 -*-

from auto_login import *


def test_auto_login():
    assert is_login_success(get_login_response(*get_account_info())) is True
