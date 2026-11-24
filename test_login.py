def test_valid_login():
    username = "admin"
    password = "12345"

    assert username == "admin"
    assert password == "12345"

    print("Login test passed")


def test_invalid_login():
    username = "user"
    assert username != "admin"

    print("Invalid login test passed")
