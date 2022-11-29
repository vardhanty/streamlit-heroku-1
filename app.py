import streamlit as st
import pandas as pd

st.write("""
#  largest among 3 given numbers (value greater than the other two) """)
#Get Input

st.header('User Input Parameters')
a=st.number_input('Enter first number')
b=st.number_input('Enter second number')
c=st.number_input('Enter third number')
max=a
if max<b:
    max=b
if max<c:
    max=c
st.write('maximum number is')
st.write(max)
