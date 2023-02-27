from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

liste=["itfaiye","eklemli","makaslı","teleskobik","platform","hidrolik","yürüyüşlü","araç üstü","arazöz","arasöz"]
                          ########## FIXED CODE ##########\n"
driver = webdriver.Chrome()
driver.get("https://ekap.kik.gov.tr/EKAP/Ortak/IhaleArama/index.html") 
    # OKAY
driver.maximize_window()
    # LİSTEYİ ACMAYA TIKLIYOR
roledropdown = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div/div[4]/div[1]/select").click()
    # 2023'ü seçiyor.
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div/div[4]/div[1]/select/option[2]").click()
                                  ########## FIXED CODE ##########
    
for i in liste:
    # yazıyı gönderiyor.\n"
    driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[4]/div[2]/input").send_keys(i)
    # Arama tuşuna basıyor.\n",
    
    driver.find_element(By.XPATH, "//*[@id='pnlFiltreBtn']/button").click()
    
    # sonuç yok yazısı
    #x=driver.find_element(By.CLASS_NAME, "'col-sm-12\'")
    #y=driver.find_element(By.XPATH,"//*[@id='sonuclar']/div[1]/div/div/div/div[2]/div/div/p[1]/text()")
    #print(y.text)
    time.sleep(3)
    #Yeni arama için çarpıya basıyor.
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div/div[4]/div[2]/span").click()
    
    #print(x.text)
   
