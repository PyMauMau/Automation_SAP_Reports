from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from rulesReports import ChoiceRules
#from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup
#from selenium.webdriver.chrome.service import Service

class TakeReportFromSap():
    def __init__(self):
        pass
    
    @staticmethod
    def _whichType(Type:int):
        try:
            if Type == 0:
                return "Indirect"
            elif Type == 1:
                return "Direct"
            else:
                raise KeyError            
        except KeyError:
            return "Código invalido para operação."

    @staticmethod
    def _takeInstructions(type:str, method:object):
        try:
            if type:
                instructions = method.applyRule(type)
                return instructions
            else:
                raise KeyError
        except KeyError:
            "Has some problem with Dict keys on ChoiceRules Method."

    def goToSap(self, site_inicial:str, site_target:str, type:int):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless
        chrome_options.add_argument("--disable-gpu")  # Necessário para o Windows
        browser = webdriver.Chrome()
        browser.get(site_inicial)
        sleep(1)
        browser.find_element(By.XPATH,'//*[@id="i0116"]').click()
        browser.find_element(By.XPATH,'//*[@id="i0116"]').send_keys('user_SAP')
        browser.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
        sleep(2)
        browser.find_element(By.XPATH,'//*[@id="i0118"]').click()
        browser.find_element(By.XPATH,'//*[@id="i0118"]').send_keys('password_SAP')
        browser.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
        sleep(2)
        browser.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
        sleep(2)
        browser.get(site_target)
        sleep(2)
        typeReport = str(self._whichType(type))
        chosenRule = ChoiceRules()
        isntructions = self._takeInstructions(typeReport, chosenRule)
        print(isntructions)