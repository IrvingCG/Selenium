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


def seleccionar_administracion_usuarios():
    admin_usuario = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkSubmenuItem_617']")))
    admin_usuario.click()
    print("2.-Opcion Administrador de Usuarios Seleccionado")

def Consultar_Cliente(cliente):
    campo_cliente = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='clientNumber']")))
    boton_enviar_consulta = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='sendId']")))

    campo_cliente.send_keys(cliente)
    boton_enviar_consulta.click()

    print("3.-Se a consultado el cliente")

def cerrar_sesion():
    # Cerrar sesión a través de la URL de logout
    driver.get("http://10.1.2.221:9420/internal-web/authentication/inputInternal.action")
    print("4.-Cierre de sesión exitoso")


# Ejecutar flujo
inciciar_sesion("irving31", "2tempora")
seleccionar_administracion_usuarios()
time.sleep(5)
Consultar_Cliente("1000306192")
# Esperar 1 minuto antes de cerrar sesión
time.sleep(30)
cerrar_sesion()
# Esperar un poco antes de cerrar el navegador
time.sleep(5)
# Cerrar navegador después de finalizar la sesión
driver.quit()
print("5.-Se ha cerrado correctamente el navegador")