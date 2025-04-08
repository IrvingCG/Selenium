from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el driver
driver = webdriver.Edge()
driver.get("http://10.1.2.221:9420/internal-web/authentication/logout.action")  # Asegúrate de que esta es la URL de inicio de sesión
wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos para cada acción

def inciciar_sesion(user, password):
    campo_usuario = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginInternal_user']")))
    campo_contraseña = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginInternal_password']")))
    boton_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginInternal_0']")))

    campo_usuario.send_keys(user)
    campo_contraseña.send_keys(password)
    boton_continuar.click()
    print("1.-Sesion iniciada correctamente")


def seleccionar_deslogeo():
    deslog_usuario = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkSubmenuItem_619']")))
    deslog_usuario.click()
    print("2.-Opcion Deslogeo / Usuario Cliente Seleccionado")

def buscar_usuario(usuario):
    campo_usuario = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='userExternal.loginName']")))
    boton_buscar = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='findUserLoggedId']")))

    campo_usuario.send_keys(usuario)
    boton_buscar.click()
    print("3.-Se a buscado el cliente correctamente")

def deslogear_usuario():
    boton_cerrar = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='endSessionId']")))
    boton_cerrar.click()
    print("4.-Se a deslogeado al usuario con la sesion atrapada") 

def aceptar_cerrar():
    boton_aceptar_cerrar = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='acceptLogoutId']")))
    boton_aceptar_cerrar.click()
    print("5.-Se a aceptado cerrar la sesion correctamente") 



def cerrar_sesion():
    driver.get("http://10.1.2.221:9420/internal-web/authentication/inputInternal.action")
    print("6.-Cierre de sesión exitoso")

# Ejecutar flujo
inciciar_sesion("irving31", "2tempora")
seleccionar_deslogeo()
time.sleep(5)
buscar_usuario("CADEGI01")
time.sleep(5)
deslogear_usuario()
time.sleep(5)
aceptar_cerrar()
# Esperar 1 minuto antes de cerrar sesión
time.sleep(30)
cerrar_sesion()
# Esperar un poco antes de cerrar el navegador
time.sleep(5)
# Cerrar navegador después de finalizar la sesión
driver.quit()
print("7.-Se ha cerrado correctamente el navegador")
