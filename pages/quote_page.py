from typing import List
from selenium.webdriver.support.ui import Select

from scraper_project.locator.quotes_page_locator import QuotesPageLocator
from scraper_project.parser.quote import QuoteParser

"""
 In Beautiful soup everything thing that comes inside the Tags.
"""

class QuotesPages:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self)  -> List[QuoteParser] :
        return [QuoteParser(e)
                for e in self.browser.find_elements_by_css_selector(
                    QuotesPageLocator.QUOTE
            )
        ]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocator.AUTHOR_DROPDOWN
        )
        return Select(element)  # Select is a wrapper

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocator.TAG_DROPDOWN
        )
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(
            QuotesPageLocator.SEARCH_BUTTON
        )

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tag_dropdown.options]

    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)
