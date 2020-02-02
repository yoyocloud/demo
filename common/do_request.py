# coding=utf-8
import requests


class HttpRequest:

    @staticmethod
    def my_request(method, url, params=None, cookies=None):
        if method.lower() == "post":
            result = requests.post(url=url, data=params, cookies=cookies)
        elif method.lower() == "get":
            result = requests.get(url=url, params=params, cookies=cookies)
        return result


if __name__ == '__main__':
    pass




