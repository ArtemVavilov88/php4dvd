from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Application(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)


    def go_to_home_page(self):
        self.driver.get(self.base_url)


    def login(self, user):
        driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user.username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user.password)
        driver.find_element_by_name("submit").click()


    def creating_film_positive(self, film):
        driver = self.driver
        #film's quantity before creating
        quantity_before = driver.find_elements_by_class_name("movie_cover")
        driver.find_element_by_link_text("Add movie").click()
        driver.find_element_by_name("imdbid").send_keys(film.IMDb_number)
        driver.find_element_by_name("name").send_keys(film.Title)
        driver.find_element_by_name("aka").send_keys(film.Also_known_as)
        driver.find_element_by_name("year").send_keys(film.Year)
        driver.find_element_by_name("duration").send_keys(film.Duration_minutes)
        driver.find_element_by_id("own_no").click()
        driver.find_element_by_name("plots").send_keys(film.Plots)
        driver.find_element_by_id("submit").click()
        #checking film's name
        getText = driver.find_element_by_tag_name("h2").text
        print getText
        #film's quantity after creating
        driver.find_element_by_link_text("Home").click()
        quantity_after = driver.find_elements_by_class_name("movie_cover")
        #checking adding film
        result = len(quantity_after)-len(quantity_before)
        if result == 1:
            print "The film was added successfully"
        else:
            print "Test fail"


    def creating_film_negative(self, film):
        driver = self.driver
        #film's quantity before creating
        quantity_before = driver.find_elements_by_class_name("movie_cover")
        driver.find_element_by_link_text("Add movie").click()
        driver.find_element_by_name("imdbid").send_keys(film.IMDb_number)
        driver.find_element_by_name("aka").send_keys(film.Also_known_as)
        driver.find_element_by_name("year").send_keys(film.Year)
        driver.find_element_by_name("duration").send_keys(film.Duration_minutes)
        driver.find_element_by_id("own_no").click()
        driver.find_element_by_name("plots").send_keys(film.Plots)
        driver.find_element_by_id("submit").click()
        #checking error message
        getText_error = driver.find_element_by_tag_name("label").text
        print getText_error
        #film's quantity after unsuccessful creating
        driver.find_element_by_link_text("Home").click()
        quantity_after = driver.find_elements_by_class_name("movie_cover")
        result = len(quantity_after)-len(quantity_before)
        if result == 0:
            print "The film didn't create"
        else:
            print "Test fail"


    def delete_film(self):
        driver = self.driver
        #film's quantity before deleting
        quantity_before = driver.find_elements_by_class_name("movie_cover")
        #just find the first element with class="title"
        driver.find_element_by_class_name("title").click()
        driver.find_element_by_link_text("Remove").click()
        #accept the "Are you sure you want to remove this?" dialog
        driver.switch_to_alert().accept()
        #film's quantity after deleting
        quantity_after = driver.find_elements_by_class_name("movie_cover")
        result = len(quantity_before) - len(quantity_after)
        if result == 1:
            print "The film was deleted successfully "
        else:
            print "Test fail"


    def search_film_positive(self, film):
        driver = self.driver
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(film.Search_field)
        time.sleep(1)
        driver.find_element_by_id("q").click()
        time.sleep(1)
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        time.sleep(2)
        # There is the film which was found
        driver.find_element_by_class_name("movie_cover").click()
        get_Title_Name = driver.find_element_by_tag_name("h2").text
        print "The film which was searched -",get_Title_Name


    def search_film_negative(self, film):
        driver = self.driver
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(film.Search_field)
        time.sleep(1)
        driver.find_element_by_id("q").click()
        time.sleep(1)
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        time.sleep(2)
        #checking message about searching
        get_message = driver.find_element_by_class_name("content").text
        print get_message


    def is_logged_in(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_all_elements_located((By.CSS_SELECTOR, "nav")))
            return True
        except WebDriverException:
            return False


    def is_not_logged_in(self):
        driver = self.driver
        try:
           self.wait.until(presence_of_all_elements_located((By.ID, "loginform")))
           return True
        except WebDriverException:
            return False


    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Log out").click()
        driver.switch_to_alert().accept()
