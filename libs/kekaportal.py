from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
import time
from data import config

username = config.username
password = config.password


def kekaportal(page):
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
    time.sleep(3)
    page.locator(
        "//body/xhr-app-root/div[@class='main-container']/xhr-left-nav/nav[@role='navigation']/div[@class='left-nav-body navbar-inner left-nav-fixed-top']/ul[@id='accordion']/li[1]/a[1]").click()
    time.sleep(3)
    page.locator(
        "//li[@class='nav-item active']//a[@class='nav-link']").click()
    page.locator("//span[normalize-space()='Employees']")
    page.keyboard.press("Enter")
    time.sleep(3)
