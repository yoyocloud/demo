# coding = utf-8
# time:2020/2/1
# author:xiaohei
# ----*----*----*----*----*
import pytest

@pytest.mark.demo
class TestLogin:

    res = None

    # @pytest.mark.parametrize("data", gain_userinfo.user_info_list)
    # def test_user_info(self, app_login, data):
    #     global res
    #     try:
    #         cookies = app_login[1]
    #         obj = app_login[0]