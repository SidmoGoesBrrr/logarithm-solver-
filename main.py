import streamlit as st
import numpy as np

st.title("Logarithmic Calculation App")
st.header("Made by Siddhant because completing physics journal is not fun")
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

    operation_str = f"AL(log({num1}) {'+' if operation == 'Multiplication' else '-'} log({num2})"
    st.subheader(f"{num1} {'x' if operation == 'Multiplication' else '%'} {num2}")
    st.write(f"1) {operation_str})")
    
    # Split the result into the first digit and the rest of the digits
    first_digit, rest_of_digits = str(result).split(".")
    
    st.write(f"2) AL({log_num1:.3f} {'+' if operation == 'Multiplication' else '-'} {log_num2:.3f})")
    st.write(f"3) AL({first_digit:.3f})")
    st.write(f"4)") 
    
    # Calculate the antilog of the result
    antilog_result = 10 ** result
    st.write(f"5) The actual antilog of the result is: {antilog_result:.3f}")
    
