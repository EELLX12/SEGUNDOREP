import streamlit as st
import numpy as np

st.title("Ejercicio 1 de 13 : ingresar numeros hasta que se introdusca cero, imprimir suma y media ")

if 'numeros' not in st.session_state:
    st.session_state.numeros = []

def main():
    
    
    # Lista para almacenar los números ingresados
    numeros = []  

    while True:
        numero = st.number_input("Ingresa un número (0 para salir)", step=1.0)
        
        if numero == 0:
        break

    st.session_state.numeros.append(numero)

# Calcular la suma total
if st.session_state.numeros:
    suma = sum(st.session_state.numeros)
    media =np.mean(st.session_state.numeros)
    st.write(f"La suma de los números ingresados es: {suma}")
    st.write(f"La media de los números ingresados es: {media}")
else:
    st.write("No se ingresaron números.")
       

if __name__ == "__main__":
    main()

