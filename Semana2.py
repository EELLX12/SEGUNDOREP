import streamlit as st

#titulo a la aplicacion
st.title("Introduccion ava♫")

#descripcionon
st.write("phyton es un")

#seccion
st.header("ejemplo 1: enteros")
st.write(" en phyton un entero")

#imput paraque el usuario ingrese dato de preferencia entero
int_variable = st.number_input("ingrese  un entero")
st.code(f" int_variable = {int_variable}# tipo {type(int_variable)}")