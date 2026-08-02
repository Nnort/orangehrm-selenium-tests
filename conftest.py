import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Новый браузер на каждый тест: изоляция важнее скорости на текущем объёме."""
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, TIMEOUT)
