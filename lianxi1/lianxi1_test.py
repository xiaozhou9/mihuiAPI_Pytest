import requests
import pytest
from ddt import ddt, data


login_url ='http://test-www.mihuiai.com/r/user/login'
headers = {}


class Test_lianxi():

    def test_login01(self):
        payload = {"userName":"046","password":"123456", "autoLogin": "yes"}
        response = requests.post(login_url, json=payload)
        print(response.json())
        print(response.cookies)
        return response.cookies




if __name__ == '__main__':
    pytest.main()


