import streamlit as st

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: División por cero"

def main():
    st.title("Calculadora Básica")
    #Entrada de datos
    numero1 = st.number_input("Ingrese el primer número:", format="%f")
    numero2 = st.number_input("Ingrese el segundo número:", format="%f")
    #Selección de operación
    operacion = st.selectbox("Seleccione la operación", ("Suma", "Resta", "Multiplicación", "División"))
    #Realizar la operación seleccionada
    if operacion == "Suma":
        resultado = suma(numero1, numero2)
    elif operacion == "Resta":
        resultado = resta(numero1, numero2)
    elif operacion == "Multiplicación":
        resultado = multiplicacion(numero1, numero2)
    elif operacion == "División":
        resultado = division(numero1, numero2)
    #monstrar el resultado
    st.write(f"Resultado: {resultado}")
if __name__ == "__main__":
    main()



#------------------------------------2do ejemplo-----------------------------------

import streamlit as st
import math

#las funciones se declaran como def

def calcular_area(radio):
    return math.pi * (radio**2)

def calcular_perimetro(radio):
    return 2*math.pi * radio

def main():
    st.title("Calculo de area y perimetro de circunferencia")
    #Entrada de datos
    radio = st.number_input("Ingrese el radio de circunferencia:", min_value = 0.0, step=0.1)
    
   
    if radio > 0:
        area = calcular_area(radio)
        perimetro = calcular_perimetro(radio)
    
    #monstrar el resultado
    st.write(f"Area : {area:2f}")
    st.write(f"Perimetro : {perimetro:2f}")
if __name__ == "__main__":
    main()
