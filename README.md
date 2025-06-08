# Интеллектуальный антивирус для веб-приложений на Python

## Структура проекта

1.  [Статический анализатор](https://github.com/smirkinhd/PythonAnalyzer/tree/main/static_analyzer) 
   - Цель: 
     - найти вредоносные конструкции до выполнения кода.
     - Что проверяет:
       - Встроенные (inline) JavaScript-скрипты
       - Подключенные внешние скрипты
       - Опасные шаблоны JavaScript-кода
       - Признаки обфускации
2. [Динамический анализатор](https://github.com/smirkinhd/PythonAnalyzer/tree/main/dynamic_analyzer)
   - Цель:
     - Запустить HTML/JS-код в изолированной среде (например, Docker, виртуальной машине или headless-браузере) и отслеживать его поведение, чтобы обнаружить вредоносные действия, которые невозможно выявить статическим анализом.
   - Что делает:
     - Открывает страницу в headless-браузере (Chromium) с помощью Playwright.
     - Собирает данные со страницы:
        - Cookies
        - LocalStorage
        - SessionStorage
        - Сообщения консоли (console.log и другие)
        - Выводит собранные данные в консоль.
        - Автоматически закрывает браузер и сервер после анализа.
     - Как запустить:

          1. Ручками
             ```bash
             python analyze_dynamic.py suspicious.html
             ```

          2. Через докер образ:

             2.1

             ```bash
             docker pull smirkinhd7/pythonanalyzerimage:v4
             ```

             2.2
             
             ```bash
             docker run --rm -v ${PWD}:/app -p 8080:8000 smirkinhd7/pythonanalyzerimage:v4 python /app/analyze_dynamic.py /app/suspicious.html
             ```
       
