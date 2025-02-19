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
        st.image("images/gaza.jpg")
        st.write(
            "Our donation organization is currently concentrating on two locations. One of them is Karthoum in Sudan, "
            "where women and girls are facing famine, displacement, home confinement and gender-based sexual violence. "
            "More than 7,000 new mothers could die in the coming months if their nutritional health needs remain unmet."
            " Women and girls, aged from 9 to 60, are confronted with various forms of sexual violence, such as forced "
            "and child marriage, and prolonged captivity in conditions of sexual slavery. Therefore, your signed petitions, "
            "donations; clothes, money and sanitary products will be directly sent to the UN office and given to women and girls in Khartoum, "
            "who are still hardly surviving the war while living in fear in destructed areas and houses.")

        st.write("United Nations Office Sudan, Gama'a Avenue, House 7, Block 5, Postal Code 11111, Khartoum, Sudan")

    with c2:
        st.image("images/sudan.jpg")
        st.write(
            "Our second donation location is Jabalia, the largest of the Gaza Strip's eight refugee camps. It is "
            "located north of Gaza City, close to a village of the same name. The camp covers an area of only 1.4 "
            "square kilometers. 119,540 Palestine Refugees are registered with UNRWA in Jabalia camp. All of your "
            "donations will be sent to the UNRWA, that help and support refugees with medical care, education and"
            " basic necessities.")

        st.write(
            "The UN's Human Rights Office has condemned the high number of civilians killed in the war in Gaza, saying "
            "its analysis shows close to 70% of verified victims over a six-month period were women and children. The "
            "ages most represented among the dead were five to nine-year-olds. A ceasefire is not enough, many "
            "civilians are left alive, injured, displaced and starving, without access to adequate water, food or "
            "healthcare. Donate with DON-AID!")

        st.write(
            "UNRWA united nations relief and works agency for palestine refugees in the near east Jabalia Camp, "
            "Gaza Strip قطاع غزّة")
