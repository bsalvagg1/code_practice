import streamlit as st

st.write('''
# Welcome to Password Generator
*Get a randomly generated password with a length of your choosing!*
''')

length = int(st.text_input('How long would you like your password to be?'))

letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
char = '!@#$%&*()+?<>'
password = letter + num + char
pwd = ''.join(random.sample(password, length))

st.text_area('Here is your password!')
st.text_area(pwd)