import streamlit as st
import random
st.write('''
# Welcome to Password Generator
*Get a randomly generated password with a length of your choosing!*
''')

length = st.text_input('How long would you like your password to be?')

letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
char = '!@#$%&*()+?<>'
password = letter + num + char
pwd = ''.join(random.sample(password, int(length))

st.text_area('Here is your password!')
st.text_area(pwd)