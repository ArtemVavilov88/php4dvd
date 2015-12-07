from selenium import webdriver
from selenium_fixture import app
from model.user import User
from model.info_about_a_film import Film


def test_login_with_valid_data(app):
    app.go_to_home_page()
    app.login(User.admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()

def test_login_with_invalid_data(app):
    app.go_to_home_page()
    app.login(User.random_data())
    assert app.is_not_logged_in()

def test_creating_film_positive(app):
    app.go_to_home_page()
    app.login(User.admin())
    app.creating_film_positive(Film.value_positive())
    app.logout()

def test_creating_film_negative(app):
    app.go_to_home_page()
    app.login(User.admin())
    app.creating_film_negative(Film.value_negative())
    app.logout()

def test_delete_film(app):
    app.go_to_home_page()
    app.login(User.admin())
    app.delete_film()
    app.logout()

def test_search_film_positive(app):
    app.go_to_home_page()
    app.login(User.admin())
    app.search_film_positive(Film.value_search_positive())
    app.logout()

def test_search_film_negative(app):
    app.go_to_home_page()
    app.login(User.admin())
    app.search_film_negative(Film.value_search_negative())
    app.logout()

