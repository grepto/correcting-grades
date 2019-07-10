# Скрипты для улучшения показателей в электронном дневнике

С помощью этих скриптов можно исправить оценки 2 и 3 на 5, удалить замечания и добавить похвалу. Cкрипты выполняются
в Django shell'е проекта сайта. Для их использования на компьютере должен быть развернут проект сайта с подключенной БД.
Все зависимости должны быть установлены, миграции сделаны. Инструкции по локальному запуску проекта
[в README](https://github.com/devmanorg/e-diary/blob/master/README.md) проекта Электронный дневник школы

## Запуск

- Откройте файл `scripts.py` и скопируйте его содержимое в буфер обмена
- В терминале перейдите в корневую папку проекта сайта
- Выполните команду `python3 manage.py shell`
- Вставьте содержимое файла `scripts.py` из буфера обмена

## Скрипты
 - `get_schoolkid` - возвращает объект schoolkid. Он понадобится для других скриптов. В качестве аргумента нужно указать
фамилию и имя ученика. Если найдется несколько учеников, вернет первого.
 - `fix_marks` - принимает на вход объект `schoolkid`. Исправляет оценки 2 и 3 на 5.
 - `remove_chastisements` - принимает на вход объект `schoolkid`. Удаляет замечания
 - `add_commendation` - принимает на вход объект `schoolkid` и название школьного предмета. Добавляет похвалу ученику от
преподавателя по предмету. После названия школьного предмета можно передать еще 2 необязательных аргумента:
    - `commendation_text` - текст похвалы. Если не передавать, скрипт использует один
    из [базовых вариантов](https://pedsovet.org/beta/article/30-sposobov-pohvalit-ucenika)
    - `commendation_date` - дата похвалы в формате YYYY-mm-dd. Если не передать, похвала запишется текущей датой.
 

## Использование
После запуска shell'а и копирования в него содержимого `scripts.py`, в нем можно выполнить скрипты


### Пример использования
```python
# Создаем объект `schoolkid`
schoolkid = get_schoolkid('Фролов Иван')

# Исправляем плохие оценки
fix_marks(schoolkid)

# Удаляем замечания
remove_chastisements(schoolkid)

# Добавляем похвалу от учителя матемитики
add_commendation(schoolkid, 'Математика')

# Добавляем похвалу от учителя музыки со своим текстом и конкретной датой
add_commendation(schoolkid, 'Музыка', commendation_text='Красиво поешь!!!', commendation_date='2019-04-25' )
```




