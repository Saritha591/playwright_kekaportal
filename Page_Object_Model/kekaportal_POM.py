from playwright.sync_api import Page
from data import config


class SearchPage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator(
            '[aria-label="Enter your search term"]')

    def navigate(self):
        self.page.goto("https://msys.keka.com/")

    def search(self):
        self.search_term_input.fill()
        self.search_term_input.fill(password)
        self.search_term_input.press
