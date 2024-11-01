import streamlit as st

# Inicializa la lista en el estado de la sesión si no existe
if 'numeros' not in st.session_state:
    st.session_state.numeros = []

st.title("Suma de Números")

# Campo de entrada para el número
numero = st.number_input("Ingresa un número (0 para salir)", step=1.0)

# Botón para agregar el número a la lista
if st.button("Agregar número"):
    if numero != 0:
        st.session_state.numeros.append(numero)
        st.success(f"Número {numero} agregado.")
    else:
        st.write("Has ingresado 0. La entrada se detiene.")

# Calcular la suma total si hay números
if st.session_state.numeros:
    suma_total = sum(st.session_state.numeros)
    st.write(f"La suma de los números ingresados es: {suma_total}")
else:
    st.write("No se ingresaron números.")