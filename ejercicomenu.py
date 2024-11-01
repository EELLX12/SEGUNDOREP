import streamlit as st
import numpy as np
#Ejercicio 3:  CREA UN MENU

st.title("Ejercicio 13.3 : GENERA UN MENU ")
# Crear un menú en la barra lateral
menu1 = st.sidebar.selectbox("Menús", ["Archivo", "Editar", "Ver", "Salir"])

# Mostrar el contenido según la opción seleccionada
if menu1 == "Archivo":
    st.write("Has seleccionado la opción 'Archivo'. Aquí puedes manejar archivos.")
        
elif menu1 == "Editar":
    st.write("Has seleccionado la opción 'Editar'.")
    
elif menu1 == "Ver":
    st.write("Has seleccionado la opción 'Ver'.")
    
elif menu1 == "Salir":
    st.write("Has seleccionado 'Salir'. Gracias por utilizar la aplicación.")