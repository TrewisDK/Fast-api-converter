# Fast-api-converter
Just a currency converter

Просто конвертер написанный на фреймворке FastApi.
Данные о курсах мы получаем от google с помощью модуля requests и beautifulsoup4.

Запрос:
GET: /api/rates?_from=RUB&_to=EUR&value=100

Зависимости:
fastapi==0.88.0
requests==2.28.1
beautifulsoup4==4.11.1
uvicorn==0.20.0
lxml==4.9.2

Почему FastAPI?
В отличии от Django Rest Framework который в большинстве случаев используется для написания Rest Api, FastAPi куда лучше подходит для написания микросервисов,
в которых не требуется работа с базой данных, в первую очередь из за ускорения разработки и развертывания.
