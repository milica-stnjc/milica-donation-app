import streamlit as st
from helpers import connect_to_collection
import pandas as pd

def donation_action():
    st.header("ACTION OF FEBRUARY: PERMANENT CEASEFIRE IN GAZA")
    st.write("Sign the monthly petition for establishing a permanent ceasefire in Gaza and  to finally clearly "
             "name the serious violations and crimes under international law and to do everything possible to "
             "stop this genocide, to ensure that sufficient humanitarian aid reaches Gaza on a permanent basis, "
             "to lift the illegal blockade of the Gaza Strip and to ensure that the current ceasefire leads to a"
             " permanent ceasefire.")
    st.write("The current ceasefire was announced on 15 January and began four days later, after months of "
             "negotiations led by the US, Qatar and Egypt. Right now, stage one of the temporary ceasefire lasts "
             "42 days: Hamas will release a total of 33 hostages, Israel will release about 1,900 Palestinian "
             "prisoners, Israeli forces will leave populated areas, Displaced Palestinian civilians will be allowed "
             "to return to their neighbourhoods. Stage two will begin after 16 days where negotiations take place "
             "and Israeli forces would completely withdrawal from the Gaza strip: only then a permanent ceasefire "
             "can be established.")
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
