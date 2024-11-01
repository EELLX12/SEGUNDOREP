import streamlit as st

# Inicializamos una lista en el estado de la sesión si no existe
if 'numeros' not in st.session_state:
    st.session_state.numeros = []

st.title("Suma de Números")

# Bucle para ingresar números hasta que se ingrese cero
while True:
    numero = st.number_input("Ingresa un número (0 para salir)", step=1.0)

    if numero == 0:
        break

    st.session_state.numeros.append(numero)

# Calcular la suma total
if st.session_state.numeros:
    suma_total = sum(st.session_state.numeros)
    st.write(f"La suma de los números ingresados es: {suma_total}")
else:
    st.write("No se ingresaron números.")