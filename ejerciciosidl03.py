import streamlit as st

#Ejercicio 4:  calcular la suma  de n numeros elevados a la n
st.title("SESION 12 Estructura repetitiva")
st.subheader("Ejercicio 4 : suma  de n numeros elevados a la n")
def generar_serie(n):
    serie = []
    for i in range(n):
        a=i+1
        serie.append(a^a)
        st.write(serie[i])
        st.write(a)
        
    return serie
    i+=i

n = st.number_input("ingresa el valor de n:", min_value=1, step=1)
serie = generar_serie(n)
st.write(f"La serie generada para n={n} es: {serie}")

lst = [10,20,30,40] 
x = 1 
lst.append(x) 
st.write(lst) 