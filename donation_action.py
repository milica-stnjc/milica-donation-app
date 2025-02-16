import streamlit as st
from helpers import connect_to_collection
import pandas as pd

def donation_action():
    st.header("ACTION OF FEBRUARY")
    st.write("This months action is about managing the ceasefire in... tba")
    st.write("We need 15.000 signatures")
    sig_name = st.text_input("Enter your full name")
    button = st.button("Signature")

    # connect to the collection in mongodb
    db_name = 'streamlit'
    collection_name = 'signatures'
    collection = connect_to_collection(db_name, collection_name)

    if button:

        # Create a document - a dictionary with a key and index
        document = {
            "sig_name": sig_name
        }
        # Insert into MongoDB
        collection.insert_one(document)

    user_data = pd.DataFrame(list(collection.find()))

    amount = user_data["sig_name"].count()
    st.write(f"We already have {amount} signatures")
