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
    print("2.-Boton continuar presionado")  

def confirmar_continuar():
    boton_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sbmExternalAuthentication']")))
    boton_continuar.click()
    print("3.-Boton continuar presionado")  

def ingresar_credenciales(password, otp):
    campo_password = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginRequestDTO.password']")))
    print("4.-Se ingreso correctemente la contraseña")  
    campo_otp = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginRequestDTO.token']")))
    print("5.-Se ingreso correctemente la contraseña dinamica")  
    
    campo_password.send_keys(password)
    campo_otp.send_keys(otp)
    
    boton_aceptar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sbmExternalAuthentication']")))
    boton_aceptar.click()
    print("6.-Boton continuar presionado")  

def cerrar_sesion():
    boton_cerrar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='']")))
    boton_cerrar.click()
    print("7.-Cierre de sesion exitoso")
# Ejecutar flujo
ingresar_usuario("AATA6410")
confirmar_continuar()
ingresar_credenciales("tempora1", "11111111")

# Esperar 30 segundos antes de cerrar sesión
time.sleep(30)

# Cerrar sesión
cerrar_sesion()


# Cerrar navegador después de finalizar la sesión
driver.quit()
print("8.-Se ha cerrado correctamente el navegador")