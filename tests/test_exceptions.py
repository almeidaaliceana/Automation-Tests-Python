import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium.webdriver.support.wait import WebDriverWait

from Reports.page_object.exceptions_page import ExceptionsPage


class TestException:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 input should be displayed but is not"

    @pytest.mark.exceptions
    def test_element_no_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page.add_second_food("Hamburguer")
        assert exceptions_page.get_confirmation_message() == "Row 2 was saved", "Row 2 input should be displayed, but is not"

    @pytest.mark.exceptions

    def test_invalid_element_estate_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.modify_row_1_input("Hamburguer")
        assert exceptions_page.get_confirmation_message() == "Row 1 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.are_instructions_displayed(), "Instruction text element should be not displayed"

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 input should be displayed but is not"
