import streamlit as st
import pickle

#Adding trained model into program
model = pickle.load(open("sorting_hat_model.pkl", "rb"))
house_names = pickle.load(open("house_names.pkl", "rb"))
 

page_element = """
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://static.vecteezy.com/system/resources/previews/018/800/333/non_2x/blue-sky-and-clouds-with-stars-anddark-gray-watercolor-background-colorful-watercolor-paint-background-dark-blue-color-grunge-texture-vector.jpg");
  background-size: cover;
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

blood_status, bravery, intelligence, loyalty, ambition, dark_arts, quidditch_skills, dueling_skills, creativity = 0, 0, 0, 0, 0, 0, 0, 0, 0
with st.form("my_form"):
    st.title("Fill out this Form to find your Wizarding House")
    st.subheader("If you're a true Harry Potter fan, chances are you've taken more than a few Hogwarts House quizzes over the years—and maybe you've ended up with different results every time. One quiz says you're a brave Gryffindor, another insists you're a clever Ravenclaw, while the next places you in loyal Hufflepuff or ambitious Slytherin. If you've ever wondered which Hogwarts House truly matches your personality, you've come to the right place. This quiz is designed to give you the most accurate result based on your unique traits, values, and decisions.")
    st.image("banner.png")

    answer1 = st.radio(
        "What wizarding background are you?",
        ["A", "B", "C"],
        format_func=lambda x: {
            "A": "Pure Blood",
            "B": "Muggle Born",
            "C": "Half Blood"
        }[x]
    )
    if answer1 == "A":
         blood_status= 2
    elif answer1 == "B":
         blood_status= 0
    else:
         blood_status= 2

    answer2 = st.radio(
        "A troll breaks into the castle while you're nearby. What do you do?",
        ["A", "B", "C", "D"],
        format_func=lambda x: {
            "A": "Charge in to stop it yourself.",
            "B": "Get help from a teacher.",
            "C": "Run away immediately.",
            "D": "Stay and protect others while waiting for help."
        }[x]
    )

    if answer2 == "A":
        bravery += 7
        dueling_skills += 2
    elif answer2 == "B":
        bravery += 4
        intelligence += 2
    elif answer2 == "C":
        bravery += 1
    else:
        bravery += 7
        loyalty += 2

    answer3 = st.radio(
        "You have an important exam tomorrow. What best describes your preparation?",
        ["A", "B", "C", "D"],
        format_func=lambda x: {
            "A": "I revise the basics.",
            "B": "I thoroughly research beyond the syllabus.",
            "C": "I don't study.",
            "D": "I create notes and practice questions."
        }[x]
    )

    if answer3 == "A":
        intelligence += 4
    elif answer3 == "B":
        intelligence += 10
        ambition += 2
    elif answer3 == "C":
        intelligence += 1
    else:
        intelligence += 7
        creativity += 2

    answer4 = st.radio(
        "Your friend is accused of something they didn't do. What do you do?",
        ["A", "B", "C", "D"],
        format_func=lambda x: {
            "A": "Speak up for them.",
            "B": "Stay out of it.",
            "C": "Stand by them no matter the consequences.",
            "D": "Support them privately."
        }[x]
    )

    if answer4 == "A":
        loyalty += 7
        bravery += 1
    elif answer4 == "B":
        loyalty += 1
    elif answer4 == "C":
        loyalty += 10
        bravery += 2
    else:
        loyalty += 4

    answer5 = st.radio(
        "You discover a chance to become Head Student.",
        ["A", "B", "C", "D"],
        format_func=lambda x: {
            "A": "I'd work hard to earn it.",
            "B": "I'm not interested.",
            "C": "I'd do everything possible to achieve it.",
            "D": "I'd consider it."
        }[x]
    )

    if answer5 == "A":
        ambition += 7
        intelligence += 2
    elif answer5 == "B":
        ambition += 1
    elif answer5 == "C":
        ambition += 10
        bravery += 2
    else:
        ambition += 4

    answer6 = st.radio(
        "How often do you study dangerous or forbidden magic?",
        ["A", "B", "C", "D"],
        format_func=lambda x: {
            "A": "Frequently because I find it fascinating.",
            "B": "Rarely.",
            "C": "Never.",
            "D": "Occasionally out of curiosity."
        }[x]
    )

    if answer6 == "A":
        dark_arts += 10
    elif answer6 == "B":
        dark_arts += 3
    elif answer6 == "C":
        dark_arts += 0
    else:
        dark_arts += 6

    answer7 = st.radio(
        "During Quidditch practice, how do you perform compared to most students?",
        ["A", "B", "C", "D"],
        format_func=lambda x: {
            "A": "I'm about average.",
            "B": "I struggle to stay on my broom.",
            "C": "I'm one of the best players.",
            "D": "I'm below average."
        }[x]
    )

    if answer7 == "A":
        quidditch_skills += 6
    elif answer7 == "B":
        quidditch_skills += 0
    elif answer7 == "C":
        quidditch_skills += 10
    else:
        quidditch_skills += 3

    answer8 = st.radio(
        "A fellow student challenges you to a duel.",
        ["A", "B", "C", "D"],
        format_func=lambda x: {
            "A": "I know a few spells.",
            "B": "I'd be confident of winning.",
            "C": "I'd probably lose badly.",
            "D": "I'd hold my own."
        }[x]
    )

    if answer8 == "A":
        dueling_skills += 4
    elif answer8 == "B":
        dueling_skills += 10
    elif answer8 == "C":
        dueling_skills += 1
    else:
        dueling_skills += 7

    answer9 = st.radio(
        "A professor asks you to solve a magical problem.",
        ["A", "B", "C", "D"],
        format_func=lambda x: {
            "A": "I create a completely original approach.",
            "B": "I follow the instructions exactly.",
            "C": "I think of an unusual solution.",
            "D": "I make small improvements."
        }[x]
    )

    if answer9 == "A":
        creativity += 10
        intelligence += 2
    elif answer9 == "B":
        creativity += 1
    elif answer9 == "C":
        creativity += 7
        intelligence += 1
    else:
        creativity += 4

    submitted = st.form_submit_button("Submit")


if submitted:
    new_student = [[blood_status, bravery, intelligence, loyalty, ambition, dark_arts, quidditch_skills, dueling_skills, creativity]]
    prediction = model.predict(new_student)
    house = house_names[prediction[0]]
    if house == 0:
        house = "Gryffindor, Founded in the 10th century by Godric Gryffindor. It values courage, bravery, and determination, symbolized by the lion and the element of fire. Notable alumni include Harry Potter and Albus Dumbledore"
        st.image("https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/1280w/products/88361/91122/Harry-Potter-Gryffindor-Crest-Official-wall-mounted-cardboard-cutout-buy-now-at-star__95823.1507640354.jpg?c=2")
    elif house == 1:
        house  = "Ravenclaw, Founded by Rowena Ravenclaw in the 10th century, Ravenclaw values wit, wisdom, and a love of learning. Its mascot is the eagle, representing the element of air, and the house colors are blue and bronze. The house ghost is the Grey Lady, Rowena's daughter Helena."
        st.image("https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/1280w/products/88363/91130/Harry-Potter-Ravenclaw-Crest-Official-wall-mounted-cardboard-cutout-buy-now-at-star__86173.1507642983.jpg?c=2")
    elif house == 2:
        house  = "Hufflepuff, Founded by the medieval Welsh witch Helga Hufflepuff, Hufflepuff is one of the four houses of Hogwarts School of Witchcraft and Wizardry. Uniquely inclusive, Helga Hufflepuff chose to accept and teach all magical students fairly rather than selecting for bravery, ambition, or intelligence. The house values hard work, patience, loyalty, and fair play."
        st.image("https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/1280w/products/88364/91134/Harry-Potter-Hufflepuff-Crest-Official-wall-mounted-cardboard-cutout-buy-now-at-star__21122.1507644096.jpg?c=2")
    else:
        house  = "Slytherin, Founded by Salazar Slytherin, one of the four legendary creators of Hogwarts School of Witchcraft and Wizardry, the House of Slytherin values ambition, cunning, and resourcefulness. Historically recognized by its emerald green and silver colors and serpent emblem, the house is famously located in the Slytherin Dungeons beneath the Black Lake."
        st.image("https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/1280w/products/88362/91127/Harry-Potter-Slytherin-Crest-Official-wall-mounted-cardboard-cutout-buy-now-at-star__31920.1507640618.jpg?c=2")
    st.success(f" You belong to {house}")

