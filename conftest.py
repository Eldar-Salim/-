import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_name = request.param
    
    if browser_name == "Chrome":
        browser = webdriver.Chrome()
    elif browser_name == "Firefox":
        browser = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser specified in the test parameters.")
    browser.implicitly_wait(10)
    yield browser
    
    print("\nQuit browser..")
    browser.quit()



    """
    print("\nstart browser for test..")
    browser = 
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
    """
