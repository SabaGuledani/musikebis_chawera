import time
import os
import requests
import re
import pyautogui
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

folder_path = r'C:\Users\student\PycharmProjects\scrap\downloaded_files'
TEXT_FILE_PATH = 'file.txt'


wd = webdriver.Chrome()
wd.implicitly_wait(4)

file1 = open(TEXT_FILE_PATH, 'r')
lines = file1.readlines()

downloader_link = 'https://ytmp3.nu/gEIs/'
iteration = 0

for link in lines:
    if iteration == 0:
        wd.execute_script("window.open('about:blank', '_blank');")
        iteration += 1
    wd.switch_to.window(wd.window_handles[1])
    wd.get(downloader_link)
    time.sleep(5)
    input_path = '//*[@id="url"]'
    convert_btn_path= '/html/body/form/div[2]/input[2]'
    download_btn_path = "/html/body/form/div[2]/a[1]"

    input_field = wd.find_element(By.XPATH, input_path)
    input_field.click()
    input_field.clear()
    input_field.send_keys(link)
    pyautogui.press('enter')


    # convert_btn = wd.find_element(By.XPATH, convert_btn_path)
    # convert_btn.click()

    elem = WebDriverWait(wd, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > form > div:nth-child(3)'))

    )
    time.sleep(2)
    download_btn = wd.find_element(By.XPATH, download_btn_path)
    download_btn.click()

    time.sleep(5)
    pyautogui.press('enter')










