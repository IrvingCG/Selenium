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
    print("3.-Se han ingresado correctamente las contraseñas")

def navegar_a_administracion():
    administracion = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkMenuItem_383']")))
    administracion.click()
    print("4.-Se a seleccionado correctamente la opcion administracion")

def navegar_a_traspasos():
    traspasos = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkSubmenuItem_280']")))
    traspasos.click()
    print("5.-Se a seleccionado correctamente la opcion administracion")    

def selec_nuevo_registro():
    boton_nuevo_reg =  wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkAddForm']")))
    boton_nuevo_reg.click()
    print("6.-Se a seleccionado correctamente el boton Nuevo Registro de Cuenta")       

def selec_cuenta_tipo():
    selec_cuenta = driver.find_element(By.XPATH,"//*[@id='preregister.product.number']")
    select = Select(selec_cuenta)
    
    selec_tipo = driver.find_element(By.XPATH,"//*[@id='preregister.type.code']")
    select2 = Select(selec_tipo)


    select.select_by_value("00002151952")
    select2.select_by_value("01")
    print("7.-Se a selecciono correctamente la cuenta y el tipo de traspaso")

 
def datos_preregistro(monto,m_dia,m_mes,ope,dinamica): 
    monto_maximo = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='preregister.amountMaximumTrx']")))
    monto_dia =  wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='preregister.amountMaximumTrxDay']")))
    monto_mes = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='preregister.amountMaximumTrxMonth']")))
    ope_dia = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='preregister.quantityTrxDay']")))
    contra_dinamica = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ikey.ikey']")))
    
    monto_maximo.send_keys(monto)
    monto_dia.send_keys(m_dia)
    monto_mes.send_keys(m_mes)
    ope_dia.send_keys(ope)
    contra_dinamica.send_keys(dinamica)
    print("8.-Se ingresaron correctamente los datos para el pre registro")   

def cuenta_d_razon(d_cuenta,r_social):
    cuenta_destino = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='preregister.destinationAccount.accountNumber']")))
    nombre_razon_social = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='preregister.destinationAccount.holderName']")))
   

    cuenta_destino.send_keys(d_cuenta)
    nombre_razon_social.send_keys(r_social)
    print("9.-Se ingresaron correctamente la cuenta y la razon social")    

def selecionar_aceptar():
    boton_aceptar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lnkPreregisterAddCi']")))
    boton_aceptar.click()
    print("11.-Se a seleccionado correctamente el boton aceptar")      

def cerrar_sesion():
    # Cerrar sesión a través de la URL de logout
    driver.get("https://beta.cibanco.com:9403/external-pm-web/authentication/logout.action")
    print("12.-Cierre de sesión exitoso")    

#Ejecutar flujo
ingresar_usuario("CADEGI01")
time.sleep(2)
seleccionar_boton1()
time.sleep(2)
ingresar_contraseñas("tempora1","11111111")
navegar_a_administracion()
navegar_a_traspasos()
time.sleep(5)
selec_nuevo_registro()
time.sleep(5)
selec_cuenta_tipo()
time.sleep(5)
datos_preregistro("20000","30000","40000","9","11111111")
time.sleep(5)
cuenta_d_razon("2151936","jesus")
time.sleep(5)
selecionar_aceptar()
#Cierre de sesion
time.sleep(30)
cerrar_sesion()
# Cerrar navegador después de finalizar la sesión
time.sleep(5)
driver.quit()
print("13.-Se ha cerrado correctamente el navegador")

