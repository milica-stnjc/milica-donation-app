import streamlit as st

def take_action():
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

    st.header("WHERE YOUR DONATIONS WILL END UP:")
    c1, c2 = st.columns(2)

    with c1:
        st.write("")
        st.image("images/gaza.jpg")

    with c2:
        st.write("")
        st.image("images/sudan.jpg")