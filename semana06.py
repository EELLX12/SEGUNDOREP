import streamlit as st

#Ejercicio5: generar e imprimir los números pares entre 0 y 100
st.title("Ejercicios de números pares")

st.subheader("Ejercicio 5: Números pares entre 0 y 100")
pares_0_100 = [i for i in range(0,101) if i % 2 == 0]
st.write("Números pares entre 0 y 100:")
st.write(pares_0_100)


#Ejercicio5 con botón
st.markdown("""
    <style>
    div.stButton > button{
        background-color: #8B0000;
        color: white;
        font-size: 16px;
        padding; 10px;
        border-radius: 10px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

if st.button("Mostrar números pares entre 0 y 100"):
    pares0a100 = [i for i in range(0,101) if i % 2 == 0]
    st.write("Número pares entre 0 y 100:")
    st.write(pares0a100)

st.write("############################################################################")

#Función para generar la serie numérica
def generar_serie(n):
    serie = []
    elementos = [1, 5, 3, 7, 5, 9, 7] 
    for i in range(n):
        serie.append(elementos[i % len(elementos)])
    return serie

#Función para validar y calcular la suma
def calcular_suma_serie(n):
    if n <= 0:
        return "El valor de n debe de ser mayor que 0"
    serie = generar_serie(n)
    suma = sum(serie)
    return suma, serie

#Streamlit para obtener el valor de n
st.title("Ejercicio 6: Suma de los primeros n elementos de la serie")

#Ingresar un número por teclado
n = st.number_input("ingresa el valor de n:", min_value=1, step=1)

#Botón para calcular la suma
if st.button("Calcular suma"):
    suma,serie = calcular_suma_serie(n)
    st.write(f"La serie generada para n={n} es: {serie}")
    st.write(f"La suma de los primeros {n} elementos es: {suma}")