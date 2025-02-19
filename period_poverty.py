import streamlit as st

def period_poverty():
    st.subheader("Get Active with DON-AID & Active Cycle")
    st.subheader("Join our fight against period poverty.")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**1 in 4 teenagers and 1 in 3 adults in the United States cannot afford "
                 "menstrual products**, affecting especially teens of color and "
                 "those from low-income households. "
                 "**1 in 10 girls in Sub-Saharan Africa misses school during their menstrual "
                 "cycle**, resulting in lost educational opportunities that can shape their future. "
                 "**In Gaza, more than 540,000 women and girls of reproductive age lack access to "
                 "menstrual products** and are forced to use unsafe alternatives like cloth or sponges. "
                 "Menstrual hygiene is a basic human need, yet millions worldwide are"
                 "struggling to access the products they need to manage their periods safely"
                 "and with dignity. Period poverty isn’t just about missing products—it’s about "
                 "missed opportunities, health risks, and the emotional toll of navigating a world "
                 "where basic needs are out of reach.")

    with c2:
        st.image("images/TB2-period-poverty.png")

    st.markdown(
        "[CLICK HERE to learn about absence of girls in school, due to LACK OF MENSTRUAL EDUCATION!](https://blogs.worldbank.org/en/education/globally-periods-are-causing-girls-be-absent-school)")
    st.subheader("Together, we can make a difference.")
    st.write("For many, the added cost of menstrual products makes an already tight situation even harder. "
             "Period poverty isn’t just someone else’s problem—it’s a challenge "
             "we all face together.")
    st.subheader("Cooperation with DON-AID and Active Cycle")
    st.write("**Sela Schulze and Milica Stanojić** are both young founders who engage in the **fight for women’s rights**. “Active Cycle“ helps women to understand their menstrual cycle and balance their lifestyle around it. “DON-AID“ is a donation platform that specifically supports women in war zones and shares testimonials to raise awareness.")
    st.write("**Active Cycle**'s mission is to reduce the stigma surrounding menstrual health by providing guidance and support for cycle-syncing workout routines at all levels. We show that the menstrual cycle is not a weakness but a source of strength. Use the app to educate yourself on your menstrual cycle and improve your life quality, by means of suggestions and cycle-tracking.")
    st.write("**DON-AID** actively shares your donations and improves sanitary access through money, material donations and signatures. As more than **1.5 billion people still lack basic basic sanitation services and 1 in 10 women in rural areas across 12 countries do not have a private place to wash and change during periods**, period poverty is a prominent and essential topic,"
             "as periods do not stop for war. Not only women lack menstrual education of their own bodies, but more importantly decision-makers and political authorities do not involve women’s needs in policy-making.")
    st.write("With DON-AID every donation can make a change. Comment on personal stories of women in war zones, fund teaching possibilities in war zones and donate sanitary products.")

