import streamlit as st

# Función principal
def main():
    st.title("Calculadora de Media de N Números")

    # Inicializar acumulador y contador
    suma = 0
    contador = 0

    # Entrada de números y acumulación de valores
    while True:
        numero = st.number_input("Ingrese un número (0 para finalizar):", step=1.0, format="%f", key=f"numero_{contador}")

        # Si el usuario ingresa 0, se termina la entrada
        if numero == 0:
            break

        # Acumular el número y contar cada entrada
        suma += numero
        contador += 1

    # Calcular la media solo si se ingresaron números válidos
    if contador > 0:
        media = suma / contador
        st.success(f"Suma total de los números: {suma}")
        st.success(f"Media de los números: {media}")
    else:
        st.info("No se ingresaron números.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
