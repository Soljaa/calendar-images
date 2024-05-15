from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

import chromedriver_autoinstaller
import time


def print_tables(driver, name):
    while True:
        try:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, '_g2s11rv')))
            time.sleep(0.5)
            table = driver.find_element(By.CLASS_NAME, '_g2s11rv')
            time.sleep(0.5)
            table.screenshot(f"calendarAirbnb{name}.png")
            break
        except StaleElementReferenceException:
            pass


def click_next_month(driver):
    while True:
        try:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, '_qz9x4fc')))
            next_months_btn = driver.find_element(By.CLASS_NAME, '_qz9x4fc')
            next_months_btn.click()
            time.sleep(0.5)
            break
        except StaleElementReferenceException:
            pass


def main():
    options = Options()
    driver = webdriver.Chrome(options=options)

    url = "https://www.airbnb.com.br/rooms/52668572#availability-calendar"
    driver.get(url)
    # eventual popup
    try:
        time.sleep(0.5)
        WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.CLASS_NAME, 'c1lbtiq8')))
        time.sleep(0.5)
        close_btn = driver.find_element(By.CLASS_NAME, 'c1lbtiq8')
        close_btn.click()
    except TimeoutException:
        pass

    # cookies warning dismiss
    time.sleep(0.5)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'iv91188')))
    time.sleep(0.5)
    show_tables_btn = driver.find_element(By.CLASS_NAME, 'iv91188')
    show_tables_btn.click()

    print_tables(driver, "0")
    click_next_month(driver)
    print_tables(driver, "1")
    click_next_month(driver)
    print_tables(driver, "2")
    click_next_month(driver)
    print_tables(driver, "3")
    click_next_month(driver)
    print_tables(driver, "4")
    click_next_month(driver)
    print_tables(driver, "5")
    driver.quit()


if __name__ == '__main__':
    chromedriver_autoinstaller.install()
    main()