from playwright.sync_api import Page


class TestLoginUI():
    def test_title(self,page: Page):
        assert page.title() == "OrangeHRM"
        
