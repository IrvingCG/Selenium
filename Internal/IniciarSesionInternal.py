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


def cerrar_sesion():
    # Cerrar sesión a través de la URL de logout
    driver.get("http://10.1.2.221:9420/internal-web/authentication/inputInternal.action")
    print("2.-Cierre de sesión exitoso")


# Ejecutar flujo
inciciar_sesion("irving30", "2tempora")

# Esperar 40 segundos antes de cerrar sesión
time.sleep(40)
cerrar_sesion()

# Esperar un poco antes de cerrar el navegador
time.sleep(5)

# Cerrar navegador después de finalizar la sesión
driver.quit()
print("3.-Se ha cerrado correctamente el navegador")
