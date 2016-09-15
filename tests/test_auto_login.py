import pytest

import auto_login


def test_get_account_info(tmpdir):
    account_file = tmpdir.join('account.txt')
    account_file.write('myid,mypassword')
    account_file_path = str(account_file)

    assert auto_login.get_account_info(account_file_path) == ('myid', 'mypassword')


@pytest.mark.parametrize('account_id, account_password', [('wrong_id', 'wrong_password')])
def test_get_login_response(account_id, account_password):
    login_response = auto_login.get_login_response(account_id, account_password)

    assert login_response is not None
    assert login_response.status_code == 200
    assert auto_login.is_login_success(login_response) is False
