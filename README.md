# 🌱 Agronote Backend Template

Стартовый шаблон бэкенд-проекта на Python с использованием Litestar. Подходит для микросервисов, REST API и ML-интеграций в сфере агропромышленности, предиктивной аналитики и автоматизации.

---

## 📌 Назначение

Шаблон предназначен для:
- быстрых стартов Python API-проектов,
- создания микросервисов с REST-интерфейсом,
- проектов, связанных с агроаналитикой, сенсорами, метео-данными,
- командной разработки с фокусом на качество кода и CI/CD.

---

## ⚙️ Технологический стек

- **Язык**: Python 3.10
- **Фреймворк**: [Litestar](https://docs.litestar.dev/) 2.x — асинхронный API-фреймворк
- **Сервер**: Uvicorn (ASGI)
- **Валидация**: Pydantic
- **Тестирование**: Pytest
- **Форматирование и анализ**: Ruff, Black, Isort
- **CI/CD**: GitHub Actions
- **Сборка и запуск**: Docker, Docker Compose

---

## 🚀 Быстрый старт

### Установка зависимостей

```bash
poetry install
```

## ✅ Часто используемые команды

### Проверка кода
```bash
poetry run isort --check-only .
poetry run black --check .
poetry run ruff check .
```
### Автоисправление
```bash
poetry run isort .
poetry run black .
poetry run ruff check . --fix
```
### Запуск тестов
```bash
poetry run pytest
```

### 📁 Структура проекта
```text
agronote-template/
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions: пайплайн CI для линтинга и тестов
├── docker/
│   └── Dockerfile               # Инструкция по сборке контейнера приложения
├── src/
│   └── app/
│       ├── api/
│       │   └── routes.py        # HTTP-роуты (контроллеры) Litestar
│       ├── models/
│       │   ├── weather_orm.py   # ORM-модель для работы с БД (SQLAlchemy)
│       │   ├── weather_dto.py   # Pydantic-схема (DTO) для обмена погодными данными
│       │   └── field_data.py    # Заглушка модели данных поля
│       ├── repositories/
│       │   ├── field_repository.py     # Репозиторий для доступа к данным полей
│       │   └── weather_repository.py   # Интерфейс и заглушка репозитория погоды
│       ├── schemas/
│       │   └── field_schema.py         # Pydantic-схема для валидации данных полей
│       ├── services/
│       │   ├── irrigation.py           # Расчёт оптимального полива 
│       │   ├── weather_interface.py    # Интерфейс сервиса погоды
│       │   └── weather_service.py      # Заглушка сервиса получения погодных данных
│       └── main.py                     # Точка входа приложения Litestar
├── tests/
│   └── test_root.py             # Юнит-тесты корневого роута и бизнес-логики
├── docker-compose.yml           # Композиция сервисов 
├── pyproject.toml               # Конфигурация Poetry, зависимостей, линтеров и форматеров
└── README.md                    # Описание проекта
```


### 🧰 Используемые инструменты

| Инструмент |	Назначение
|------------|-------------
| Poetry	| Менеджер зависимостей и окружений
| Black	| Автоформатирование кода
| Isort	| Упорядочивание импортов
| Ruff	| Быстрый линтер и проверка стиля
| Pytest	| Фреймворк для тестирования
| GitHub  | Actions	Автоматический CI/CD
| Docker	| Сборка и запуск приложения в контейнере



### 💬 Контакты
-----
Разработано в рамках тестового задания Agronote.
#### Автор: [Gevorg Khachatryan](https://github.com/Gevorg2799)
#### Email: [gevorg2799@mail.ru](mailto:gevorg2799@mail.ru)