from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import csv

driver = webdriver.Chrome()


def buscar_item_buscape(url, termo_busca):

    driver.get(url)
    sleep(2)
    produtos_lista = []

    try:
        campo_busca = driver.find_element(
            By.CSS_SELECTOR, '[data-test="input-search"]')
        campo_busca.clear()
        campo_busca.send_keys(termo_busca)
        campo_busca.send_keys(Keys.RETURN)
        sleep(6)

        produtos = driver.find_elements(
            by="xpath", value='//div[@class="Hits_ProductCard__Bonl_"]')

        for produto in produtos:
            try:
                nome = produto.find_element(
                    by='xpath', value='.//h2[@class="Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ"]').text
                preco = produto.find_element(
                    by='xpath', value='.//p[@class="Text_Text__ARJdp Text_MobileHeadingS__HEz7L"]').text
                print("Nome:", nome)
                print("Preço:", preco)
                print("-----")
                produtos_lista.append([nome, preco])
            except Exception as e:
                print("Erro ao coletar informações do produto:", e)

    except Exception as e:
        print("Erro na busca:", e)

    with open("produtosBuscape.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S)")
        writer.writerow(["Data e Hora da Coleta:", data_hora_atual])
        writer.writerow(["Nome", "Preço"])

        writer.writerows(produtos_lista)

    print("Dados salvos em produtosBuscape.csv")


def buscar_tenis(loja_url, termo_busca):
    driver.get(loja_url)
    sleep(2)
    produtos_lista = []
    try:
        campo_busca = driver.find_element(By.ID, "search")
        campo_busca.clear()
        campo_busca.send_keys(termo_busca)
        campo_busca.send_keys(Keys.RETURN)
        sleep(6)

        produtos = driver.find_elements(
            by="xpath",
            value='//div[contains(@class, "card double-columns full-image")]',
        )

        for produto in produtos:
            try:
                nome = produto.find_element(
                    By.CLASS_NAME, "card__description--name"
                ).text
                preco = produto.find_element(
                    by="xpath", value='//span[@data-price="price"]'
                ).text
                print("Nome:", nome)
                print("Preço:", preco)
                print("-----")
                produtos_lista.append([nome, preco])
            except:
                print("Erro ao coletar informações do produto.")

    except Exception as e:
        print("Erro na busca:", e)

    with open("produtos.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S)")
        writer.writerow(["Data e Hora da Coleta:", data_hora_atual])
        writer.writerow(["Nome", "Preço"])
        writer.writerows(produtos_lista)

    print("Dados salvos em produtos.csv")


buscar_tenis("https://www.netshoes.com.br",
             "Tênis Nike Revolution 7 Masculino")
buscar_item_buscape("https://www.buscape.com.br",
                    "Tênis Nike Revolution 7 Masculino")

driver.quit()
