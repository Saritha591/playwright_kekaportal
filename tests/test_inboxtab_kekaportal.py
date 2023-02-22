from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
import time
from data import config

username = config.username
password = config.password


def test_home_kekaportal(page):
    page.goto("https://msys.keka.com/")
    page.get_by_role("button", name="keka password").click()
    page.get_by_role("textbox", name="Email").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.locator("//button[normalize-space()='Login']").click()
    page.locator(
        "/html/body/xhr-app-root/div/xhr-home/div/home-dashboard/div/div/div/home-wall-feed/div/home-events/div/ul/div[1]/div/li[1]/a/div/p[2]")
    page.keyboard.press("Enter")
    page.locator(
        "//li[@class='animated-tab mr-20 active z-index-2']//p[@class='ml-4']")
    page.keyboard.press("Enter")
    page.locator("//span[@class='ic-person sidebar-list-icon']").click()
    page.locator("//span[normalize-space()='Attendance']")
    page.mouse.wheel(0, 800)
    page.locator("//span[@class='ic-inbox sidebar-list-icon']").click()
    page.locator("a[routerlink='action']").click()
    page.locator("//span[@class='ic-rupee sidebar-list-icon']")
    page.keyboard.press("Enter")
