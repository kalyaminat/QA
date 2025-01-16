from sqlalchemy import create_engine
from sqlalchemy import text


class UsersTable:
    scripts = {
        'select': "select * from users",
        'delete by email': text('delete from users where user_email = :user_to_delete'),
        'insert new': text('insert into users(user_email) values (:new_user)'),
        'select by email': text("select * from users where user_email = :select_email"),
        'edit': text("update users set user_email = :edit_email where user_email = :user_email")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def add_user(self, user_email):
        self.db.execute(self.scripts['insert new'], new_user=user_email)

    def edit_user(self, edit_email, email):
        self.db.execute(self.scripts['edit'], edit_email=edit_email, user_email=email)

    def delete(self, user_email):
        self.db.execute(self.scripts['delete by email'], user_to_delete=user_email)

    def get_users(self):
        return self.db.execute(self.scripts['select']).fetchall()

    def get_user_email(self, email):
        return self.db.execute(self.scripts['select by email'], select_email=email).fetchall()[0]

    def get_all_user_email(self, email):
        return self.db.execute(self.scripts['select by email'], select_email=email).fetchall()
