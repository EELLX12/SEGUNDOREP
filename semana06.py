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