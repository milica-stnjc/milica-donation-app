import streamlit as st
from helpers import connect_to_collection
import pandas as pd

def retrieve_data():
    # connect to the collection in mongodb
    db_name = 'streamlit'
    collection_name = 'don-aid'
    collection = connect_to_collection(db_name, collection_name)

    # fetch data
    user_data = pd.DataFrame(list(collection.find()))
    # sort the data and display the (hopefully) current user
    current_user = user_data[user_data.name == st.session_state.name]
    #st.write(current_user)
    sanitary_total = list(current_user['How many sanitary products do you want to donate?'])[-1]
    st.write(f"{sanitary_total} sanitary products")

    housing_total= list(current_user['How many housing goods do you want to donate?'])[-1]
    st.write(f"{housing_total} housing goods")

    clothes_total = list(current_user['How many clothes/blankets do you want to donate?'])[-1]
    st.write(f"{clothes_total} clothes/blankets")

    sleeping_total = list(current_user['How many sleeping mats do you want to donate?'])[-1]
    st.write(f"{sleeping_total} sleeping mats")

    money_total = list(current_user['donated_amount'])[-1]
    st.write(f"{money_total} €")

    st.write(f" SEE YOU NEXT TIME {st.session_state.name.upper()}")

    #st.write(user_data)
    total_all_users = user_data["donated_amount"].sum()
    st.subheader(f"WE HAVE RAISED {total_all_users} € SO FAR")