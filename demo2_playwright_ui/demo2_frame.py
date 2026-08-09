from playwright.sync_api import sync_playwright
import time
# p = sync_playwright().__enter__()
# try:
#     browser = p.chromium.launch(channel="chrome", headless=False)
# finally:
#     sync_playwright().__exit__()


with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False, args=["--disable-notifications"])
    context = browser.new_context(viewport={"width":1536,"height":816})
    page = context.new_page()

    page.goto("https://app.thetestingacademy.com/playwright/frames/")
    time.sleep(5)
    frame=page.frame_locator("xpath=//iframe[@name='vehicle-form']")

    frame.locator("css=input[name='vehicleName']").fill("hello")

    frame.locator("css=select[name='vehicleType']").select_option(label="SUV")

    frame.locator("css=[id='vehicle-submit']").click()

    time.sleep(5)
