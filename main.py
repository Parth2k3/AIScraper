from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

#importing all the selenium libraries.

URL = "https://deepai.org/chat"
#setting URL variable (using deepai website scraping)


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


#defining a function to create a ChromeDriver here.


def getAnswer(driver, query):

  wait = WebDriverWait(driver, 10)
  CHATBOX_CLASS = 'chatbox'
  chatbox = driver.find_elements(By.CLASS_NAME, CHATBOX_CLASS)
  #finding the input box textarea

  SUBMIT_BUTTON_ID = 'chatSubmitButton'
  submitButton = wait.until(
    EC.presence_of_element_located((By.ID, SUBMIT_BUTTON_ID)))
  #finding the submit button

  chatbox[-1].send_keys(query)
  #sending the user input to the last chatbox
  #(since the active chatbox is the last one)

  submitButton.click()
  #clicking the submit button

  OUTPUT_CSS_SELECTOR = 'div.outputBox'
  outputBoxes = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, OUTPUT_CSS_SELECTOR)))
  #finding the output box

  Answer = outputBoxes.text
  #retreiving the output content

  Answer = Answer[:-22]
  #slicing the result string to remove unwanted peice of information

  return Answer


if __name__ == "__main__":
  driver = get_driver()
  driver.get(URL)
  #defining the driver and setting URL

  while True:
    #setting an infinite loop to constantly ask for user queries/messages

    message = input("Enter your message: ")
    print('AI:', getAnswer(driver, message))
    #printing the retrieved answer

    time.sleep(4)
    deleteButtonClass = 'deleteBoxButton'
    dltBtn = driver.find_elements(By.CLASS_NAME, deleteButtonClass)
    dltBtn[1].click()
    dltBtn[0].click()
    #deleting the already created query and response to reset the divs

    if (input("Do you want to ask more?(Y/N): ")) == 'Y' or 'y':
      continue
    else:
      driver.quit()
      sys.exit()
