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
def main():
    # Ingresar la cantidad de números
    n = st.number_input("¿Cuántos números deseas ingresar?", min_value=1, value=1)

    # Crear un formulario para ingresar los números
    numeros = []
    for i in range(n):
        num = st.number_input(f"Ingrese el número {i + 1}:", key=f"num_{i}")
        numeros.append(num)

    if st.button("Hallara el Menor"):
        if numeros:
            menor = min(numeros)
            st.success(f"El menor número ingresado es: {menor}")

if __name__ == "__main__":
    main()