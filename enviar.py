from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyautogui
import time
import os

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


navegador.get("https://web.whatsapp.com")
time.sleep(5)

while True:
    try:
        navegador.find_element('xpath', '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas')
    except:
        print("conectado")
        time.sleep(10)
        break
os.system("cls")
cont = 0
with open("ctt.txt") as contatos:
    for contato in contatos:
        cont += 1
        print(f"{cont} - Enviando para > ",contato.replace("\n",""))
        navegador.get(f"https://web.whatsapp.com/send/?phone=55{contato}&text=%2AXer%C3%A9m+Online+INFORMA%2A%0AGrande+novidade%21+Agora+tamb%C3%A9m+temos+servi%C3%A7o+de+televis%C3%A3o%21%0ADesfrute+de+mais+op%C3%A7%C3%B5es+de+entretenimento+com+nossa+nova+oferta.%0AConfira+e+aproveite%21%0A%2A%3E%3E+Caso+seja+do+seu+interesse%2C+responda+essa+menssagem+com%C2%A0%3E%C2%A0Eu%C2%A0quero%21%2A")
        time.sleep(5)
        try:
            navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div').click()
        except:
            with open("log\env_nao.txt", "a") as enviados:
                enviados.write(f"{contato}")
                enviados.close()
            continue
        pyautogui.press("enter")
        time.sleep(2)
        with open("log\enviados.txt", "a") as enviados:
            enviados.write(f"{contato}")
            enviados.close()
    contatos.close()
print("Finalizado!")
