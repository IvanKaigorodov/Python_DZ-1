from SubjectTable import SadjtctTable
import pytest


db = SadjtctTable("postgresql://postgres:"
            "SkyproIvan142@localhost:5432/postgres")


def test_edit_subject_title():
    # Новый предмет
    new_title = 'Python-db'
    id = '100'
    db.create_title(new_title, id)

    #  Изменение названия предмета
    up_title = 'NEW'
    db.update_title(up_title, id)

    # Удаление предмета
    db.delete_id(id)
