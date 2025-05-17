import allure
from selene import browser, have, be

from vc_ru_tests.data.data import apps, advertising, rules


class SideBarPage:
    def __init__(self):
        self.icon_chevron_down = browser.element('.sidebar-item > .icon--chevron_down')

        self.card_name = browser.element('.subsite-card__name')
        self.card_nickname = browser.element('.subsite-card__nickname')
        self.topics = browser.all('.content-header__topic')
        self.element_topic = '.content-header__topic'

        self.href_about = browser.element('[href="/about"]')
        self.href_rules = browser.element('[href="/rules"]')
        self.href_ads = browser.element('[href="/ads"]')
        self.href_apps = browser.element('[href="/apps"]')

        self.all_content = browser.all('.content')
        self.author_name = self.all_content[0].element('.author__name')

        self.content_title_editorial = self.all_content[0].element('.content-title__editorial')
        self.content_title = self.all_content[0].element('.content-title')

        self.apps_page_title = browser.element('.apps-page__title')
        self.apps_page_qr = browser.element('.apps-page__qr')

    def clickable_icon_chevron_down(self):
        self.icon_chevron_down.click()

    def should_be_visible_content_subsite_cards(self, name, nick_name):
        with allure.step(f'Кликаем раздел "{name}"'):
            browser.element(f'[href="/{nick_name}"]').click()
        with allure.step(f'Проверяем название титульной карточки "{name}"'):
            self.card_name.should(have.exact_text(name))
        with allure.step(f'Проверяем никнейм титульной карточки "@{nick_name}"'):
            self.card_nickname.should(have.exact_text(f'@{nick_name}'))

        with allure.step(f'Проверяем, что все дополнительные карточки на странице имеют тег "{name}"'):
            for topic in self.topics:
                topic.element(self.element_topic).should(have.exact_text(name))

    def should_be_visible_content_sidebar_section_topics(self, top):
        for name, nick_name in top.items():
            with allure.step(f'Выбираем тему "{name}" в боковой панели '):
                self.should_be_visible_content_subsite_cards(name, nick_name)

    def should_be_visible_content_about_project(self, name, title):
        with allure.step(f'Кликаем раздел "О {title}"'):
            self.href_about.click()
        with allure.step(f'Проверяем автора титульной карточки "{name}"'):
            self.author_name.should(have.exact_text(name))
        with allure.step(f'Проверяем название титульной карточки "О {title}"'):
            self.content_title_editorial.should(have.exact_text(title))

    def should_be_visible_content_rules(self, name, title):
        with allure.step(f'Кликаем раздел "{rules}"'):
            self.href_rules.click()
        with allure.step(f'Проверяем автора титульной карточки "{name}"'):
            self.author_name.should(have.exact_text(name))
        with allure.step(f'Проверяем название титульной карточки "{title}"'):
            self.content_title.should(have.exact_text(title))

    def should_be_visible_content_advertising(self, name, title):
        with allure.step(f'Кликаем раздел "{advertising}"'):
            self.href_ads.click()
        with allure.step(f'Проверяем автора титульной карточки "{name}"'):
            self.author_name.should(have.exact_text(name))
        with allure.step(f'Проверяем название титульной карточки "{title}"'):
            self.content_title.should(have.exact_text(title))

    def should_be_visible_content_apps(self, title):
        with allure.step(f'Кликаем раздел "{apps}"'):
            self.href_apps.click()
        with allure.step(f'Проверяем текст модального окна "{title}"'):
            self.apps_page_title.should(have.exact_text(title))
        with allure.step(f'Проверяем отображение qr-кода'):
            self.apps_page_qr.should(be.visible)
