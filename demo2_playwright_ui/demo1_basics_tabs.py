from playwright.sync_api import sync_playwright

# p = sync_playwright().__enter__()
# try:
#     browser = p.chromium.launch(channel="chrome", headless=False)
# finally:
#     sync_playwright().__exit__()


with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False, args=["--disable-notifications"])
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.online.citibank.co.in/")

    page.locator("xpath=//button[@id='onetrust-accept-btn-handler']").click()
    page.locator("xpath=//div[text()='My Account']").hover()

    # expect new popup (page) and get it 
    with page.expect_popup() as new_page_info:
        page.locator("xpath=//div[text()='Banking with Citi']").click()
    new_page=new_page_info.value

    new_page.wait_for_load_state()

    new_page.locator("xpath=//input[@formcontrolname='username']").fill("admin")
    new_page.locator("xpath=//button[contains(text(),'Sign On')]").click()
    actual_error=new_page.locator("xpath=//span[contains(text(),'valid pass')]").inner_text()
    print(actual_error)

    