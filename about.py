import streamlit as st

def about():
    st.image("images/about.png")
    st.subheader("SUDAN AND GAZA IN CRISIS:")
    st.write(
        "Unfortunately, there are are countries that loose over 10,000 and more inhabitants of their beloved country. Mothers, fathers, children, grandparents, relatives, friends, neighbours live in fear and danger and are closer to death than to escape or possible ceasefires. Just to name two of them, that already suffer in uncertain living circumstances: ")
    st.write(
        "A brutal war between the Sudanese Armed Forces and the Rapid Support Forces has caused widespread destruction in Sudan, including gender-based violence like sexual assault, domestic abuse and exploitation and lack of sanitary access, as well as healthcare. As this conflict severely disrupted  food supply chains, women are pressured to take on responsibility to feed their families. ")
    st.write(
        "This humanitarian catastrophe in the region of Gaza and Palestine leads to severe shortages of food, water, and essential medical supplies. Women and young girls get displaced from their homes and the lack of education and sanitary access harms their well-being and mental health. Civilians are cut off from aid and health care, with no functioning hospitals since 2023")
    st.subheader("EVERY CONTRIBUTION MATTERS! DONATE TO THOSE IN DESPERATE NEED!")

    # Insert informative Youtube Videos
    url1 = "https://www.youtube.com/watch?v=RWdWiE73RIw"
    st.video(url1, autoplay=False)
    url2 = "https://www.youtube.com/watch?v=zsNj8DiJv-A"
    st.video(url2, autoplay=False)
