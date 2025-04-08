from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Configurar el driver
driver = webdriver.Edge()
driver.get("http://beta.cibanco.com:9492/AfiliacionCINet/")  # URL de inicio de sesión
wait = WebDriverWait(driver, 30)  # Espera hasta 30 segundos para cada acción



def ingresar_codigo_registro(codigo_registro):
    campo_cod_reg = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='folio']")))
    campo_cod_reg.send_keys(codigo_registro)
    print("1.-Codigo de registro ingresado correctamente")

def continuar1():
    boton_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_t75']")))
    boton_continuar.click()
    print("2.-Botón 'Continuar' presionado")

def ingresar_cliente(cliente):
    campo_cliente = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='numCliente']")))
    campo_cliente.send_keys(cliente)
    print("3.-Codigo de registro ingresado correctamente")   

def continuar2():
    boton_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_t75']")))
    boton_continuar.click()
    print("4.-Botón 'Continuar' presionado")

def ingresar_rfc(rfc):
    campo_rfc = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='rfc']")))
    campo_rfc.send_keys(rfc)
    print("5.-Codigo de registro ingresado correctamente")  

def continuar3():
    boton_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_t75']")))
    boton_continuar.click()
    print("6.-Botón 'Continuar' presionado")

def confirmar_datos():
    boton_confirmar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_t70']")))
    boton_confirmar.click()
    print("7.-Botón 'Continuar' presionado")

def ingresar_usuario(usuario):
    campo_usuario = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='usuario']")))
    campo_usuario.send_keys(usuario)
    print("11.-Usuario ingresado correctamente") 

def boton_siguiente():
    boton_confirmar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_t83']")))
    boton_confirmar.click()
    print("12.-Botón 'Continuar' presionado")

def ingresar_contraseñas(contraseña, confcontra):
    campo_contraseña = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='contrasenia']")))
    campo_contraseña.send_keys(contraseña)
    print("13.-Contraseña ingresada correctamente")

    campo_confcontra = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='confContrasenia']")))
    campo_confcontra.send_keys(confcontra)
    print("15.-Contraseña ingresada correctamente")

def boton_siguiente2():
    boton_confirmar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_t117']")))
    boton_confirmar.click()
    print("16.-Botón 'Continuar' presionado")

def ingresar_nip(nip, confnip):
    campo_nip = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='nip']")))
    campo_nip.send_keys(nip)
    print("17.-nip ingresada correctamente")

    campo_confnip = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='confNip']")))
    campo_confnip.send_keys(confnip)
    print("18.-nip ingresada correctamente")

def boton_siguiente3():
    boton_confirmar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_t71']")))
    boton_confirmar.click()
    print("19.-Botón 'Continuar' presionado")

def boton_finalizar():
    boton_finalizar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='j_idt54']")))
    boton_finalizar.click()
    print("20.-Botón 'Finalizar' presionado")

#Ejecutar flujo
ingresar_codigo_registro("CIBSTK2025000013300402")
continuar1()
ingresar_cliente("1000306081")
continuar2()
ingresar_rfc("EANE740826G96")
continuar3()
confirmar_datos()
ingresar_usuario("EANE740826G96")
boton_siguiente()
ingresar_contraseñas("tempora1","tempora1")
boton_siguiente2()
ingresar_nip("1234","1234")
boton_siguiente3()
boton_finalizar()

# Esperar un poco antes de cerrar el navegador
time.sleep(30)

# Cerrar navegador después de finalizar la sesión
driver.quit()    
print("21.-Se ha cerrado correctamente el navegador")
