import allure, pytest


class Test_001:
    #
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="测试步骤1")
    def test_01(self):
        print("----01----")
        allure.attach("标题", "内容")

        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤2")
    def test_02(self):
        print("----02----")

        assert True

    def test_add_png(self):
        with open("C:\\Users\\飞\\Desktop\\APP\\app_5.22\\scripts\\asd.png", "rb") as f:

            allure.attach("截图", f.read(), allure.attach_type.PNG)
