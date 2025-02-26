import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "Kilometers to Miles": 0.621371,
        "Miles to Kilometers": 1.60934,
        "Kilograms to Pounds": 2.20462,
        "Pounds to Kilograms": 0.453592,
        "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
        "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9
    }

    if isinstance(conversion_factors[f"{from_unit} to {to_unit}"], float):
        return value * conversion_factors[f"{from_unit} to {to_unit}"]
    else:
        return conversion_factors[f"{from_unit} to {to_unit}"](value)

st.title("Unit Converter")

units = ["Kilometers", "Miles", "Kilograms", "Pounds", "Celsius", "Fahrenheit"]
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

if from_unit != to_unit:
    value = st.number_input(f"Enter value in {from_unit}:", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
else:
    st.warning("Please select different units for conversion!")
