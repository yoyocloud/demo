# coding=utf-8
import pytest
from test_data import gain_userinfo
from common.do_logging import Logging
import random
from common.do_request import HttpRequest


@pytest.mark.demo
class TestLogin:

    res = None

    @pytest.mark.parametrize("data", gain_userinfo.user_info_list)
    def test_user_info(self, app_login, data):
        global res
        try:
            cookies = app_login[1]
            obj = app_login[0]
            # url = data["url"]
            # params = data["payload"]
            print(cookies)
            print(obj)
            # res = obj.my_request("get", url, params, cookies)
            # # print(res.json())
            # return res
        except Exception as e:
            Logging().error(e)
        try:
            assert res.json().get("res").get("uid") is not None
        except Exception as e:
            Logging().error(e)

    # @pytest.mark.parametrize("data", gain_userinfo.edit_grade)
    # def test_edit_grade(self, login, data):
    #     cookies = login[1]
    #     obj = login[0]
    #     url = data["url"]
    #     # print(res)
    #     now_grade = res.json()["res"]["grade"]
    #     print(now_grade)
    #     while True:
    #         random_grade = random.randint(1, 6)
    #         if now_grade == random_grade:
    #             random.randint(1, 6)
    #         else:
    #             break
    #     print(url)
    #     print(cookies)
    #     print(obj)
    #     edit_grade_res = obj.my_request("get", url, cookies)
    #     print(edit_grade_res.json())








