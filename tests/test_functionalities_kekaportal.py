from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
import time
from data import config

username = config.username
password = config.password


def test_functionality_kekaportal(page):
    page.goto("https://msys.keka.com/")
    page.get_by_role("button", name="keka password").click()
    page.get_by_role("textbox", name="Email").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.locator("//button[normalize-space()='Login']").click()
    page.locator("//span[@class='ic-home sidebar-list-icon']").click()
    page.locator(
        "//li[@class='animated-tab mr-20 active z-index-2']//p[@class='ml-4']").click()
    time.sleep(3)
