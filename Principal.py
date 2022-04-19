# 6 - Usar threadings para executar processos simultaneos

#Reconhecimento de fala
from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError, WaitTimeoutError
import speech_recognition as sr
#sintetizador
import pyttsx3
#busca
import unicodedata
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
# navegador
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# 2 - Sintetizador de voz
def Sintetizador(resposta):
    en = pyttsx3.init()
    en.setProperty('voice', b'brazil')
    en.setProperty('rate', 190)
    en.setProperty('volume', 1)
    en.say(resposta)
    en.runAndWait()

# 1 - Reconhecer voz
def Microfone():
    print('fale')
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        recon.adjust_for_ambient_noise(source, duration=0.02)
        recon.pause_threshold = 1
        audio = recon.listen(source, timeout=7, phrase_time_limit=7)
        # resposta = recon.recognize_google(audio, language='pt')
        # resposta = resposta.replace(" ", "+")
        # resposta = unicodedata.normalize(u'NFKD', resposta).encode('ascii', 'ignore').decode('utf8')
        # print(resposta)
        try:
            resposta = recon.recognize_google(audio, language='pt')
            print(resposta)
            # return resposta
        except WaitTimeoutError:
            print("SEM AUDIO - 1")
            Microfone()
            return "none"
        except Exception as e:
            #print("SEM AUDIO - 2")
            #Microfone()
            return "none"
        return resposta

# 3 - Laço de repetição usando condicional do nome AV
def Menu():
    i = " "
    while i != "sair":
        resposta = Microfone()
        # print("While> {} ".format(resposta))
        if resposta == "Nero":
            #print(">>>")
            resposta = "Póde Falaar!"
            Sintetizador(resposta)
            nome = Microfone()
            (titulos, link) = pesquisar(nome)
            Sintetizador("{} ".format(titulos[0]))
            AbrirSite(link[0])
        
        elif resposta=="Fechar programa":
            Sintetizador("Fechando")
            #browser.minimize_window()
            #browser.close()
            #FecharSite()
            break
        i = resposta

# 4 -Função de busca
def pesquisar(resposta):
    # resposta = "globo"
    resposta = resposta.replace(" ", "+")
    resposta = unicodedata.normalize(u'NFKD', resposta).encode('ascii', 'ignore').decode('utf8')
    link = "https://www.google.com.br/search?sxsrf=ALeKk00MQi6RiTA_3lCh1yIqkmO4UEah2Q%3A1601946620374&source=" \
           "hp&ei=_MN7X-6aFPDE5OUPo4q70Ag&iflsig=AINFCbYAAAAAX3vSDCLAt2Gm_E4y-26HRoXARJo1knoF&q=" \
           "{}&btnK=Pesquisa+Google&oq=3BD+%2B+4+DB&gs_lcp=CgZwc3ktYWIQAzoKCC4Q6gIQJxCTAjoHCCMQ6gIQJzoCCAA6BQg" \
           "AELEDOgUILhCxAzoICAAQsQMQgwE6AgguOgQIABAKOgQILhAKOgQIABAeOgYIABAKEBM6CAgAEAoQHhATOgYIABAeEBM6CAgAE" \
           "AUQHhATOgQIABATOgYIABAWEB46CAgAEBYQChAeUMcXWJ5CYM9JaANwAHgAgAH-AogBxRmSAQUyLTYuNZgBAKABAaoBB2d3cy1" \
           "3aXqwAQo&sclient=psy-ab&ved=0ahUKEwjuiISa5J7sAhVwIrkGHSPFDooQ4dUDCAY&uact=" \
           "5#btnK=Pesquisa%20Google".format(resposta)
    print(link)
    req = Request(link, headers={
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/81.0.4044.138 Safari/537.36'})
    # print(req)
    webpage = urlopen(req).read()
    site = []
    titulos = []
    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html.parser')
        # print(soup)
        for item in soup.find_all('div', attrs={'class': 'tF2Cxc'}):  # dbsr
            raw_link = (item.find('a', href=True)['href'])
            site.append(raw_link)
        for item in soup.find_all('div', attrs={'class': 'tF2Cxc'}):  # dbsr tF2Cxc
            titulo = (item.find('span'))
            titulos.append(titulo)

    print("\n{}".format(titulos))
    print("\n{}".format(site))
    return titulos, site

# 5 - Definir navegador
def AbrirSite(link):
    try:
        print(link)
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.maximize_window()
        # wait = WebDriverWait(browser, 3)
        browser.get(link)

        # presence = EC.presence_of_element_located
        # visible = EC.visibility_of_element_located
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, '//button[@aria-label="Reproduzir (k)"]').click()
        browser.find_element(By.XPATH, '//button[@aria-label="Tela inteira (f)"]').click()

        # wait.until(visible((By.ID, "video-title")))
        # browser.find_element_by_id("video-title").click()
        # time.sleep(5)
        # driver.implicitly_wait(5)
        # driver.switch_to.frame(0)
        # element = driver.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
        # element.click()
        # wait.until(visible((By.ID, "jw-icon jw-icon-display jw-button-color jw-reset")))
        # browser.find_element_by_id("Reproduzir").click()
        # principal()
    except Exception as e:
        print("deu erro")
        return "none"

def FecharSite():
    browser.quit()

if __name__ == "__main__":
    Menu()