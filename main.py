import streamlit as st
import numpy as np

st.title("Logarithmic Calculation App")

# Input for the first number
num1 = st.number_input("Enter the first number (up to 3 decimal places):", format="%.3f")

# Input for the second number
num2 = st.number_input("Enter the second number (up to 3 decimal places):", format="%.3f")

# Dropdown to select the operation
operation = st.selectbox("Select operation:", ["Multiplication", "Division"])

# Perform the operation and calculate the logarithms
if operation == "Multiplication":
    result = np.log10(num1) - np.log10(num2)
    operation_str = "AL(log({} / {}))".format(num1, num2)
    log_num1 = np.log10(num1)
    log_num2 = np.log10(num2)
elif operation == "Division":
    result = np.log10(num1) - np.log10(num2)
    operation_str = "AL(log({} / {}))".format(num1, num2)
    log_num1 = np.log10(num1)
    log_num2 = np.log10(num2)

# Display the steps
st.markdown("1) {}".format(operation_str))
st.markdown("2) AL({:.3f} - {:.3f})".format(log_num1, log_num2))
st.markdown("3) AL({:.3f})".format(result))

# Calculate the antilog of the result
antilog_result = 10 ** result
st.markdown("4) The actual antilog of the result is: {:.3f}".format(antilog_result))
