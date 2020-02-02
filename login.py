# coding=utf-8
import requests


def login_tv():
    url = "http://btvapi.yitongxuexi.com/sys/test/login"
    payload = {
        "KY_UUID": "08b7617199eba54642ada74d786102cf",
        "phone": 18310160699
    }
    sign_in = requests.get(url, params=payload)
    # print(Sign_in.json())
    return sign_in


# 获取用户信息
def gain_user_info(cookies):
    url = "http://btvapi.yitongxuexi.com/sys/user/info"
    payload = {
            "KY_UUID": "08b7617199eba54642ada74d786102cf",
    }
    user_info = requests.get(url, params=payload, cookies=cookies)
    return user_info




if __name__ == '__main__':
    res = login_tv()
    # res1 = gain_user_info(res_cookies)
    print(res.json())
    print(res.cookies)