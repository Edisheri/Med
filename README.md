# Med - Медицинская Диагностика

## Описание

Med - это веб-приложение для медицинской диагностики, созданное с использованием фреймворка Django. Приложение позволяет управлять пользователями, корзинами покупок, заказами и предоставляемыми медицинскими услугами.

## Технологии

- **Python**
- **Django v4.2.7**
- **PostgreSQL**
- **HTML, CSS**
- **Django Templates**
- **Django Forms**
- **Git**

## Функциональность

- **Управление пользователями**: регистрация, аутентификация, авторизация
- **Корзина покупок**: добавление, удаление и просмотр товаров
- **Заказы**: создание и управление заказами
- **Медицинские услуги**: просмотр и заказ медицинских услуг

## Установка и Настройка

1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/Edisheri/Med.git
   cd Med
2. **Создание и активация виртуального окружения**
   python -m venv env
   source env/bin/activate  # Для Windows используйте `env\Scripts\activate`

3. **Установка зависимостей**
   ```pip install -r requirements.txt```
4. **Настройка переменных окружения**
   Создайте файл .env в корне проекта и заполните его следующими данными:
   ```SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_NAME=your_db_name
   DATABASE_USER=your_db_user
   DATABASE_PASSWORD=your_db_password
   DATABASE_HOST=your_db_host
   DATABASE_PORT=your_db_port```

5. **Создание базы данных и применение миграций**
   ```python manage.py makemigrations
   python manage.py migrate```
6. **Создание суперпользователя**
   ```python manage.py createsuperuser```
7. **Запуск сервера разработки**
   ```python manage.py runserver```

## Структура проекта 

```Med/
├── MedSite/                 # Основное приложение Django
│   ├── __init__.py
│   ├── settings.py         # Настройки проекта
│   ├── urls.py             # URL маршруты проекта
│   ├── wsgi.py             # Настройки WSGI для развертывания
│   └── asgi.py             # Настройки ASGI для развертывания
├── carts/                   # Приложение для управления корзинами
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── fixtures/                # Тестовые данные
│   └── services/
├── media/                   # Загружаемые файлы
│   └── services_images/
├── orders/                  # Приложение для управления заказами
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── services/                # Приложение для управления услугами
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/                  # Статические файлы (CSS, JavaScript и т.д.)
├── templates/               # Шаблоны HTML
├── users/                   # Приложение для управления пользователями
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── .gitignore               # Файлы и директории, игнорируемые Git
├── README.md                # Файл описания проекта
├── manage.py                # Основной файл управления Django
└── requirements.txt         # Зависимости проекта```

 
