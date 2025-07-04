# Diplom_project
# Автоматизированные тесты для КИНОПОИСКА

## Данный проект содержит автоматизированные UI и API тесты для тестирования веб-сайта "Кинопоиск"

### Стек:
- pytest
- selenium
- requests
- allure

### Структура проекта:
- Config/ - настройки и тестовые данные
- KinoPages/ - Page Object модели
- Tests/ - тесты (UI и API)
- Utils/ - вспомогательные утилиты

### Библиотеки:
- pip install pytest
- pip install selenium
- pip install requests
- pip install webdriver-manager
- pip install allure-pytest
- pip install allure-python-commons

### Предварительные требования
Перед началом работы необходимо убедиться, что у вас установлены:
- python версии 3.8 или новее
- браузеры Chrome и Firefox
- Allure Commandline [Инструкция по установке](https://allurereport.org/docs/#_installing_a_commandline)

### Шаги:
1. [Склонировать репрозиторий github](https://github.com/840227lenaelina/Diplom_project.git)
2. Установить зависимости из файла requirements.txt
3. Провести тестирование:
 - Запуск всех тестов: pytest -v
 - Запуск только UI тестов: pytest Tests/test_ui.py -m "ui" --alluredir=allure-results
 - Запуск только API тестов: pytest Tests/test_api.py -m "api" --alluredir=allure-results
4. Сгенерировать отчет Allure: allure serve allure-results
5. Изменить тестовые данные можно в файле: Config.test_data.py
