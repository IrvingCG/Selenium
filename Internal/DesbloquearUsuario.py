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

def seleccionar_admin_usuarios():
    admin_usuarios = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkSubmenuItem_617']")))
    admin_usuarios.click()
    print("2.-Opcion Administracion de Usuarios Seleccionado")    

def ingresar_usuario(usuario):
    campo_usuario_cinet = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginName']")))
    boton_enviar_consulta = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sendId']"))) 

    campo_usuario_cinet.send_keys(usuario)
    boton_enviar_consulta.click()
    print("3.-Usuario ingresado correctamente y boton enviar consulta selccionado")  

def seleccionar_desbloquear():
     boton_desbloquear= wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='image_BO']"))) 
     #//*[@id='image_BT'] Bloqueo por intentos
     #//*[@id="image_BO"] Bloqueo por solicitud
     #//*[@id="image_BP"] Bloqueo preventivo
     boton_desbloquear.click()
     print("4.-Boton Desbloquear Seleccionado")  


def seleccionar_aceptar():
     boton_aceptar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sendConfirmAction']"))) 
     boton_aceptar.click()
     print("5.-Boton Aceptar Seleccionado")       


def cerrar_sesion():
    # Cerrar sesión a través de la URL de logout
    driver.get("http://10.1.2.221:9420/internal-web/authentication/inputInternal.action")
    print("6.-Cierre de sesión exitoso")

# Ejecutar flujo
inciciar_sesion("irving32","2tempora") 
seleccionar_admin_usuarios()
time.sleep(5)
ingresar_usuario("GUCN7013")
time.sleep(5)
seleccionar_desbloquear()
time.sleep(5)
seleccionar_aceptar()
# Esperar 30 segundos antes de cerrar sesión
time.sleep(10)
cerrar_sesion()
# Esperar un poco antes de cerrar el navegador
time.sleep(5)
# Cerrar navegador después de finalizar la sesión
driver.quit()
print("7.-Se ha cerrado correctamente el navegador")
