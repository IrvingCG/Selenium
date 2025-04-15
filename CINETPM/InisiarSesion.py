from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el driver
driver = webdriver.Edge()
driver.get("https://beta.cibanco.com:9403/external-pm-web/authentication/close.action")  # Asegúrate de que esta es la URL de inicio de sesión
wait = WebDriverWait(driver, 30)  # Espera hasta 10 segundos para cada acción

def ingresar_usuario(user):
    campo_usuario = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='user']")))
    boton_ingresar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sbmKeySecretForm']")))

    campo_usuario.send_keys(user)
    boton_ingresar.click()
    print("1.-Sesion iniciada correctamente")

def seleccionar_boton1():
    boton_aceptar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sbmExternalAuthentication']")))
    boton_aceptar.click()
    print("2.-Se a seleccionado correctamente el boton aceptar")

def ingresar_contraseñas(contra,dinamica):
    campo_contraseña = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginRequestDTO.password']")))
    campo_dinamica = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginRequestDTO.token']")))
    boton_ingresar2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sbmExternalAuthentication']")))    
    
    campo_contraseña.send_keys(contra)
    campo_dinamica.send_keys(dinamica)
    boton_ingresar2.click()
    print("3.-Se ha ingresado correctamente la contaseña y la contraseña dinamica")

def cerrar_sesion():
    # Cerrar sesión a través de la URL de logout
    driver.get("https://beta.cibanco.com:9403/external-pm-web/authentication/logout.action")
    print("12.-Cierre de sesión exitoso")   


#Ejecutar flujo
time.sleep(2)
ingresar_usuario("CADEGI01")
time.sleep(2)
seleccionar_boton1()
time.sleep(2)
ingresar_contraseñas("tempora1","11111111")
#Cierre de sesion
time.sleep(30)
cerrar_sesion()
# Cerrar navegador después de finalizar la sesión
time.sleep(15)
driver.quit()
print("4.-Se ha cerrado correctamente el navegador")