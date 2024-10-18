import streamlit as st

#Ejercicio 4:  calcular la suma  de n numeros elevados a la n
st.title("SESION 12 Estructura repetitiva")
st.subheader("Ejercicio 4 : suma  de n numeros elevados a la n")
def generar_serie(n):
    serie = []
    i=1
    for i in range(n):
        serie.append(i^i)
        i+=1
        st.write(i)
    return serie



n = st.number_input("ingresa el valor de n:", min_value=1, step=1)



