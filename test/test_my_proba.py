from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()

def test_nexus_6(driver):
    driver.get('https://demoblaze.com/')
    nexus_6 = driver.find_element(By.XPATH, "//a[text()='Nexus 6']")
    nexus_6.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Nexus 6'

def test_laptops(driver):
    driver.get('https://demoblaze.com/index.html')
    laptops_link = driver. find_element(By.CSS_SELECTOR, '''[onclick="byCat('notebook')"]''')
    laptops_link.click()
    time.sleep(2)
    six_laptops = driver.find_elements(By.CSS_SELECTOR, '.card')
    assert len(six_laptops) == 6