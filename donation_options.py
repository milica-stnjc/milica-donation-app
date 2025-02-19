import streamlit as st
from helpers import connect_to_collection
from retrieve_data import retrieve_data

def donation_options():
    # Don Aid
    st.title("Donation Options: Choose at least one option")
    st.write("**THANK YOU** for your financial, emotional and hands-on support!")
    # the info you want from user
    amount1 = st.number_input("How many **sanitary products** do you want to donate?", step=1)
    amount2 = st.number_input("How many **housing goods** do you want to donate?", step=1)
    amount3 = st.number_input("How many **clothes/blankets** do you want to donate?", step=1)
    amount4 = st.number_input("How many **sleeping mats** do you want to donate?", step=1)
    amount5 = st.number_input("Do you want to donate money, if so: **Insert your amount in €**", step=1)
    amount6 = st.text_input("Your **personal message** to the receiving person:")
    button = st.button("Donate")

    # when user clicks on button the data is stored
    if button:
        # connect to the collection in mongodb
        db_name = 'streamlit'
        collection_name = 'don-aid'
        collection = connect_to_collection(db_name, collection_name)

        # Create a document - a dictionary with a key and index
        document = {
            "How many sanitary products do you want to donate?": amount1,
            "How many housing goods do you want to donate?": amount2,
            "How many clothes/blankets do you want to donate?": amount3,
            "How many sleeping mats do you want to donate?": amount4,
            "donated_amount": amount5,
            "Your personal message to the receiving person:": amount6,
            "name": st.session_state.name
        }
        # Insert into MongoDB
        collection.insert_one(document)
        retrieve_data()
