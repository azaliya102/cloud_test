Данный проект включает автоматизированные тесты для проверки сайта [example.com] с использованием **Selenium WebDriver** и **pytest**.

## Требования

Перед запуском убедитесь, что у вас установлены следующие библиотеки и инструменты:

| Библиотека | Версия |
|:-----------|:-------|
| `attrs` | 24.2.0 |
| `certifi` | 2025.4.26 |
| `cffi` | 1.15.1 |
| `exceptiongroup` | 1.2.2 |
| `greenlet` | 2.0.2 |
| `h11` | 0.14.0 |
| `idna` | 3.10 |
| `importlib-metadata` | 6.7.0 |
| `outcome` | 1.3.0.post0 |
| `playwright` | 1.35.0 |
| `pycparser` | 2.21 |
| `pyee` | 9.0.4 |
| `PySocks` | 1.7.1 |
| `selenium` | 4.11.2 |
| `sniffio` | 1.3.1 |
| `sortedcontainers` | 2.4.0 |
| `trio` | 0.22.2 |
| `trio-websocket` | 0.11.1 |
| `typing-extensions` | 4.7.1 |
| `urllib3` | 2.0.7 |
| `wsproto` | 1.2.0 |
| `zipp` | 3.15.0 |
| `pytest` | последняя версия |

Все зависимости можно установить командой:

```bash
pip install -r requirements.txt
```

Также необходимо наличие установленного браузера **Google Chrome**.

## Установка

1. Клонируйте репозиторий или скачайте проект.
2. Создайте виртуальное окружение:
    ```bash
    python -m venv venv
    ```
3. Активируйте окружение:
    - Windows:
      ```bash
      venv\Scripts\activate
      ```
    - Linux/macOS:
      ```bash
      source venv/bin/activate
      ```
4. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск тестов

Для запуска всех тестов используйте команду:

```bash
pytest
```

Для запуска с подробным выводом:

```bash
pytest -v
```

Тесты находятся в папке `tests/`.

## Структура проекта

```
cloud_test/
├── example_page.py
├── tests/
│   └── test_example_selenium.py
├── conftest.py
├── requirements.txt
└── README.md
```

## Заметки

- Для загрузки и управления ChromeDriver используется пакет **webdriver-manager**.
- Для автоматизации браузера используется **Selenium WebDriver**.
- Для запуска и организации тестов используется **pytest**.

