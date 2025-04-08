from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el driver
driver = webdriver.Edge()
driver.get("http://10.1.2.221:9420/internal-web/authentication/logout.action")  # Asegúrate de que esta es la URL de inicio de sesión
wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos para cada acción

def ingresar_credenciales(user, password):
    # Ingresar usuario
    campo_usuario = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginInternal_user']")))
    campo_usuario.send_keys(user)
    print("1.-Usuario ingresado correctamente")

    # Ingresar contraseña
    campo_contraseña = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginInternal_password']")))
    campo_contraseña.send_keys(password)
    print("2.-Contraseña ingresada correctamente")

def confirmar_continuar():
    # Hacer clic en botón "Continuar"
    boton_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginInternal_0']")))
    boton_continuar.click()
    print("3.-Botón continuar presionado")

def seleccionar_administracion_contratos():
    admin_contrato = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkSubmenuItem_613']")))
    admin_contrato.click()
    print("4.-Opción 'Administracion de contratos'")    

def boton_nuevo_contrato():
    boton_nuevo_con = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='newContractButton']")))
    boton_nuevo_con.click()
    print("5.-Botón 'Nuevo contrato' presionado")    


def ingresar_cliente(cliente):
    campo_cliente = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contract.client.clientNumber']")))
    campo_cliente.send_keys(cliente)
    print("6.-Cliente ingresado correctamente")  

def boton_validar_cliente():
    boton_validar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkClientValidation']")))
    boton_validar.click()
    print("7.-Botón 'Validar cliente' presionado")    

def seleccionar_todas():
# Seleccionar todos los checkboxes en la tabla de "Servicios Contratados"
    checkboxes = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='selectedServices']")))

    for checkbox in checkboxes:
        if not checkbox.is_selected():  # Solo marcar si no está seleccionado
               checkbox.click()
        print("8.-Se han selecionado todas las casillas")

def boton_crear_contrato():
    boton_crear = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='urlNewContractId']")))
    boton_crear.click()
    print("9.-Botón 'Crear contrato' presionado")  

def cerrar_sesion():
    # Cerrar sesión a través de la URL de logout
    driver.get("http://10.1.2.221:9420/internal-web/authentication/inputInternal.action")
    print("10.-Cierre de sesión exitoso")


#Ejecutar flujo
ingresar_credenciales("irving31","2tempora")
confirmar_continuar()
seleccionar_administracion_contratos()
boton_nuevo_contrato()
time.sleep(5)  # Espera 2 segundos antes de ingresar el client
ingresar_cliente("1000306081")
boton_validar_cliente()
seleccionar_todas()
boton_crear_contrato()

# Esperar 2 minutos antes de cerrar sesión
time.sleep(15)
cerrar_sesion()

# Esperar un poco antes de cerrar el navegador
time.sleep(15)

# Cerrar navegador después de finalizar la sesión
driver.quit()    
print("11.-Se ha cerrado correctamente el navegador")