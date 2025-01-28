import streamlit as st

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
            st.session_state["comments"].append({"name": username, "comment": comment})
            st.success("Your comment has been posted!")
        else:
            st.error("Please fill out both fields before submitting.")

    # Display Comments Section
    st.subheader("Comments")
    if st.session_state["comments"]:
        for i, entry in enumerate(st.session_state["comments"], 1):
            st.markdown(f"**{i}. {entry['name']}**: {entry['comment']}")
    else:
        st.write("No comments yet. Be the first to share your thoughts!")

