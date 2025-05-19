import allure
from selene import browser, be, have


class MainPage:
    def __init__(self):
        self.header_left = browser.element('.header__left > a')
        self.header_main = browser.element('.header__main')
        self.search_button = browser.element('.search__button')
        self.button_editor = browser.element('.header__right > [href="/editor"] > button')
        self.button_auth = browser.element('.header__right > [href="/auth"] > button')

    @allure.step('Открываем Главную страницу')
    def open_main_page(self):
        browser.open('/')

    @allure.step('Проверяем отображение логотипа')
    def should_be_visible_logo_in_header(self):
        self.header_left.should(be.visible)

    @allure.step('Проверяем отображение основного контента хедера')
    def should_be_visible_main_header(self):
        self.header_main.should(be.visible)

    @allure.step('Проверяем отображение кнопки поиска')
    def should_be_visible_search_button(self):
        self.search_button.should(be.visible)

    @allure.step('Проверяем отображение кнопки "Написать"')
    def should_be_visible_button_editor(self):
        self.button_editor.should(be.visible)

    @allure.step('Проверяем отображение кнопки "Войти"')
    def should_be_visible_button_auth(self):
        self.button_auth.should(be.visible)
