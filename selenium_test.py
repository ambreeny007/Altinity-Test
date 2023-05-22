import time

from testflows.core import *
from selenium import webdriver
from selenium.webdriver.common.by import By


with Scenario('Test - Verify User is able to navigate to blogs page'):
    browser = webdriver.Firefox()
    with Given("I got connected to DB"):
        browser.get('https://altinity.com/')
        time.sleep(3)
    with When("I click on blog menu"):
        element = browser.find_element(By.XPATH,"(//a[@href='/blog'])[1]")
        element.click()
        time.sleep(3)
    with Then("I see Altinity Blogs Page"):
        assert "Altinity Blog" in browser.title

    browser.quit()
