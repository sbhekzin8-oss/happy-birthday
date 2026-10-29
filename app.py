import streamlit as st
from urllib.parse import quote

# ============================================================
# CONFIGURATION — CHANGE THIS TO YOUR WHATSAPP NUMBER
# South Africa example: 27821234567 (no +, no leading 0)
# ============================================================
WHATSAPP_NUMBER = "27716424244"

st.set_page_config(
    page_title="Martha Kekane (nana0 | Belated Birthday",
    page_icon="🎂",
    layout="centered",
)

# ---------------------- Styling -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Playfair+Display:wght@600;700&display=swap');

    .stApp {
        background: linear-gradient(140deg, #251522 0%, #302033 48%, #20243b 100%);
        color: #f8edf4;
    }
    [data-testid="stHeader"] { background: rgba(37,21,34,.85); }
    [data-testid="stSidebar"] { background: #251522; }
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #f4b8d0;
    }
    p, label, div, span {
        font-family: 'DM Sans', sans-serif;
    }
    .hero {
        padding: 1.5rem 1rem;
        border-radius: 24px;
        background: rgba(61,39,58,.92);
        border: 1px solid #87516d;
        text-align: center;
        box-shadow: 0 10px 35px rgba(0,0,0,.25);
    }
    .hero p { color: #e7cbd9; }
    [data-testid="stMarkdownContainer"] p { color: #f3e5ed; }
    [data-testid="stWidgetLabel"] p { color: #f4dbe7 !important; }
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    div[data-baseweb="textarea"] > div {
        background: #38283a;
        color: #fff4fa;
        border-color: #87516d;
    }
    input, textarea { color: #fff4fa !important; }
    div[data-testid="stAlert"] { background: #3b2a40; color: #fff4fa; }
    .stButton > button, .stLinkButton > a, .stFormSubmitButton > button {
        border-radius: 16px;
        min-height: 3rem;
        font-weight: 700;
        border: 1px solid #9c6683; background: #50334b; color: #fff4fa;
    }
    div[data-testid="stForm"] {
        background: rgba(55,36,54,.92);
        padding: 1rem;
        border-radius: 18px;
        border: 1px solid #87516d;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------- Session state -----------------------
defaults = {
    "celebrated": None,
    "game_invite": None,
    "game": None,
    "show_birthday_blessing": False,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------------------- Welcome -----------------------------
st.markdown(
    """
    <div class="hero">
        <div style="font-size:3rem;">🎂 🌷 ✨ 🎁</div>
        <h1>A Little Late, A Lot of Love</h1>
        <h3>For Marthe Kekane 💗</h3>
        <p>Some celebrations arrive late, but the love behind them is right on time.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

# ---------------------- Birthday letter ---------------------
st.markdown("## 💌 A Belated Birthday Letter")
st.markdown(
    """
    **Dear Martha (nana),**

    Happy belated birthday! 🥳💐

    I’m sorry this birthday wish is arriving a little late, but I hope your special
    day brought you peace, laughter, love, and beautiful memories. You deserve to
    be celebrated—not only on your birthday, but throughout the whole year.

    May God guide your steps, strengthen you when life feels difficult, fill your
    heart with joy, and bless you with wisdom, good health, meaningful friendships,
    and opportunities that make you smile. May this new chapter bring you closer
    to your dreams and remind you how special and appreciated you are.

    I hope you felt loved on your special day. And if the celebrations were quiet,
    let this little corner of the internet be an extra celebration just for you. 🌸

    **With warm wishes and lots of love,**  
    *Your belated birthday well-wisher* 💗
    """
)

st.divider()

# ---------------------- Birthday question -------------------
st.markdown("## 🎉 One Little Question...")
st.markdown("**Marthe, did you get to celebrate your birthday?**")

yes_col, no_col = st.columns(2)
with yes_col:
    if st.button("YES! I celebrated 🎊", use_container_width=True, key="yes_bday"):
        st.session_state.celebrated = "Yes"
with no_col:
    if st.button("Not really 😔", use_container_width=True, key="no_bday"):
        st.session_state.celebrated = "No"

if st.session_state.celebrated == "Yes":
    st.success("Yaaay! 🎉 I hope it was full of beautiful moments. You deserve every bit of happiness!")
    st.balloons()
elif st.session_state.celebrated == "No":
    st.info("Then this celebration is officially for you! 💗 No escaping the birthday love, Marthe 😄")
    st.markdown("### 🎁 Your birthday mission")
    blessing_choice = st.selectbox(
        "Choose your birthday gift:",
        [
            "A prayer for a joyful year 🙏",
            "A reminder of how loved you are 💗",
            "A cheerful birthday challenge 🎉",
        ],
    )
    blessings = {
        "A prayer for a joyful year 🙏":
            "May God bless you and protect you, give you peace, and guide you in the year ahead. (Numbers 6:24–26)",
        "A reminder of how loved you are 💗":
            "You are wonderfully made, and your life has value and purpose. (Psalm 139:14)",
        "A cheerful birthday challenge 🎉":
            "Smile, name three things you are grateful for, and do one kind thing for yourself today. 🌷",
    }
    st.success(blessings[blessing_choice])
    st.caption("P.S. The birthday love cannot be cancelled. You have been lovingly caught! 🎀")

st.divider()

# ---------------------- Games invitation --------------------
st.markdown("## 🕵️‍♀️ Want to Play a Little Game?")
st.write("Would you like to try a fun Bible-themed birthday game?")

play_col, later_col = st.columns(2)
with play_col:
    if st.button("YES, let's play! 🎮", use_container_width=True, key="play_yes"):
        st.session_state.game_invite = "Yes"
with later_col:
    if st.button("Maybe later 🌷", use_container_width=True, key="play_later"):
        st.session_state.game_invite = "Later"

if st.session_state.game_invite == "Later":
    st.write("No pressure, Marthe. The games will be waiting whenever you're ready. 💗")

elif st.session_state.game_invite == "Yes":
    st.markdown("### Choose Your Game")
    game_choice = st.radio(
        "Pick a game:",
        [
            "🔎 Bible Hide-and-Seek: Guess the Person",
            "📖 Finish the Bible Moment",
            "🎂 Birthday Bible Quiz",
        ],
        key="game_choice",
    )

    if st.button("Start my game ✨", use_container_width=True, key="start_game"):
        st.session_state.game = game_choice

    # Bible Hide-and-Seek
    if st.session_state.game == "🔎 Bible Hide-and-Seek: Guess the Person":
        st.markdown("#### 🔎 Bible Hide-and-Seek")
        st.write("A Bible person is hiding behind these clues. Can you guess who it is?")
        mystery = st.selectbox("Choose a mystery:", ["Mystery 1", "Mystery 2", "Mystery 3"])

        mysteries = {
            "Mystery 1": (
                "I built a huge ark because God warned me about a flood. Who am I?",
                ["Ham", "Moses", "Peter", "David"],
                "Noah",
                "Genesis 6–9",
            ),
            "Mystery 2": (
                "I was brave, faced a giant, and used a sling and a stone. Who am I?",
                ["Samson", "Bra D", "Joseph", "Joshua"],
                "David",
                "1 Samuel 17",
            ),
            "Mystery 3": (
                "I spent time inside a great fish. Who am I?",
                [" Bra Jonah", "bra Daniel", "bra Elijah", "uncle Paul"],
                "Jonah",
                "Jonah 1–2",
            ),
        }
        question, options, answer, reference = mysteries[mystery]
        st.write(question)
        guess = st.radio("Your guess:", options, key="hide_guess")

        if st.button("Reveal the answer 🔍", key="reveal_hide"):
            if guess == answer:
                st.success(f"Correct! 🎉 It was {answer}. Read {reference} for the story.")
            else:
                st.warning(f"Good try! The answer is **{answer}**. Read {reference} to discover the story.")

    # Finish the Bible moment
    elif st.session_state.game == "📖 Finish the Bible Moment":
        st.markdown("#### 📖 Finish the Bible Moment")
        question = st.selectbox(
            "Choose a question:",
            [
                "What did David use against Goliath?",
                "Who was swallowed by a great fish?",
                "Who led the Israelites out of Egypt?",
            ],
        )
        question_data = {
            "What did David use against Goliath?": (
                ["A sling and a stone", "A sword from an angel", "A bow and arrow"],
                "A sling and a stone",
                "1 Samuel 17:49",
            ),
            "Who was swallowed by a great fish?": (
                ["Jonah", "Noah", "Job"],
                "Jonah",
                "Jonah 1:17",
            ),
            "Who led the Israelites out of Egypt?": (
                ["Moses", "Solomon", "Andrew"],
                "Moses",
                "Exodus 3–14",
            ),
        }
        options, answer, reference = question_data[question]
        guess = st.radio("Your answer:", options, key="finish_guess")

        if st.button("Check my answer 🌟", key="check_finish"):
            if guess == answer:
                st.success(f"That's right! 🌟 You can read more in {reference}.")
            else:
                st.info(f"Good try! The answer is **{answer}**. You can read {reference}.")

    # Birthday Bible quiz
    elif st.session_state.game == "🎂 Birthday Bible Quiz":
        st.markdown("#### 🎂 Birthday Bible Quiz")
        st.write("Three quick questions for the birthday star!")
        quiz = [
            ("Who was known for great strength?", ["Samson", "Zacchaeus", "Timothy"], "Samson"),
            ("Where was Jesus born?", ["Bethlehem", "Jerusalem", "Nazareth"], "Bethlehem"),
            ("Who climbed a tree to see Jesus?", ["Zacchaeus", "Lazarus", "Thomas"], "Zacchaeus"),
        ]
        answers = []
        for i, (question, options, _answer) in enumerate(quiz):
            st.write(f"**{i + 1}. {question}**")
            answers.append(st.radio(f"Question {i + 1}", options, key=f"quiz_{i}", horizontal=True))

        if st.button("Mark my birthday quiz 🎂", key="mark_quiz"):
            score = sum(answers[i] == quiz[i][2] for i in range(len(quiz)))
            st.success(f"You scored {score}/3, birthday star! 🎉 Every day is a chance to learn something new.")

st.divider()

# ---------------------- Feedback + WhatsApp -----------------
st.markdown("## 💬 Tell Me How You Enjoyed It")
st.write("Your feedback helps make this little birthday surprise even better.")

with st.form("feedback_form"):
    enjoyment = st.select_slider(
        "How much did you enjoy this birthday surprise?",
        options=["Not much", "It was okay", "I liked it", "Loved it! 💗"],
    )
    favourite = st.selectbox(
        "What was your favourite part?",
        [
            "The birthday letter 💌",
            "The birthday blessing 🙏",
            "Bible Hide-and-Seek 🔎",
            "Bible quiz 📖",
            "The whole surprise 🎉",
        ],
    )
    message = st.text_area("Leave a message (optional):", placeholder="Write your feedback here...")
    submit_feedback = st.form_submit_button("Prepare my feedback 💌", use_container_width=True)

if submit_feedback:
    feedback_text = (
        "Marthe Kekane's Belated Birthday Surprise Feedback 🎂\n"
        f"Enjoyment: {enjoyment}\n"
        f"Favourite part: {favourite}\n"
        f"Message: {message.strip() if message.strip() else 'No extra message'}"
    )

    if not WHATSAPP_NUMBER or WHATSAPP_NUMBER == "27821234567":
        st.warning(
            "Remember to replace the example WhatsApp number near the top of app.py "
            "with your own number before sharing the app."
        )

    whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(feedback_text)}"
    st.success("Your feedback is ready. Tap the button below to open WhatsApp.")
    st.link_button(
        "Send feedback to me on WhatsApp 📲",
        whatsapp_url,
        use_container_width=True,
    )
    st.caption(
        "WhatsApp opens with the message addressed to the configured number. "
        "The sender must tap Send; this page does not silently send messages."
    )

st.markdown(
    "<p style='text-align:center;color:#775b68;'>Made with warmth, faith, and birthday confetti 🌷</p>",
    unsafe_allow_html=True,
)
