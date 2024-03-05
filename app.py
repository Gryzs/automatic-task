import pyautogui
import pandas
import time
# TABULA LÊ PDF

url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(url)
pyautogui.press('enter')

time.sleep(1.5)

pyautogui.click(x=866, y=372, clicks=1)
pyautogui.write('aulapy@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha123py')
pyautogui.press('enter')

time.sleep(1.5)

tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:

    pyautogui.click(x=714, y=257)

    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)
