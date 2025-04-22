import streamlit as st
st.image("gases ideales.png")

R = 0.0821  # L·atm/mol·K

st.title("Calculadora de la Ecuación de Gases Ideales")
st.write("Ecuación: PV = nRT")

opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

if opcion == "Presión (P)":
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.2f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.4f")
    if volumen > 0:
        presion = (moles * R * temperatura) / volumen
        st.success(f"Presión = {presion:.4f} atm")

elif opcion == "Volumen (V)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.4f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.4f")
    if presion > 0:
        volumen = (moles * R * temperatura) / presion
        st.success(f"Volumen = {volumen:.4f} L")

elif opcion == "Temperatura (T)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.4f")
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.2f")
    moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.4f")
    if moles > 0:
        temperatura = (presion * volumen) / (moles * R)
        st.success(f"Temperatura = {temperatura:.2f} K")

elif opcion == "Número de moles (n)":
    presion = st.number_input("Presión (atm)", min_value=0.0, format="%.4f")
    volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.2f")
    temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.2f")
    if temperatura > 0:
        moles = (presion * volumen) / (R * temperatura)
        st.success(f"Número de moles = {moles:.4f} mol")
