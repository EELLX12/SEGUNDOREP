import streamlit as st

#Ejercicio 4:  calcular la suma  de n numeros elevados a la n
st.title("SESION 12 Estructura repetitiva")
st.subheader("Ejercicio 4 : suma  de n numeros elevados a la n")
#Función para generar serie
def generar_serie(n):
    serie = []
    for i in range(n):
        a=i+1
        b= a**a
        serie.append(b)
    return serie
#Función para validar y calcular la suma
def calcular_suma_serie(n):
    if n <= 0:
        return "El valor de n debe de ser mayor que 0"
    serie = generar_serie(n)
    suma = sum(serie)
    return suma, serie

#Ingresa el valor de n
n = st.number_input("ingresa el valor de n:", min_value=1, step=1)
serie = generar_serie(n)
#Botón para calcular la suma
if st.button("Calcular suma"):
    suma,serie = calcular_suma_serie(n)
    st.write(f"La serie generada para n={n} es: {serie}")
    st.write(f"La suma de los primeros {n} elementos es: {suma}")

st.write("##############################################################################################")

#Ejercicio 3:  Calcular el número mayor de una lista de N números dados.
st.title("SESION 12 Estructura repetitiva")
st.subheader("Ejercicio 3 : Calcular el número mayor de una lista de N números dados")
# Funcion para encontrar menor
def encontrar_menor():
    # Pedir al usuario la cantidad de números
    n = int(input("¿Cuántos números deseas ingresar? "))
    if n <= 0:
        print("Debes ingresar un número positivo.")
        return
    # Inicializar la lista para almacenar los números
    numeros = []

    # Ingresar los números
    for i in range(n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(num)

    # Encontrar el menor número
    menor = min(numeros)

    # Mostrar el resultado
    
    return menor

# Llamar a la función
elmenos=encontrar_menor()
print(f"El menor número ingresado es: {elmenos}")