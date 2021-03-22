import requests

class HttpRequests(object):

    def __init__(self, url):
        self.url = url
        self.rep = requests.Session()
        self.headers = {}
    def get(self, uri='', params='', data='', json='', headers=None, cookies=None):
        url = self.url + uri
        response = requests.get(url, params=params, data=data, json=json, headers=headers, cookies=cookies)
        return response

    def post(self, uri='', params='', data='', json='', headers=None, cookies=None):
        url = self.url + uri
        response = requests.post(url, params=params, data=data, json=json, headers=headers, cookies=cookies)
        return response

    def put(self, uri='', params='', data='', json='', headers=None, cookied=None):
        url = self.url + uri
        response = requests.put(url, params=params, data=data, json=json, headres=headers, cookied=cookied)
        return response

    def delete(self, uri='', params='', data='', json='',headers=None, cookies=None):
        url = self.url + uri
        response = requests.delete(url, params=params, data=data, json=json, headers=headers, cookies=cookies)
