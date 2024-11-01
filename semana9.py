st.title("SESION 12 Ejercicio 1 : Calcular de 10 números la media, calcular cuantos son >10 =10 y <10 ")
import streamlit as st
import numpy as np

dieznumeros = []
with st.form(key='my_form'):
    for i in range(1, 11):
        num = st.number_input(f"Ingrese el número {i}:", key=f'num_{i}',  step=1)
        dieznumeros.append(num)
    submit_button = st.form_submit_button(label='Enviar')

contar1=0
contar2=0
contar3=0
    
for i in range(10):
    if dieznumeros[i]>10:
        contar1+=1
    elif dieznumeros[i] ==10:
        contar2+=1
    else:
        contar3+=1
media = np.mean(dieznumeros)
         
if submit_button:
    st.write(f"La media para 10 numeros es= {media} ")
    st.write(f"La cantidad de numeros mayores de 10 son = {contar1} ")
    st.write(f"La cantidad de numeros iguales de 10 son ={contar2} ")
    st.write(f"La cantidad de numeros menores de 10 son = {contar3} ")

