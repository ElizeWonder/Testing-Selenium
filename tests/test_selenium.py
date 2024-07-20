import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import FirefoxDriverManager
from selenium.webdriver.firefox.by import By


def test_closing_popup():
    #Firefox_options = Options()
    #Firefox_options.headless = True
    #driver = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install()),options=Firefox_options)
    service = FirefoxService(executable_path"/usr/bin/firefox")
    options = webdriver.Firefox_options()
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://candymapper.com")
    assert "CandyMapper.Com" in driver.title
    PopUpButton = driver.find_element(By.ID, "popup-widget238491")
    CloseButton = driver.find_element(By.ID, "popup-widget238491-close-icon")
    assert PopUpButton.get_attribute("style") == "display: flex;"
    CloseButton.click()
    assert PopUpButton.get_attribute("style") == "display: none;"
    driver.close()

# @pytest.fixture(params=generate_options())
# def driver(request):
#     driver = webdriver.Firefox()
#     driver.get("https://candymapper.com")
#     yield driver
#     # elem = driver.find_element(By.NAME, "q")
#     # elem.clear()
#     # elem.send_keys("pycon")
#     # elem.send_keys(Keys.RETURN)
#     # assert "No results found." not in driver.page_source
#     driver.close()

# def test_Close_Popup(driver)
#     assert "candymapper" in driver.title
#     PopUpButton = driver.find_element_by_ID("popup-widget238491")
#     CloseButton = driver.find_element_by_ID("popup-widget238491-close-icon")
#     CloseButton.click()
#     assert PopUpButton not in driver.page_source


# def generate_options():
#     uwp_options = WindowsOptions()
#     # How to get the app ID for Universal Windows Apps (UWP):
#     # https://www.securitylearningacademy.com/mod/book/view.php?id=13829&chapterid=678
#     uwp_options.app = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
#     uwp_options.platform_name = "WINDOWS"

#     return [uwp_options]


# @pytest.fixture(params=generate_options())
# def driver(request):
#     drv = webdriver.Remote("http://127.0.0.1:4723", options=request.param)
#     yield drv
#     drv.quit()

# def test_Positive():
#     assert 0 == 0
