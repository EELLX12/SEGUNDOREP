import streamlit as st

#Ejercicio 4:  calcular la suma  de n numeros elevados a la n
st.title("SESION 12 Estructura repetitiva")
st.subheader("Ejercicio 4 : suma  de n numeros elevados a la n")
#Función para generar serie
def generar_serie(n):
    serie = []
    for i in range(n):
        a=i+1
        b= a**a
        serie.append(b)
    return serie
#Función para validar y calcular la suma
def calcular_suma_serie(n):
    if n <= 0:
        return "El valor de n debe de ser mayor que 0"
    serie = generar_serie(n)
    suma = sum(serie)
    return suma, serie

#Ingresa el valor de n
n = st.number_input("ingresa el valor de n:", min_value=1, step=1)
serie = generar_serie(n)
#Botón para calcular la suma
if st.button("Calcular suma"):
    suma,serie = calcular_suma_serie(n)
    st.write(f"La serie generada para n={n} es: {serie}")
    st.write(f"La suma de los primeros {n} elementos es: {suma}")

st.write("##############################################################################################")

#Ejercicio 3:  Calcular el número mayor de una lista de N números dados.
st.title("SESION 12 Estructura repetitiva")
st.subheader("Ejercicio 3 : Calcular el número mayor de una lista de N números dados")
# Funcion para encontrar menor
def hallarmenor():
    # Ingresar la cantidad de números
    n = st.number_input("¿Cuántos números deseas ingresar?", min_value=1, value=1)

    # Crear un formulario para ingresar los números
    numeros = []
    for i in range(n):
        num = st.number_input(f"Ingrese el número {i + 1}:", key=f"num_{i}")
        numeros.append(num)

    if st.button("Hallara el Menor"):
        if numeros:
            menor = min(numeros)
            st.success(f"El menor número ingresado es: {menor}")

if __name__ == "__main__":
    hallarmenor()
st.write("##############################################################################################")
import streamlit as st
import numpy as np
#Ejercicio 1v1:  De una lista de 10 números calcular la media y determinar cuántos son mayores que 10, cuantos son iguales y cuántos son menores..
st.title("SESION 12 Estructura repetitiva")
st.subheader("Ejercicio 1 : Calcular de 10 números la media, calcular cuantos son >10 =10 y <10 ")
dieznumeros = []
with st.form(key='my_form'):
    for i in range(1, 11):
        num = st.number_input(f"Ingrese el número {i}:", key=f'num_{i}',  step=1)
        dieznumeros.append(num)
    submit_button = st.form_submit_button(label='Enviar')

contar1=0
contar2=0
contar3=0
    
for i in range(10):
    if dieznumeros[i]>10:
        contar1+=1
    elif dieznumeros[i] ==10:
        contar2+=1
    else:
        contar3+=1
media = np.mean(dieznumeros)
         
if submit_button:
    st.write(f"La media para 10 numeros es= {media} ")
    st.write(f"La cantidad de numeros mayores de 10 son = {contar1} ")
    st.write(f"La cantidad de numeros iguales de 10 son ={contar2} ")
    st.write(f"La cantidad de numeros menores de 10 son = {contar3} ")

st.write("##############################################################################################")
import streamlit as st
import numpy as np
#Ejercicio 1:  De una lista de 10 números calcular la media y determinar cuántos son mayores que 10, cuantos son iguales y cuántos son menores..
st.title("SESION 12 Estructura repetitiva")
st.subheader("Ejercicio 1 : Calcular de 10 números la media, calcular cuantos son >10 =10 y <10 ")

def calcular():
    dieznumeros = [87,45,97,10,10,25,87,-6,-3,0]
    contar1=0
    contar2=0
    contar3=0
    
    for i in range(10):
        if dieznumeros[i]>10:
            contar1+=1
        elif dieznumeros[i] ==10:
            contar2+=1
        else:
            contar3+=1
    media = np.mean(dieznumeros)
    return media,contar1, contar2, contar3       
if st.button("Calcular"):
    media,contar1, contar2, contar3 =calcular()
    st.write(f"La media para 10 numeros es= {media} ")
    st.write(f"La cantidad de numeros mayores de 10 son = {contar1} ")
    st.write(f"La cantidad de numeros iguales de 10 son ={contar2} ")
    st.write(f"La cantidad de numeros menores de 10 son = {contar3} ")


    
st.write("##############################################################################################")
import streamlit as st
import numpy as np
#Ejercicio 3:  CREA UN MENU
st.title("SESION 13 Estructura repetitiva")
st.subheader("Ejercicio 3 : GENERA UN MENU ")
# Crear un menú en la barra lateral
menu = st.sidebar.selectbox("Menú", ["Archivo", "Editar", "Ver", "Salir"])

# Mostrar el contenido según la opción seleccionada
if menu == "Archivo":
    st.write("Has seleccionado la opción 'Archivo'. Aquí puedes manejar archivos.")
    # Opciones específicas para 'Archivo'
    archivo_opcion = st.selectbox("Opciones de Archivo", ["Abrir", "Guardar", "Cerrar"])
    if archivo_opcion == "Abrir":
        st.write("Abrir archivo seleccionado.")
    elif archivo_opcion == "Guardar":
        st.write("Guardar archivo seleccionado.")
    elif archivo_opcion == "Cerrar":
        st.write("Cerrar archivo seleccionado.")
      
elif menu == "Editar":
    st.write("Has seleccionado la opción 'Editar'.")
    # Opciones específicas para 'Editar'
    editar_opcion = st.selectbox("Opciones de Edición", ["Cortar", "Copiar", "Pegar"])
    if editar_opcion == "Cortar":
        st.write("Cortar seleccionado.")
    elif editar_opcion == "Copiar":
        st.write("Copiar seleccionado.")
    elif editar_opcion == "Pegar":
        st.write("Pegar seleccionado.")

elif menu == "Ver":
    st.write("Has seleccionado la opción 'Ver'.")
    # Opciones específicas para 'Ver'
    ver_opcion = st.selectbox("Opciones de Vista", ["Zoom In", "Zoom Out", "Pantalla Completa"])
    if ver_opcion == "Zoom In":
        st.write("Zoom In seleccionado.")
    elif ver_opcion == "Zoom Out":
        st.write("Zoom Out seleccionado.")
    elif ver_opcion == "Pantalla Completa":
        st.write("Pantalla Completa seleccionado.")

elif menu == "Salir":
    st.write("Has seleccionado 'Salir'. Gracias por utilizar la aplicación.")
    # Aquí puedes poner una acción para cerrar o reiniciar la app (si fuera posible en Streamlit).

st.write("##############################################################################################")
import streamlit as st
import numpy as np
#Ejercicio 3:  CREA UN MENU
st.title("SESION 13 Estructura repetitiva")
st.subheader("Ejercicio 3 : GENERA UN MENU ")
# Crear un menú en la barra lateral
menu1 = st.sidebar.selectbox("Menús", ["Archivo", "Editar", "Ver", "Salir"])

# Mostrar el contenido según la opción seleccionada
if menu1 == "Archivo":
    st.write("Has seleccionado la opción 'Archivo'. Aquí puedes manejar archivos.")
        
elif menu1 == "Editar":
    st.write("Has seleccionado la opción 'Editar'.")
    
elif menu1 == "Ver":
    st.write("Has seleccionado la opción 'Ver'.")
    
elif menu1 == "Salir":
    st.write("Has seleccionado 'Salir'. Gracias por utilizar la aplicación.")