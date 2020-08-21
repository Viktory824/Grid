from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test:

    def test_go_to_card(self, driver):
        driver.get('https://beru.ru')

        el = driver.find_element_by_css_selector("[data-zone-name='headerCatalog']")
        el.click()

        wait = WebDriverWait(driver, 5)
        el = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Бытовая техника")))
        el.click()

        title_page = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='rPzd7GVCYx _1s00-3EuYB']")))
        assert title_page.text == 'Бытовая техника'

    def test_go_to_google(self, driver):
        driver.get('http://google.com')

        el = driver.find_element_by_name('q')
        el.send_keys('browserstack')
        el.send_keys(Keys.ENTER)
        sleep(3)
        assert 'browserstack' in driver.title

    def test_go_to_avito_avto(self, driver):
        driver.get('http://avito.ru')
        courses = driver.find_element_by_xpath("//a[text()='Авто']")
        courses.click()

    def test_go_to_avito_property(self, driver):
        driver.get('http://avito.ru')
        courses = driver.find_element_by_xpath("//a[text()='Недвижимость']")
        courses.click()

    def test_go_to_otus_testing(self, driver):
        driver.get('http://otus.ru')

        courses = driver.find_element_by_xpath("//div[@id='categories_id']//*[@title='Тестирование']")
        courses.click()

    def test_go_to_otus_development(self, driver):
        driver.get('http://otus.ru')

        courses = driver.find_element_by_xpath("//div[@id='categories_id']//*[@title='Data Science']")
        courses.click()
