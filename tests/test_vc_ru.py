import allure

from vc_ru_tests.data.data import subsite_card_info, author_name_vc, about_project_title, rules_title, \
    author_name_promo, advertising_name, apps_title, rules, advertising, apps
from vc_ru_tests.models.app import app


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Хедер')
@allure.title('Проверка отображения компонентов хедера при открытии страницы')
@allure.link('https://vc.ru')
def test_header(browser_open):
    app.main_page.should_be_visible_header()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Боковая панель "Темы"')
@allure.title('Проверка контента карточек на соответствие выбранной темы из боковой панели')
@allure.link('https://vc.ru')
def test_sidebar_topics(browser_open):
    with allure.step('Кликаем кнопку "Показать все"'):
        app.sidebar_page.clickable_icon_chevron_down()

    app.sidebar_page.should_be_visible_content_sidebar_section_topics(subsite_card_info)


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Боковая панель "vc.ru"')
@allure.title('Проверка контента карточек на соответствие выбранному разделу боковой панели')
@allure.link('https://vc.ru')
def test_sidebar_info(browser_open):
    with allure.step(f'Выбираем раздел "О {about_project_title}"'):
        app.sidebar_page.should_be_visible_content_about_project(author_name_vc, about_project_title)
    with allure.step(f'Выбираем раздел "{rules}"'):
        app.sidebar_page.should_be_visible_content_rules(author_name_vc, rules_title)
    with allure.step(f'Выбираем раздел "{advertising}"'):
        app.sidebar_page.should_be_visible_content_advertising(author_name_promo, advertising_name)
    with allure.step(f'Выбираем раздел "{apps}"'):
        app.sidebar_page.should_be_visible_content_apps(apps_title)
