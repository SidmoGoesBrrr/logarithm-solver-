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
        antilog_result = 10 ** result
    elif operation == "Division":
        result = np.log10(num1) - np.log10(num2)
        log_num1 = np.log10(num1)
        log_num2 = np.log10(num2)
        antilog_result = 10 ** result  # Corrected antilog calculation

    operation_str = f"AL(log({num1}) {'+' if operation == 'Multiplication' else '-'} log({num2}))"
    st.subheader(f"{num1} {'x' if operation == 'Multiplication' else '%'} {num2}")
    st.write(f"1) {operation_str}")

    result1 = log_num1 + log_num2
    st.write(f"2) AL({log_num1:.3f} {'+' if operation == 'Multiplication' else '-'} {log_num2:.3f})")
    st.write(f"3) AL({result1:.3f})")

    # Calculate the antilog of the result in scientific notation with superscripts
    antilog_result_sci = "{:.4f}".format(antilog_result)  # Updated formatting
    exponent = int(np.log10(antilog_result))
    antilog_result_custom_sci = "{:.4f} x 10^{}".format(antilog_result / 10 ** exponent, exponent)
    st.write("4) " + antilog_result_custom_sci)
    st.write(f"5) The actual antilog of the result is: {antilog_result:.5f}")  # Adjusted precision
