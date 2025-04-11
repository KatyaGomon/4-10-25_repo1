import time
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')


    #driver.get('https://demoblaze.com/')
    #galaxy_s6 = driver.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
    #galaxy_s6.click()
    #title = driver.find_element(By.CSS_SELECTOR, 'h2')
    #assert title.text == 'Samsung galaxy s6'

def test_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_products_count(2)


    #driver.get('https://demoblaze.com/index.html')
    #monitor = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    #monitor.click()
    #time.sleep(2)
    #two_monitors = driver.find_elements(By.CSS_SELECTOR, '.card')
    #assert len(two_monitors) == 2







