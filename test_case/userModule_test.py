import pytest
import requests
from mihuiapi_test_project.common import httpRequest
from mihuiapi_test_project.common.read_excel import *

url = 'http://test-p.mihuiai.com'
login_uri = '/r/mihui/user/login'
register_url = '/r/mihui/user/directRegister'


class TestLoginPage():
    @pytest.mark
    @pytest.mark.parametrize('number, username, password, msg_assert, suatus_assert, tips_msg', read_login_data())
    def test_login(self, number, username, password, msg_assert, suatus_assert, tips_msg):
        payload = {"userName": username, "password": password}
        response = requests.post(url + login_uri, json=payload)
        if number == 1:
            assert response.json().get('message') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 2:
            assert response.json().get('message') == msg_assert, tips_msg
        elif number == 3:
            assert response.json().get('message') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 4:
            assert response.json().get('message') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 5:
            assert response.json().get('message') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg

    @pytest.mark.parametrize('number, phone, password, repassword, verifyCode, msg_assert, suatus_assert, tips_msg',
                             read_register_data())
    def test_register(self, number, phone, password, repassword, verifyCode, msg_assert, suatus_assert, tips_msg):
        payload = {"phone": phone, "verifyCode": verifyCode, "password": password, "rePassword": repassword}
        response = requests.post(url + register_url, json=payload)
        if number == 1 :
            assert response.json().get('message') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 2:
            assert response.json().get('success') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 3:
            assert response.json().get('message') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 4:
            assert response.json().get('success') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 5:
            assert response.json().get('message') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 6:
            assert response.json().get('message') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 7:
            assert response.json().get('success') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 8:
            assert response.json().get('message') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg
        elif number == 9:
            assert response.json().get('success') == msg_assert, tips_msg
            assert response.status_code == suatus_assert, tips_msg


if __name__ == '__main__':
    pytest.main()
