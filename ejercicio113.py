import streamlit as st
import numpy as np

st.title("Ejercicio 1 de 13 : ingresar numeros hasta que se introdusca cero, imprimir suma y media ")

def main():
    
    
    # Lista para almacenar los números ingresados
    numeros = []  

    if True:
        numero = st.number_input("Ingresa un número (0 para salir)", step=1.0)
        
        if numero == 0:
            break
        else:
            numeros.append(numero)
    else:
        st.write("No se ingresaron números.")

    
    suma = sum(numeros)
    media =np.mean(numeros)
    st.write(f"La suma de los números ingresados es: {suma}")
    st.write(f"La media de los números ingresados es: {media}")
    

if __name__ == "__main__":
    main()

