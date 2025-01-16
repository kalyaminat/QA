from users import UsersTable

db = UsersTable("postgresql://postgres:postgres@localhost:5432/QA")


def test_add_new_user():
    body = db.get_users()
    len_before = len(body)

    email = 'petrov@mail.ru'
    db.add_user(email)

    body = db.get_users()
    len_after = len(body)

    new_user = db.get_user_email(email)

    db.delete(email)
    assert new_user['user_email'] == email
    assert len_after - len_before == 1


def test_edit_user():
    email = 'petrov@mail.ru'
    db.add_user(email)

    new_email = 'ivanov@yandex.ru'
    db.edit_user(new_email, email)

    edited = db.get_user_email(new_email)

    db.delete(new_email)
    assert edited['user_email'] == new_email


def test_delete_user():
    email = 'petrov@mail.ru'
    db.add_user(email)

    db.delete(email)

    new_user = db.get_all_user_email(email)

    assert len(new_user) == 0