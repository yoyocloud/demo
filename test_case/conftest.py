# coding=utf-8
import pytest
from common.do_request import HttpRequest
from common.do_logging import Logging
import hashlib
import json
import requests
from common.do_tools import post, Ukey


# @pytest.fixture(scope="class")
# def login():
#     hr = HttpRequest()
#     try:
#         login_res = hr.my_request("get", url=url, params=payload)
#         yield hr, login_res.cookies
#     except Exception as e:
#         Logging().error(e)
@pytest.fixture(scope="class")
def tal_login(phone):
    url = 'https://passport.100tal.com/v1/app/login/pwd'
    data = {
        "symbol": phone,
        "password": "a111111"
    }
    header = {
        "client-id": "132101",
        "device-id": "6A06BDF7845A772AD0DCF5089ED9A5FD",
        "package-name": "com.tongxue.tiku",
        "signature": "aW9zXzEuMDo4YWJkMzliM2ZkYWE5YzdmY2VhZmEwNTc1M2VkY2IwNGM4OTI1YjZj=",
        "timestamp": "1575700455347",
        "ver-num": "6.3.0|1.05.08",
        "skip-auth": "1"
    }
    response = post(url=url, data=data, headers=header)
    print(json.loads(response.content))
    res = json.loads(str(response.content, encoding="utf-8"))
    if res.get("errcode") == 0:
        tal_token = res.get('data').get('tal_token')
        tal_code = res.get('data').get('code')
        return tal_code, tal_token
    return None


@pytest.fixture(scope="class")
def app_login(tal_code, tal_token):
    url = 'https://kapi.txbapp.com/user/loginzt/codelogin'
    data = {"appchg": "AppStore", "apptype": "41", "appver": "6.3.0", "clientid": "132101",
            "code": "8fgqk6579hl0",
            "deviceid": "6FBBC896C96F0C4A6E5183796A28F68B",
            "sysdev": "iPhone 7",
            "sysver": "11.4",
            "uuid": "913103962861f66f2d2f18d53bf0f98b"}
    pass
    data["code"] = tal_code
    header = {"User-Agent": "Qingke AipBot/1.0 (Qingke-IOS/6.3.0; iOS/11.40; iPhone 7",
              "KY-UKEY": "ead20a903615c0d67dd2fdf219588071",
              "KY-SYSDEV": "iPhone 7",
              "KY-GRADE": "3",
              "Content-Length": "183",
              "KY-APPCHG": "tx_appstore",
              "KY-YEAR": "2017",
              "KY-UUID": "913103962861f66f2d2f18d53bf0f98b",
              "Connection": "keep-alive",
              "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9, en;q=0.8",
              "KY-PROID": "110000",
              "KY-SYSVER": "11.4",
              "Accept": "*/*",
              "Content-Type": "application/x-www-form-urlencoded",
              "KY-APPVER": "6.3.0",
              "Accept-Encoding": "br, gzip, deflate",
              "KY-APPVERS": "83",
              "Y-APPTYPE": "41"}
    uk = Ukey(data)
    header["KY-UKEY"] = uk
    header['KY-TAL-TOKEN'] = tal_token
    response = post(url=url, data=data, headers=header)
    print(response.status_code)
    res = json.loads(str(response.content, encoding="utf-8"))
    # return {"cookies*********": response.cookies}
    return response.cookies, header








