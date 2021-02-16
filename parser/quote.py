from scraper_project.locator.quote_locator import QuoteLocator


class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about the
    quote (quote content, author and tags.)

    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self): # it is used to represent or what will it return buddy
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocator.CONTENT
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def author(self):
        locator = QuoteLocator.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tags(self):
        locator = QuoteLocator.TAGS
        return [e.string for e in self.parent.find_elements_by_css_selector(locator)]

