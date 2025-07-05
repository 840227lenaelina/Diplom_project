# KinoPages/main_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from Config.settings import BASE_URL


class MainPage(BasePage):
    # Актуальные локаторы
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='text']")  # Поле поиска
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[aria-label='Найти']")  # Кнопка поиска

    # Дополнительные локаторы (уточняются на сайте)
    MODAL_WINDOW = (By.CLASS_NAME,
                    'styles_foregroundImage__zeN5v')  # Модальное окно
    MODAL_BUTTON = (By.XPATH,
                    "//button[text()='Не сейчас']")  # Закрытие модального окна

    def open(self):
        """Открытие главной страницы"""
        self.driver.get(BASE_URL)
        return self

    def is_modal_displayed(self):
        """Проверяет, отображается ли модальное окно"""
        try:
            return self.is_element_visible(self.MODAL_WINDOW)
        except:
            return False

    def close_modal_if_open(self):
        """Закрывает модальное окно, если оно открыто"""
        if self.is_modal_displayed():
            close_button = (self.MODAL_BUTTON)
            self.click(close_button)

    def search_for(self, query):
        """Выполнение поиска"""
        self.type(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
        return self
