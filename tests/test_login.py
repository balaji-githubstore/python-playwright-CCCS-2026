from playwright.sync_api import Page,expect
from assertpy import assert_that
import pytest
from utilities.data_source import DataSource

class TestLoginUI():
    def test_invalid_login(self, page: Page):
        page.locator("xpath=//input[@name='username']").fill("Admin")
        page.locator("xpath=//input[@name='password']").fill("admin12345")
        page.locator("xpath=//button[normalize-space()='Login']").click()
        actual_error = page.locator(
            "xpath=//p[contains(normalize-space(),'Invalid')]").inner_text()
        assert_that(actual_error).is_equal_to("Invalid credentials")

    @pytest.mark.parametrize("username,password,expected_error", [
        ["john", "john123", "Invalid credentials"],
        ["peter", "peter123", "Invalid credentials"]
    ])
    def test_invalid_login(self, page: Page, username, password, expected_error):
        page.locator("xpath=//input[@name='username']").fill(username)
        page.locator("xpath=//input[@name='password']").fill(password)
        page.locator("xpath=//button[normalize-space()='Login']").click()
        actual_error = page.locator(
            "xpath=//p[contains(normalize-space(),'Invalid')]").inner_text()
        assert_that(actual_error).is_equal_to(expected_error)

    @pytest.mark.parametrize("username,password,expected_error", DataSource.data_invalid_login_csv)
    def test_invalid_login_csv(self, page: Page, username, password, expected_error):
        page.locator("xpath=//input[@name='username']").fill(username)
        page.locator("xpath=//input[@name='password']").fill(password)
        page.locator("xpath=//button[normalize-space()='Login']").click()
        actual_error = page.locator(
            "xpath=//p[contains(normalize-space(),'Invalid')]").inner_text()
        assert_that(actual_error).is_equal_to(expected_error)
        expect(page.locator("xpath=//p[contains(normalize-space(),'Invalid')]")).to_have_text(expected_error)
