import allure

from vc_ru_tests.data.data import subsite_card_info, author_name_vc, about_project_title, rules_title, \
    author_name_promo, advertising_name, apps_title, rules, advertising, apps
from vc_ru_tests.models.app import app


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Хедер')
@allure.title('Отображения компонентов хедера при открытии страницы')
@allure.link('https://vc.ru')
def test_should_be_visible_buttons_in_header(browser_manager):
    app.main_page.open_main_page()

    app.main_page.should_be_visible_logo_in_header()
    app.main_page.should_be_visible_main_header()
    app.main_page.should_be_visible_search_button()
    app.main_page.should_be_visible_button_editor()
    app.main_page.should_be_visible_button_auth()


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Боковая панель "Темы"')
@allure.title('Проверка вкладок бокового меню')
@allure.link('https://vc.ru')
def tests_should_be_visible_content_section_topics(browser_manager):
    app.main_page.open_main_page()

    app.sidebar_components.clickable_icon_chevron_down()
    app.sidebar_components.should_be_visible_content_section_topics(subsite_card_info)


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Боковая панель "vc.ru"')
@allure.title('Проверка информационного раздела')
@allure.link('https://vc.ru')
def test_should_be_visible_content_info(browser_manager):
    app.main_page.open_main_page()

    with allure.step(f'Проверяем раздел "О {about_project_title}"'):
        app.sidebar_components.should_be_visible_content_about_project(author_name_vc, about_project_title)
    with allure.step(f'Проверяем раздел "{rules}"'):
        app.sidebar_components.should_be_visible_content_rules(author_name_vc, rules_title)
    with allure.step(f'Проверяем раздел "{advertising}"'):
        app.sidebar_components.should_be_visible_content_advertising(author_name_promo, advertising_name)
    with allure.step(f'Проверяем раздел "{apps}"'):
        app.sidebar_components.should_be_visible_content_apps(apps_title)
