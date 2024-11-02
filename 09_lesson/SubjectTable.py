from sqlalchemy import create_engine
from sqlalchemy.sql import text


class SadjtctTable:
    scripts = {
                
        "select by": text("select * from subject\
            where subject_title = :db_title"),

        "select by up": text("select * from subject\
            where subject_title = :db_up_title"),

        "select by id": text("select * from subject\
            where subject_id = :db_id"),

        "insert new": text("insert into subject\
            (subject_title, subject_id) values (:new_title, :id)"),
        
        "delete by id": text("delete from subject\
            where subject_id = :id_to_delete"),
        
        "update title": text("update subject\
            set subject_title = :up_title where subject_id = :up_id"),

    }

        
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_subject(self, new_title):
        return self.db.execute(self.scripts["select by"],
        db_title = new_title).fetchall()
    
    def get_subject_up(self, up_title):
        return self.db.execute(self.scripts["select by up"],
        db_up_title = up_title).fetchall()
    
    def get_subject_del(self, id):
        self.db.execute(self.scripts["select by id"],
        db_id = id).fetchall()

    def create_title(self, new_title, id):
        self.db.execute(self.scripts["insert new"],
                new_title=new_title, id=id)

    def update_title(self, up_title, id):
        self.db.execute(self.scripts['update title'],
                up_title=up_title, up_id=id)

    def delete_id(self, id):
        self.db.execute(self.scripts["delete by id"],
                id_to_delete=id)
