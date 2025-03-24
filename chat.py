import streamlit as st
from helpers import connect_to_collection
import pandas as pd

def chat_function():
    # Comment storage and list to hold comments
    if "comments" not in st.session_state:
        st.session_state["comments"] = []

    st.title("‘I’ve forgotten what it means to be a woman’: Women in Gaza share their stories")
    st.image("images/estemad.jpg")
    st.write("Here, women have the ability to share their stories during the current war and have the ability get "
             "support from you. Share your thoughts below!")
    st.markdown(
        "[aljazeera.com:](https://www.aljazeera.com/features/2024/3/8/a-suffering-i-would-not-wish-on-any-woman-women-of-gaza)")
    st.write("Etemad Assaf, 29, is eight months pregnant, displaced and scared of giving birth to her third child in "
             "the horrific conditions she is situated in, in Gaza.")
    st.write("“The war turned our lives upside down. Every night I feel like I’m going to give birth now because I’m "
             "so tired. You see? Is this a suitable life for a pregnant woman? A tent, cold, open air and the "
             "lack of the basic necessities of life? My little daughter, who is 11 months old, needs diapers, and "
             "they are expensive. We can barely afford food, and sometimes there is no food to eat at all. "
             "My big concern now is my impending birth and the dire conditions around me, particularly given what we"
             " hear about the complete collapse of hospitals in Gaza. The healthcare system is crumbling. "
             "There is not even a proper place to rest after delivery. Two days ago, I looked at myself in the mirror "
             "for the first time since and was shocked by how my facial features had changed and my skin, which has "
             "darkened from sitting in the sun. I used to take care of myself, moisturising my skin and hands before"
             " bed and showering was my daily routine. Now these are distant dreams.”")

    # Input box for comments
    with st.form(key="comment_form"):
        username = st.text_input("Your Name", placeholder="Enter your name")
        comment = st.text_area("Your Comment", placeholder="Share your thoughts...")
        submit_button = st.form_submit_button("Submit Comment")

    # Store the comment when submitted
    if submit_button:
        if username and comment:
            st.session_state["comments"].insert(0,{"name": username, "comment": comment})
            st.success("Your comment has been posted!")
        else:
            st.error("Please fill out both fields before submitting.")

    # connect to the collection in mongodb
    db_name = 'streamlit'
    collection_name = 'chat'
    collection = connect_to_collection(db_name, collection_name)

    if submit_button:

        # Create a document - a dictionary with a key and index
        document = {
            "comments": comment,
            "usernames": username
        }
        # Insert into MongoDB
        collection.insert_one(document)

    user_data = pd.DataFrame(list(collection.find()))

    for x in range(len(user_data)):
        st.write((user_data["comments"][x]), (user_data["usernames"][x]) )



