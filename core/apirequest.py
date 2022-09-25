from email.mime import base
import requests
from enum import Enum

class ApiRequest():

    def __init__(self, user=None, prod=False) -> None:
        if prod:
            self.baseUrl = "https://reporting.rpdpymnt.com"
        else:
            self.baseUrl = "https://sandbox-reporting.rpdpymnt.com"

        if user:
            self.token = user['token']
        else:
            self.token = None

    def get(self, url, params):
        headers = {}
        if self.token:
            headers = {"Authorization": self.token}
        return requests.get(url="{}{}".format(self.baseUrl,url), params=params, headers=headers)

    def post(self, url, data):
        headers = {}
        if self.token:
            headers = {"Authorization": self.token}
        return requests.post(url="{}{}".format(self.baseUrl,url), data=data, headers=headers)

    