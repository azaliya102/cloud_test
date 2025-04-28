from selenium.webdriver.common.by import By
from example_page import TITLE

def test_title(driver):
    driver.get("https://example.com")
    assert TITLE in driver.title

def test_more_info_link(driver):
    driver.get("https://example.com")
    more_info_button = driver.find_element(By.LINK_TEXT, "More information...")
    more_info_button.click()
    expected_url = "https://www.iana.org/help/example-domains"
    assert driver.current_url == expected_url