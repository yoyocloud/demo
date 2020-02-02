# coding = utf-8
# time:2020/2/1
# author:xiaohei
# ----*----*----*----*----*
import hashlib
import requests


def md5(content):
    m = hashlib.md5()
    m.update(content.encode("utf-8"))
    return m.hexdigest()


def Ukey(params, key_uuid='913103962861f66f2d2f18d53bf0f98b',
         app_sign_key='txbsghbcddfywxlbwn007'):
    try:
        # 将参数值提取出来生成一个字符串
        params_list = []
        # 将list中的int转化为str
        str_params_list = map(lambda x: str(x), params.values())
        for i in str_params_list:
            params_list.append(i)
        req_params = ",".join(params_list)

        # 将拼接的字符串进行md5加密
        value = key_uuid + md5(req_params) + app_sign_key
        result = md5(value)
        return result
    except Exception as e:
        print(e)
        return 'Ukey生成失败'


request_session = requests.session()


def post(url, data, headers):
    return request_session.request(method="post", url=url, data=data, headers=headers)
