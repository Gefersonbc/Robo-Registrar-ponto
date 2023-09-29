import pyautogui
import time

# Abrir o Navegador e acessar o site
pyautogui.PAUSE = 1

# abir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("Enter")

#acessar o sistema de ponto
forponto = "https://forponto.quality.com.br/ForpontoWeb/Login.aspx?ReturnUrl=%2fForpontoWeb%2fFormularios%2fPainelAdministracao2.aspx"
pyautogui.write(forponto)
pyautogui.press("Enter")

# tempo para esperar a pagina carregar
time.sleep(5)

# fazer login no sistema

#localização do click do mouse para mudar o campo de Gestor para Funcionario.
pyautogui.click(x=760, y=223)
pyautogui.press("up")
pyautogui.press("tab")
pyautogui.press("tab")

#Digitar o login e senha
pyautogui.write("geferson.cruz")
pyautogui.press("tab")
pyautogui.write("$lV_jVH%_8/#udC")
pyautogui.press("tab") 
pyautogui.press("Enter")

#tempo para carregar o login
time.sleep(5)

#Registrar a batida do ponto
pyautogui.click(x=31, y=126)
pyautogui.click(x=95, y=249)       
pyautogui.click(x=486, y=677)
time.sleep(5)
pyautogui.press("Enter")