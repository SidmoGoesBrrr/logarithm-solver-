import streamlit as st
import numpy as np

st.title("Logarithmic Calculation App")
st.header("Made by Siddhant because completing the physics journal is not fun")

# Input for the first number
num1 = st.number_input("Enter the first number (up to 3 decimal places):", format="%.3f")

# Input for the second number
num2 = st.number_input("Enter the second number (up to 3 decimal places):", format="%.3f")

# Dropdown to select the operation
operation = st.selectbox("Select operation:", ["Multiplication", "Division"])

if st.button("Calculate"):
    if operation == "Multiplication":
        result = np.log10(num1) + np.log10(num2)
        log_num1 = np.log10(num1)
        log_num2 = np.log10(num2)
    elif operation == "Division":
        result = np.log10(num1) - np.log10(num2)
        log_num1 = np.log10(num1)
        log_num2 = np.log10(num2)

    operation_str = f"AL(log({num1}) + log({num2}))"
    st.subheader(f"{num1} {'x' if operation == 'Multiplication' else '%'} {num2}")
    st.write(f"1) {operation_str}")

    result1 = log_num1 + log_num2
    st.write(f"2) AL({log_num1:.3f} + {log_num2:.3f})")
    st.write(f"3) AL({result1:.3f})")
    antilog_result_sci = f"{result:.5f} x 10^{int(np.floor(result))}"
    st.write(f"4) The antilog of the result is approximately: {antilog_result_sci}")
    st.write(f"5) The actual antilog of the result is: {10 ** result:.3f}")
