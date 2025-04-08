from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configurar el driver
driver = webdriver.Edge()
driver.get("http://10.1.2.221:9420/internal-web/authentication/inputInternal.action")  # URL de inicio de sesión
wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos para cada acción
actions = ActionChains(driver)  # Para mover el cursor

def ingresar_credenciales(user, password):
    campo_usuario = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginInternal_user']")))
    campo_usuario.send_keys(user)
    print("1.-Usuario ingresado correctamente")

    campo_contraseña = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginInternal_password']")))
    campo_contraseña.send_keys(password)
    print("2.-Contraseña ingresada correctamente")

    boton_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginInternal_0']")))
    boton_continuar.click()
    print("3.-Botón continuar presionado")

def navegar_a_tokens():
    menu_tokens = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkMenuItem_410']")))
    menu_tokens.click()
    print("4.-Menú 'Tokens' seleccionado")


def seleccionar_sucursal_soft_token():
    sucursal_soft_token = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkSubmenuItem_786'] ")))
    sucursal_soft_token.click()
    print("5.-Opción 'Sucursal Soft Token' seleccionada")

def confirmar():
    boton_confirmar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkTokenTracking']")))
    boton_confirmar.click()
    print("6.-Botón 'Confirmar' presionado")

def seleccionar_softoken_cliente():
    menu_soft_token = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='j_idt31:menuBarAlmacen:softToken']")))
    actions.move_to_element(menu_soft_token).perform()
    print("7.-Hover en 'Soft Token' realizado")
    cliente_nuevo = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='j_idt31:menuBarAlmacen:softToken:clienteNuevo:out']")))
    cliente_nuevo.click()
    print("8.-Opción 'Cliente Nuevo' seleccionada")

def ingresar_numero_cliente(numero_cliente):
    campo_cliente = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='usersCte:numeroCliente'] ")))
    campo_cliente.send_keys(numero_cliente)
    print("9.-Número de cliente ingresado correctamente")

def consultar():
    boton_consultar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='usersCte:_t54']")))
    boton_consultar.click()
    print("10.-Botón 'Consultar' presionado")

def continuar():
    boton_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='usersCte:j_idt89']")))
    boton_continuar.click()
    print("11.-Botón 'Continuar' presionado")

def confirmar_datos():
    boton_confirmar_datos = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='usersCte:clientenuevoconfirmation-accept']")))
    boton_confirmar_datos.click()
    print("12.-se han confirmado los datos")

def confirmar_accion():
    boton_confirmar_accion = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='usersCte:imprimirAcuerdoPanelConfirmation-accept']")))
    boton_confirmar_accion.click()
    print("13.-Botón 'Confirmar Acción' presionado")

def cerrar_sesion():
    driver.get("http://10.1.2.221:9420/internal-web/authentication/inputInternal.action")
    print("14.-Cierre de sesión exitoso")


# Ejecutar flujo
ingresar_credenciales("irving31", "2tempora")
navegar_a_tokens()
seleccionar_sucursal_soft_token()
confirmar()
seleccionar_softoken_cliente()
ingresar_numero_cliente("1000306081")
consultar()
continuar()
confirmar_datos()
confirmar_accion()
# Esperar 2 minutos antes de cerrar sesión
time.sleep(5)
cerrar_sesion()
# Esperar un poco antes de cerrar el navegador
time.sleep(5)
# Cerrar navegador después de finalizar la sesión
driver.quit()
print("15.-Se ha cerrado correctamente el navegador")