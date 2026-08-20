from playwright.sync_api import Page, expect


class TestLoginUI():
    def test_title(self, page: Page):
        assert page.title() == "OrangeHRM"
        expect(page).to_have_title('OrangeHRM123')

    def test_login_header(self, page: Page):
        expect(page.locator(
            "xpath=//h5[normalize-space()='Login']")).to_be_visible()
