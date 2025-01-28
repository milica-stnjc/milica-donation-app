import streamlit as st

def homepage():
    placeholder = st.empty()

    container = placeholder.container()

    container.image("images/donaid.png", use_column_width=True)
    container.write(
        "DON-AID is a donation app for women in war zones that suffer from inequality, restrictionn of basic necessities and lack of education. This application supports women in need, raises awareness, teaches about period poverty, shares stories and most importantly: gives YOU the option to donate!")
    name = container.text_input("Enter your name to registrate")
    container.write("© Milica Stanojić")

    if name:
        st.session_state.enter_app = 1
        st.session_state.name = name
        placeholder.empty()

