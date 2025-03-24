import streamlit as st
from homepage import homepage
from chat import chat_function
from donation_options import donation_options
from about import about
from take_action import take_action
from donation_action import donation_action
from period_poverty import period_poverty
from contact import contact

st.set_page_config(page_title="DON-AID",
                   page_icon="🏩")

# Organize columns for banner
c1, c2, c3 = st.columns(3)

with c1:
    st.write(' ')

with c2:
    st.image("images/banner.png")

with c3:
    st.write(' ')

# Create a flag to enter the app
if 'enter_app' not in st.session_state:
    st.session_state.enter_app = 0

# Store the username
if 'name' not in st.session_state:
    st.session_state.name = None

# Show the home page if the user hasn't entered the app
if st.session_state.enter_app == 0:
    homepage()

# Show menu options only if the user has entered the app
elif st.session_state.enter_app == 1:
    options = ['About', 'Why Take Action?', 'Donation Options', 'Donation Action',
               'Testimonials and Chat Forum', 'Period Poverty with Active Cycle', 'Contact']

    with st.sidebar:
        st.image("images/donaid-main.png")
        page_selection = st.selectbox("Menu", options)  # Defined inside the if block

    # Display the selected page
    if page_selection == "About":
        about()
    elif page_selection == "Why Take Action?":
        take_action()
    elif page_selection == "Donation Options":
        donation_options()
    elif page_selection == "Donation Action":
        donation_action()
    elif page_selection == "Testimonials and Chat Forum":
        chat_function()
    elif page_selection == "Period Poverty with Active Cycle":
        period_poverty()
    elif page_selection == "Contact":
        contact()
