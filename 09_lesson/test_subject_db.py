from SubjectTable import SadjtctTable
import pytest


db = SadjtctTable("postgresql://postgres:"
            "SkyproIvan142@localhost:5432/postgres")


def test_add_subject():
    # Добавить в базу новый предмет
    new_title = 'Новый предмет'
    id = 100
    db.create_title(new_title, id)
    # Выбрать из базы новый предмет
    add_subject = db.get_subject(new_title)
    db.delete_id(id)
    # Проверить совпадение названия предметов
    assert [(id, new_title)] == add_subject


def test_edit_subject_title():
    # Добавить в базу новый предмет
    new_title = 'Новый предмет'
    id = 100
    db.create_title(new_title, id)
    #  Изменение названия предмета
    up_title = 'Заменил название'
    db.update_title(up_title, id)
    edit_subject = db.get_subject_up(up_title)
    # Удаление предмета
    db.delete_id(id)
    # Проверить совпадения измененного названия
    assert [(id, up_title)] == edit_subject


def test_del_subject():
    # Добавить в базу новый предмет
    new_title = 'Новый предмет'
    id = 100
    db.create_title(new_title, id)
    # Выбрать из базы новый предмет по id
    rows = db.get_subject_del(id)
    # Удалить из базы новый предмет по id
    db.delete_id(id)
    # Проверить отсутствие предмета по id
    assert rows == None