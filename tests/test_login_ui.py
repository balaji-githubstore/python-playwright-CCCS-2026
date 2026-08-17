from playwright.sync_api import Page,expect


class TestLoginUI():
    def test_title(self,page: Page):
        assert page.title() == "OrangeHRM"
        expect(page).to_have_title('OrangeHRM')
        
