from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import csv
from time import sleep
import datetime
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException, WebDriverException
import os
import json
import requests

def save_to(data, name="data_wb_art_info", rows=True, type="csv"):
    dir = "data/"
    dir_name = os.path.dirname(dir)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    if type == "csv":
        filename = "{}_{}.csv".format(name, datetime.datetime.today().strftime("%d_%m_%Y_%H_%M"))
        name = dir + filename
        with open(name, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if rows == True:
                for bach in data:
                    writer.writerow(bach)
            else:
                writer.writerow(data)
    elif type == 'json':
        filename = "{}_{}.json".format(name, datetime.datetime.today().strftime("%d_%m_%Y_%H_%M"))
        name = dir + filename
        with open(name, 'w') as file:
            json.dump(data, file)
            ### Не забудь прописать ошибку по type


def get_sub_cat_urls(save=True):
    cat_urls = {}
    driver = webdriver.Firefox()
    driver.get("about:preferences")
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//*[@id='defaultZoom']"))
    ActionChains(driver).click(driver.find_element(By.XPATH, "//*[@value='50']")).perform()
    url = 'https://www.wildberries.ru/'
    driver.get(url)
    driver.implicitly_wait(9)
    sleep(0.5033)
    driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[1]/button').click() # кнопка меню
    subs = driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[2]/ul/li')[4:]
    subs.pop(-16)
    subs.pop(-3)
    driver.implicitly_wait(7)

    for cat in subs:
        driver.implicitly_wait(5)
        sleep(0.9)
        ActionChains(driver).move_to_element(cat).perform()
        sub_urls = cat.find_elements(By.XPATH, '//div/ul/li/a')
        sleep(0.7)
        try:
            for el in sub_urls:
                cat_urls[str(el.get_attribute('href').split('/')[-1]) + "__" + str(el.get_attribute('href').split('/')[-2])] = el.get_attribute('href')

            driver.implicitly_wait(5)
        except (StaleElementReferenceException, IndexError):
            pass

        sub_subs = cat.find_elements(By.XPATH, r'/html/body/div[1]/div[3]/div[3]/div/div/div/div[1]/ul/li/span')
        sub_subs = [el for el in sub_subs if len(el.text)>2]
        for i in range(len(sub_subs)):
            sub_subs_2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div/div/div[1]/ul/li/span')
            sub_subs_2 = [el for el in sub_subs_2 if len(el.text)>2]
            driver.implicitly_wait(5)
            try:
                sub_subs_2[i].click() #ActionChains(driver).move_to_element(sub_subs_2[i]).click().perform()
                backs = driver.find_elements(By.XPATH,' //div[1]/div[3]/div[3]/div/div/div/div[2]/div/button')
                back = [el for el in backs if len(el.text)>2]
                sub_subs_3 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div[17]/div/div[2]/ul/li/a')
                for el in sub_subs_3:
                    cat_urls[str(el.get_attribute('href').split('/')[-1]) +"__"+ str(el.get_attribute('href').split('/')[-2])] = el.get_attribute('href')
                back[0].click()
            except (ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException, IndexError):
                pass

    if save == True:
        save_to(cat_urls, name="sub_cat_urls", rows=False, type='json')
    driver.close()
    return cat_urls

def numbers(string):
    string = ''.join(el for el in string if el.isdigit())
    return string


def cat_collector(categorials_url: dict, save=True):
    cat_dump = []
    cat_dump_urls = []
    """По собраным суб категориям определяет размер ниши и записывает так же первые товары из поиска """
    for k, v in categorials_url.items():
        cat_info = []
        cat_urls = []
        driver = webdriver.Firefox()
        driver.get("about:preferences")
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//*[@id='defaultZoom']"))
        ActionChains(driver).click(driver.find_element(By.XPATH, "//*[@value='50']")).perform()
        driver.implicitly_wait(9)
        try:
            response = requests.get(v)
            if response.ok:
                driver.get(v)
                driver.implicitly_wait(9)
                sleep(5.1)
                number_of_products = driver.find_elements(By.XPATH, "//div/div[1]/div/span/span[1]")
                number_of_products = [el.text for el in number_of_products if len(el.text)>2]
                number_of_products = [numbers(el)for el in number_of_products]
                urls_art = [el.get_attribute('href') for el in driver.find_elements(By.XPATH, "//div/article/div/a")]
                art_rate = [el.text for el in driver.find_elements(By.XPATH, "//article/div/div/p[1]/span[2]")]
                art_rate = [numbers(el) for el in art_rate]
                cat_info.append(v)
                cat_info.append(k)
                cat_info.append(number_of_products)
                for el in urls_art:
                    cat_urls.append(el)
                for el in art_rate:
                    cat_info.append(el)
                cat_dump.append(cat_info)
                cat_dump_urls.append(cat_urls)
        except (WebDriverException, NoSuchElementException):
            pass
        driver.close()
    if save == True:
        save_to(cat_dump, name="cat_dump", type="csv", rows=True)
        save_to(cat_dump_urls, name="cat_dump_urls", type="csv", rows=True)
    return cat_dump



