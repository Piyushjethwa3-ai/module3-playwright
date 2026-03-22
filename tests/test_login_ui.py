from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert login_page.success_message_visible()