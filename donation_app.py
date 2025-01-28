import streamlit as st
from homepage import homepage
from chat import chat_function
from donation_options import donation_options
from retrieve_data import retrieve_data

st.set_page_config(page_title="DON-AID",
                   page_icon="🏩")

st.title("DON-AID FOR WOMEN")

# create a flag to entef the app
if 'enter_app' not in st.session_state:
    st.session_state.enter_app = 0

# store the user name
if 'name' not in st.session_state:
    st.session_state.name = None

# show the home page
if st.session_state.enter_app == 0:
    homepage()

if st.session_state.enter_app == 1:
    options = ['About', 'Why Take Action?', 'Donation Options', 'THANK YOU', 'Donation Action',
               'Testimonials and Chat Forum', 'Period Poverty with Sela', 'Contact']
    page_selection = st.sidebar.selectbox("Menu", options)

    if page_selection == "About":
        st.image("images/about.png", use_column_width=True)
        st.write("SUDAN AND GAZA IN CRISIS:")
        st.write(
            "Unfortunately, there are are countries that loose over 10,000 and more inhabitants of their beloved country. Mothers, fathers, children, grandparents, relatives, friends, neighbours live in fear and danger and are closer to death than to escape or possible ceasefires. Just to name two of them, that already suffer in uncertain living circumstances: ")
        st.write(
            "A brutal war between the Sudanese Armed Forces and the Rapid Support Forces has caused widespread destruction in Sudan, including gender-based violence like sexual assault, domestic abuse and exploitation and lack of sanitary access, as well as healthcare. As this conflict severely disrupted  food supply chains, women are pressured to take on responsibility to feed their families. ")
        st.write(
            "This humanitarian catastrophe in the region of Gaza and Palestine leads to severe shortages of food, water, and essential medical supplies. Women and young girls get displaced from their homes and the lack of education and sanitary access harms their well-being and mental health. Civilians are cut off from aid and health care, with no functioning hospitals since 2023")
        st.write("EVERY CONTRIBUTION MATTERS! DONATE TO THOSE IN DESPERATE NEED!")
        url1 = "https://www.youtube.com/watch?v=RWdWiE73RIw"
        st.video(url1, autoplay=False)
        url2 = "https://www.youtube.com/watch?v=zsNj8DiJv-A"
        st.video(url2, autoplay=False)


    elif page_selection == "Why Take Action?":
        st.write(
            "Why do women suffer severly in war zones? Frequently, women are confronted with sexual assault, are likely to have denied access to sanitary products and get offered no education and no job options as and only 2 out of 10 women get the possibility to flee and escape from war zones")
        st.header("SO WHY SHOULD YOU TAKE ACTION?")
        st.markdown(
            "[care-international.org's report’s findings from conflict countries include:](https://www.care-international.org/news/women-war-new-care-report-reveals-how-women-are-leaders-first-response-and-recovery-during)")
        st.write(
            "1. Women’s basic needs are going unfilled. Livelihood is women’s highest priority. 58% of women CARE spoke to in conflict zones said they need livelihood assistance. 41% of women prioritized food as one of the biggest impacts of conflict.")
        st.write(
            "2. Sexual violence is a growing threat. More than 257 million women were living in countries that had significant or massive reports of sexual violence in conflict in 2021.")
        st.write("3. Compromised health services put women and children at severe risk.")
        st.write("4. One in 4 babies born in 2022 were born within 50km of a conflict.")
        st.write(
            "5. One in 2 women who dies during pregnancy or childbirth is in a conflict area. Maternal mortality is more than 40 times higher in fragile contexts than it is in developing countries.")
        st.write("6. Formal leadership structures exclude women, compromising peace and prosperity for everyone.")
        st.write(
            "7. Narratives of conflict underrepresent women. Only 5% of articles about conflict in the last decade focus on women’s experiences.")

    elif page_selection == "Donation Options":
        donation_options()
    elif page_selection == "THANK YOU":
        st.write("THANK YOU FOR DONATING...")
        retrieve_data()
    elif page_selection == "Donation Action":
        st.header("ACTION OF FEBRUARY")
        st.write("This months action is about managing the ceasefire in... tba")
        st.write("We need 15.000 signatures")
        st.text_input("Enter your full name")
        button = st.button("Signature")
    elif page_selection == "Testimonials and Chat Forum":
        chat_function()
    elif page_selection == "Period Poverty with Sela":
        st.write("This page is still under construction, as the collaboration process with Sela is ongoing")
    elif page_selection == "Contact":
        st.image("images/contact.png")
        st.write("© Milica Stanojić")
        st.write("milica.stanojic@stud.leuphana.de")
        st.write("Instagram: https://www.instagram.com/atelierstanojic/")
        st.write("LinkedIn: https://www.linkedin.com/in/milica-stanoji%C4%87-255605345/")