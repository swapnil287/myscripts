# import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_result():
    # access chromedriver
    service_obj = Service("D:/Swapnil/40Bears/Automation/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)

    # hit amazon site
    driver.get("https://www.amazon.in/")

    # maximize the window
    driver.maximize_window()

    # access element by using find element method with xpath
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/input[1]").send_keys(
        "chair")
    driver.find_element(By.XPATH,
                        "/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/span[1]/input[1]").click()

    # store the fetch result in result_title variable
    result_title = driver.find_element(By.XPATH,
                                       "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]/span[2]").text

    # print the result
    print("\nFirst result title is: "+result_title)
