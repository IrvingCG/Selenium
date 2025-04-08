from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el driver
driver = webdriver.Edge()
driver.get("https://beta.cibanco.com:9403/external-pf-web/authentication/close.action")
wait = WebDriverWait(driver, 30)  # Espera hasta 30 segundos

def ingresar_usuario(usuario):
    campo_usuario = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='user']")))
    campo_usuario.send_keys(usuario)
    print("1.-Se ingreso correctemente el usuario")  

    boton_aceptar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sbmKeySecretForm']")))
    boton_aceptar.click()
    print("2.-Boton continuar precionado")  

def registro_clave_secreta(usuario,clave,clave2):
    campo_usuario = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='user']")))
    print("3.-Se capturo correctamente al usuario") 
    campo_clave = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='newKeySecret']")))
    print("4.-Se capturo correctemente la clave secreta")
    campo_clave2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='repeatNewKeySecret']")))
    print("5.-Se capturo y se confirmo correctemente la clave secreta")

    campo_usuario.send_keys(usuario)
    campo_clave.send_keys(clave)
    campo_clave2.send_keys(clave2)
    
    boton_registrar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='registerKeySecretPortal']")))
    boton_registrar.click()
    print("6.-Boton registrar precionado")

def capturar_contraseñas(password, dinamica):
    campo_password = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginRequestDTO.password']")))
    print("7.-Se ingreso correctemente la contraseña")  
    campo_con_dinamica = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginRequestDTO.token']")))
    print("8.-Se ingreso correctemente la contraseña dinamica")  
    
    campo_password.send_keys(password)
    campo_con_dinamica.send_keys(dinamica)
    
    boton_aceptar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginExternal_0']")))
    boton_aceptar.click()
    print("9.-Boton Ingresar precionado") 


def cerrar_sesion():
    boton_cerrar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='']")))
    boton_cerrar.click()
    print("10.-Cierre de sesión exitoso")


#Ejecutar flujo
ingresar_usuario("GABY6605")
time.sleep(5)
registro_clave_secreta("GABY6605","irving","irving")
capturar_contraseñas("tempora1","11111111")
# Esperar 30 segundos antes de cerrar sesión
time.sleep(15)
# Cerrar sesión
cerrar_sesion()
# Cerrar navegador después de finalizar la sesión
driver.quit()
print("11.-Se ha cerrado correctamente el navegador")










