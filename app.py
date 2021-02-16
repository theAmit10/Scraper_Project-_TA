from selenium import webdriver  # it is used to scrap javaScript
from selenium.common.exceptions import NoSuchElementException

from scraper_project.pages.quote_page import QuotesPages


class InvalidTagForAuthorError():
    pass


try:
    chrome = webdriver.Chrome(executable_path="D:/chromedriver.exe")
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPages(chrome)
    
    author = input("Enter the author you would like to see quotes from:  ")
    page.select_author(author_name=author)
    
    
    tags = page.get_available_tags()
    print("Select one of these tags: [{}] ".format(" | ".join(tags)))
    selected_tag = input("Enter The Tag name: ")
    
    page.select_tag(tag_name=selected_tag)
    
    page.search_button.click()
    
    print(page.quotes)
except NoSuchElementException as e:
    print("No result found")




