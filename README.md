# Проект "Ранжирование в поиске"
## Описание задачи
В проекте необходимо было разработать сервис, для
ранжирования товаров предлагаемых покупателю на основании локации клиента,
рекламы, конверсий и так далее.

## Описание 

- Сделал первичный разведочный анализ данных (EDA)
- Выявил позиционное и сезонное смещение в данных 
- Обучил модели LambdaMart (в реализации LightGBM), YetiRank (в реализации Catboost) и Ranknet
- Оптимизировал гиперпараметры с помощью Optuna

## Структура репозитория

- `get_recs.py` Получение предсказаний от модели
- `app.py` Flask приложение для обработки запросов
- `zapros.py` Пример запроса к модели
- `rnd` Ноутбуки с исследованием данных и обучением моделей

## Установка и запуск
```bash
$ docker build -t my-app .
```

Запустите докер контейнер следующей командой

```bash
$ docker run -d -p 5000:5000 my-app
```

После запуска приложение будет доступно по адресу http:127.0.0.1:5000