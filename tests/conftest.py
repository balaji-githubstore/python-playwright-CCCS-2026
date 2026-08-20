import pytest
from playwright.sync_api import sync_playwright
import logging
from datetime import datetime
import os
import allure

def setup_logging():
    """
    Configure logging for test execution
    """
    # Create logs directory
    logs_dir = "logs1"
    os.makedirs(logs_dir, exist_ok=True)

    # Create log file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(logs_dir, f"test_execution_{timestamp}.log")

    # Root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove handlers if behave already set them
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("=" * 80)
    logger.info("Test Execution Started")
    logger.info("=" * 80)
    return logger


@pytest.fixture(scope="session")
def logger():
    return setup_logging()


@pytest.fixture(scope="session")
def browser(logger):
    logger.info("Launching Chrome browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        yield browser
        logger.info("Closing Chrome browser")
        browser.close()


@pytest.fixture(scope="function")
def page(browser, logger):
    logger.info("Opening OrangeHRM application")
    context = browser.new_context()

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/")
    yield page
    
    context.tracing.stop(
        path="traces/test_trace.zip"
    )

    logger.info("Closing page")
    page.close()

# ---------- Screenshot on Failure ----------


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            page.screenshot(
                path=f"screenshots/{item.name}_{timestamp}.png"
            )

            # allure.attach.file(
            #     screenshot_path,
            #     name="Failure Screenshot",
            #     attachment_type=allure.attachment_type.PNG
            # )