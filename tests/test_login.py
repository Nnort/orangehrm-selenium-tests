from config.settings import BASE_URL, VALID_USERNAME, VALID_PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_main_page_opens(driver):
    """Главная страница корректно загружается и отображается"""
    driver.get(BASE_URL)

    assert "OrangeHRM" in driver.title, f"Неожиданный заголовок: {driver.title}"
    assert "/auth/login" in driver.current_url

    assert LoginPage(driver).is_visible(LoginPage.USERNAME), "Поле логина не отображается"


def test_login_with_invalid_credentials_shows_error(driver):
    """При попытке авторизации с неверными данными появляется ошибка, вход не происходит"""
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login("test", "test")

    error_text = login_page.get_error_text()
    assert "Invalid credentials" in error_text, f"Отличается текст ошибки: {error_text}"

    assert "dashboard" not in driver.current_url, "Вход выполнен с неверными данными"


def test_login_with_valid_credentials_success(driver):
    """Авторизация с корректными данными успешная, происходит редирект на дашборд - страницу авторизованного пользователя"""
    driver.get(BASE_URL)

    LoginPage(driver).login(VALID_USERNAME, VALID_PASSWORD)

    assert "dashboard" in driver.current_url, "Вход не выполнен, редирект на дашборд не произошел"


def test_logout(driver):
    """Выход из системы редиректит на главную страницу. Сессия завершается - прямой доступ к дашборду недоступен"""
    driver.get(BASE_URL)

    LoginPage(driver).login(VALID_USERNAME, VALID_PASSWORD)
    DashboardPage(driver).logout()

    assert "/auth/login" in driver.current_url

    driver.get(f"{BASE_URL}/web/index.php/dashboard/index")
    assert "auth/login" in driver.current_url, "Сессия не завершена: доступ к дашборду сохранился"
