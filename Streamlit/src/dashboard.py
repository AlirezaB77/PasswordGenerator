import streamlit as st
from Password_Generator import PinPasswordGenerator,RandomPasswordGenerator,MemorablePasswordGenerator

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPHE403Xh_ImoW-MmACGAO6ScnVSrdQPdpEw&s",width=400, use_column_width="auto")
st.title(":sparkles: Password Generator")

option = st.radio("Select a Password Generator",('Pin Password','Random Password','Memorable Password'))

if option == 'Pin Password':
    lenght = st.slider("lenght of password ",4,16,8)
    Password = PinPasswordGenerator(lenght)

elif option == 'Random Password':
    lenght = st.slider("lenght of password ",4,16,8)
    number = st.toggle("include number")
    symbol = st.toggle("include symbol")
    Password = RandomPasswordGenerator(lenght,number,symbol)

elif option == 'Memorable Password':
    number_word = st.slider("lenght of password ",4,16,8)
    separator = st.text_input("Enter separator for word" , value="-")
    capital = st.toggle("include capital word")
    Password = MemorablePasswordGenerator(number_word,separator,capital)


Password = Password.generate()
st.write(f'your Password is  `{Password}`')