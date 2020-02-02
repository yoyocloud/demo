# coding = utf-8
# time:2020/1/31
# author:xiaohei
# ----*----*----*----*----*
import hashlib
import json
import requests
import urllib3


# 看代码应该是先集团登录 获取tal_code 和tal_token 然后再app  code登录
class Login:
    request_session = requests.session()
    urllib3.disable_warnings()

    # MD5加密
    def md5(self, content):
        m = hashlib.md5()
        m.update(content.encode("utf-8"))
        return m.hexdigest()

    # 生成UKey
    def Ukey(self, params, key_uuid='937d587092f17ed1f86a5aefd279ac14', app_sign_key='txbsghbcddfywxlbwn007'):
        try:
            # 将参数值提取出来生成一个字符串
            params_list = []
            # 将list中的int转化为str
            str_params_list = map(lambda x: str(x), params.values())
            for i in str_params_list:
                params_list.append(i)
            req_params = ",".join(params_list)

            # 将拼接的字符串进行md5加密
            value = key_uuid + self.md5(req_params) + app_sign_key
            result = self.md5(value)
            return result
        except Exception as e:
            print(e)
            return 'Ukey生成失败'

    def post(self, url, data, headers):
        return self.request_session.request(method="post", verify=False, url=url, data=data, headers=headers)

    def tal_login(self, phone):
        url = 'https://passport.100tal.com/v1/app/login/pwd'
        data = {
            "symbol": phone,
            "password": "a111111"
        }
        # header = self.tool.yamlRead('headers.yaml', 'tal')
        header = {
            "client-id": "132101",
            "device-id": "6A06BDF7845A772AD0DCF5089ED9A5FD",
            "package-name": "com.tongxue.tiku",
            "signature": "aW9zXzEuMDo4YWJkMzliM2ZkYWE5YzdmY2VhZmEwNTc1M2VkY2IwNGM4OTI1YjZj=",
            "timestamp": "1575700455347",
            "ver-num": "6.3.0|1.05.08",
            "skip-auth": "1"
        }
        response = self.post(url=url, data=data, headers=header)
        # print(json.loads(response.content))
        res = json.loads(str(response.content, encoding="utf-8"))
        if res.get("errcode") == 0:
            tal_token = res.get('data').get('tal_token')
            tal_code = res.get('data').get('code')
            return tal_code, tal_token
        return None

    def app_login(self, tal_code, tal_token):
        url = 'https://kapi.txbapp.com/user/loginzt/codelogin'
        data = {"appchg": "AppStore",
                "apptype": "41",
                "appver": "6.3.0",
                "clientid": "132101",
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
                  # "Connection": "close",
                  "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9, en;q=0.8",
                  "KY-PROID": "110000",
                  "KY-SYSVER": "11.4",
                  "Accept": "*/*",
                  "Content-Type": "application/x-www-form-urlencoded",
                  "KY-APPVER": "6.3.0",
                  "Accept-Encoding": "br, gzip, deflate",
                  "KY-APPVERS": "83",
                  "KY-APPTYPE": "41"
                  # "KY-SERIAL": "A1000A0A013352",
                  # "KY-ROMVER": "BOS01A000235"
                  }
        uk = self.Ukey(data)
        header["KY-UKEY"] = uk
        header['KY-TAL-TOKEN'] = tal_token
        response = self.post(url=url, data=data, headers=header)
        # print(response.status_code)
        # res = json.loads(str(response.content, encoding="utf-8"))
        # return {"cookies*********": json.loads(response.content)}
        # headers["KY-SERIAL"] = "A1000A0A013352"
        # headers["KY-ROMVER"] = "BOS01A000235"
        # headers["checkCookie"] = "false"
        # headers["KY-APPCHG"] = "BoxTV"
        # headers["KY-SYSVER"] = "7.1.2"
        return response.cookies, header


if __name__ == '__main__':
    request_session = requests.session()
    res = Login().tal_login(16200000001)
    print("tal_code", res[0])
    print("tal_token", res[1])
    response = Login().app_login(res[0], res[1])
    print("response:", response)
    cookies = response[0]
    headers = response[1]
    headers["KY-SERIAL"] = "A1000A0A013352"
    headers["KY-ROMVER"] = "BOS01A000235"
    headers["checkCookie"] = "false"
    headers["KY-APPCHG"] = "BoxTV"
    headers["KY-SYSVER"] = "7.1.2"

    print("cookies---", cookies)
    print("headers---", headers)
    url = "https://tvapi.yitongxuexi.com/sys/user/info"
    # url = "https://kapi.txbapp.com/live/info/livestart"
    # params= {"_t":"1580648338", "packid": "63"}
    result = requests.get(url=url, cookies=cookies, headers=headers)
    print("请求返回的结果", json.loads(result.content))

