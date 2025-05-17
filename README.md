
# Пример организации автотестирования для веб-сайта <a target="_blank" href="https://vc.ru/">Vc.ru</a>
> Vc.ru — Это крупнейшая в рунете платформа, где публикуются ключевые новости, мнения, обзоры и аналитика. 
> Материалы пишут и сотрудники редакции, и пользователи платформы.

## :open_book: Содержание:
- [Описание проекта](#heavy_check_mark-описание)
- [Кратко](#heavy_check_mark-кратко)
- [Технологии и инструменты](#gear-технологии-и-инструменты)
- Что проверяем:
  - [UI](#heavy_check_mark-реализованные-ui-проверки)
- Запуск тестов:
  - [Jenkins](#-запуск-тестов-из-jenkins)
  - [Локально](#computer-локальный-запуск)
- Отчеты:
  - [Allure](#bar_chart-отчеты-о-прохождении-тестов-доступны-в-allure)
  - [Telegram](#-telegram)
- [Allure TestOps](#briefcase-проект-интегрирован-с-allure-testops)
- [Видео прогона теста](#movie_camera-пример-видео-тестового-прогона)


## :heavy_check_mark: Описание
В проекте представлен пример UI автоматизации тестирования на Python. 
<p>При написании тестов использовался шаблон проектирования PageObjects.
<p>Выделены тест-кейсы.
<p>Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео, etc). 
В тестах отображен тип передачи шагов теста в отчет:
 
- Лямбда-степы через with allure.step

<p>Также по факту прохождения теста отправляется уведомление с результатами в Telegram.
<p>Браузер в запускается удаленно в Selenoid.
<p>Реализована интеграция с Allure TestOps.

## :heavy_check_mark: Кратко
- [x] `Page Object` с шагами 
- [x] Запуск тестов, используя `Jenkins` и `Selenoid`
- [x] `Allure Reports` с вложениями (логи, скриншоты, видео)
- [x] Интеграция с `Allure TestOps`
- [x] Отправка результатов тестирования в `Telegram`

## :gear: Технологии и инструменты:

<div align="center">
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/python-original-wordmark.svg" 
    title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/pytest-original-wordmark.svg" 
    title="Pytest" alt="Pytest" width="45" height="45"/>&nbsp; 
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selenium-original1.svg" 
    title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;  
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selene.png" 
    title="Selene" alt="Selene" width="50" height="50"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selenoid1.png" 
    title="Selenoid" alt="Selenoid" width="40" height="40"/>&nbsp;  
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/pycharm-original.svg" 
    title="PyCharm" alt="PyCharm" width="40" height="40"/>&nbsp;    
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/jenkins-original.svg" 
    title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/Allure.svg" 
    title="Allure Report" alt="Allure Report" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/AllureTestOps.png" 
    title="Allure TestOps" alt="Allure TestOps" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/telegram1.png" 
    title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp;
</div>

## :heavy_check_mark: Реализованные проверки

> - Проверка отображения компонентов хедера при открытии страницы
> - Проверка контента карточек при выборе темы в боковой панели "Темы":
>   - Проверка на соответствие названия титульной карточки и выбранной темы
>   - Проверка на соответствие никнейма титульной карточки и выбранной темы
>   - Проверка, что все дополнительные карточки на странице имеют тег выбранной темы
> - Проверка контента карточек при выборе информационного раздела в боковой панели "vc.ru" 
>   - Проверка автора титульной карточки в разделах "О проекте", "Правила", "Реклама" 
>   - Проверка названия титульной карточки в разделах "О проекте", "Правила", "Реклама"
>   - Проверка текста модального окна в разделе "Приложения"
>   - Проверка отображения qr-кода в разделе "Приложения"


## <img width="4%" title="Jenkins" src="https://github.com/Yunaika/yunaika/blob/main/img/logos/jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/juliamur_python_autotests_stepik_diplom/)

Для запуска тестов из Jenkins:
1. Нажмите кнопку "Build with Parameters"

<p><img src="media/screenshots/jenkins_1.jpg" alt="Jenkins"/></p>

2. Выберите параметры

<p><img src="media/screenshots/jenkins_2.jpg" alt="Jenkins"/></p>

3. Нажмите "Build"

## :computer: Локальный запуск 

1. Склонируйте репозиторий
2. Установите зависимости `pip install -r requirements.txt`
3. Откройте проект в PyCharm, установите интерпретатор
4. Создайте `.env` файл, пример файла - `.env.example`
5. Запустите тесты в PyCharm или в командной строке:
```bash
pytest --browser_version={BROWSER_VERSION} 
```

### :heavy_plus_sign: Параметры сборки

> - BROWSER_VERSION — версия браузера _(chrome: 128.0, 127.0), по умолчанию 128.0

## :bar_chart: Отчеты о прохождении тестов доступны в Allure

> При локальном запуске введите в командной строке: 
```bash
pytest tests
```

### <img width="3%" title="Allure" src="https://github.com/Yunaika/yunaika/blob/main/img/logos/Allure.svg"> Allure

#### Примеры отображения тестов

<img src="..." alt="Allure"/>

<img src="..." alt="Allure"/>

### <img width="2.5%" title="Telegram" src="https://github.com/Yunaika/yunaika/blob/main/img/logos/telegram.png"> Telegram

Настроена отправка отчета в Telegram

<img src="..." alt="Telegram"/>


## :briefcase: Проект интегрирован с Allure TestOps 

#### Cобраны тест-кейсы

<img src="..." alt="Allure TestOps"/>

#### Представлены дашборды аналитики

<img src="..." alt="Allure TestOps"/>

## :movie_camera: Пример видео тестового прогона

В отчетах Allure для каждого теста прикрепленs скриншот, лог и видео прохождения теста

<p align="center">
  <img title="Video" src="...">
</p>