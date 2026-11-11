from app.user_service import create_user, get_user


def test_create_user():
    user = create_user("Arjun", "arjun@example.com")

    assert user["name"] == "Arjun"
    assert user["email"] == "arjun@example.com"


def test_get_user():
    user = get_user(101)

    assert user["id"] == 101
    assert user["name"] == "Arjun"
