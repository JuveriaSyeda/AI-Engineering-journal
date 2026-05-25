# Beautiful Soup
# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/")
# scrapper = BeautifulSoup(response.text,"html.parser")
# titles = scrapper.select(".title")
# for title in titles:
#     print(title.get_text())
#creating all the readMe paragraphs
# readmeCreation = scrapper.select("#creating-a-readme-file p")
# # print(readmeCreation)
# for readMe in readmeCreation:
#     readMeText = readMe.get_text()
#     print(readMeText)
#Selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://selenium.dev/documentation")
# assert "Selenium" in driver.title

# elem = driver.find_element(By.ID, "m-documentationwebdriver")
# elem.click()
# historyTab.screenshot_as_png
# driver.quit()