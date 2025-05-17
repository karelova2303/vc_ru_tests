import allure
from selene import browser, be


class MainPage:
    def __init__(self):
        self.header_left = browser.element('.header__left')
        self.header_main = browser.element('.header__main')
        self.header_right = browser.element('.header__right')

    def should_be_visible_header(self):
        with allure.step('Компоненты в левой части хедера отображаются'):
            self.header_left.should(be.visible)
        with allure.step('Компоненты в центре хедера отображаются'):
            self.header_main.should(be.visible)
        with allure.step('Компоненты в правой части хедера отображаются'):
            self.header_right.should(be.visible)
