import streamlit as st
from helpers import connect_to_collection
import pandas as pd

def chat_function():
    # Placeholder for comments storage
    if "comments" not in st.session_state:
        st.session_state["comments"] = []  # A list to hold comments

    # Title or Article Display
    st.title("‘I’ve forgotten what it means to be a woman’: Nada Abdelsalam")
    st.write("Here is the monthly testimonial from Gaza women who share their stories. Share your thoughts below!")

    # Input Box for Comments
    with st.form(key="comment_form"):
        username = st.text_input("Your Name", placeholder="Enter your name")
        comment = st.text_area("Your Comment", placeholder="Share your thoughts...")
        submit_button = st.form_submit_button("Submit Comment")

    # Store the comment when submitted
    if submit_button:
        if username and comment:  # Ensure both fields are filled
            st.session_state["comments"].insert(0,{"name": username, "comment": comment})
            st.success("Your comment has been posted!")
        else:
            st.error("Please fill out both fields before submitting.")

    # Display Comments Section
   # st.subheader("Comments")
   # if st.session_state["comments"]:
    #    for i, entry in enumerate(st.session_state["comments"], 1):
    #        st.markdown(f"**{i}. {entry['name']}**: {entry['comment']}")
   # else:
    #    st.write("No comments yet. Be the first to share your thoughts!")

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



