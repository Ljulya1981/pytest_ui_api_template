# pytest_ui_api_template

## Описание и структура проекта

### Шаги:
1. Склонировать проект 'git clone https://github.com/Ljulya1981/pytest_ui_api_template.git'
2. Установить зависимости
3. Запустить тесты: 'pytest -s -v'
4. Запустить только ui тесты: "pytest -m ui"
5. Запустить только api тесты: "pytest -m api"
6. Запустить тесты с allure: "pytest --alluredir allure-result"
7. Установить утилиту Allure Report 
   (для Windows): "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression"; 
   (для macOS): "/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   "+" "scoop install allure"                    
8. Создание отчета "allure serve allure-result"

### Стек:
    - pytest
    - selenium
    - requests
    - _sqlalchemy_
    - allure
    - config

### Cтруктура:
    - ./test - тесты
    
### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignor](https://www.toptal.com/developers/gitignore)

### Библиотеки:
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure
- pip install allure-pytest
- pip install SQLAlchemy

### Ссылка на финальный проект
- https://studentskypro.yonote.ru/share/ba89b5e3-84ae-4619-8242-ebe9cc477e69