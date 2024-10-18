import streamlit as ste

#Ejercicio 4:  calcular la suma  de n numeros elevados a la n
st.title("SESION 12 Estructura repetitiva")
st.subheader("Ejercicio 4 : suma  de n numeros elevados a la n")
n = st.number_input("ingresa el valor de n:", min_value=1, step=1)

def generar_serie(n):
    serie = []
    for i in range(n):
        serie.append(i^i)
        serie
    return serie

#Función para validar y calcular la suma
def calcular_suma_serie(n):
    serie = generar_serie(n)
    suma = sum(serie)
    return suma, serie
suma,serie = calcular_suma_serie(n)
st.write(f"La serie generada para n={n} es: {serie}")
st.write(f"La suma de los primeros {n} elementos es: {suma}")
