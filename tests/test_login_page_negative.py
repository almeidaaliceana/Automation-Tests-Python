import pytest
from Reports.page_object.login_page import LoginPage


class TestNegativeScenarios:
    @pytest.mark.login  # executa o teste
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrect", "Password123", "Your username is invalid!"),
                              ("student", "Password321", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error_message, "Error message is not expected"

