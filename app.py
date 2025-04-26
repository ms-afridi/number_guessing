import streamlit as st
import random

# Setting page config
st.set_page_config(page_title="🎯 Number Guessing Game", page_icon="🎯", layout="centered")

# Adding custom CSS for a better look
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .attempts-box {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Game title and subtitle
st.markdown('<div class="title">🎯 Guess The Secret Number!</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Can you find the secret number between 1 and 100?</div>', unsafe_allow_html=True)

# Initialize secret number and attempts in session state
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = []

# Funny responses
funny_replies = {
    "too_low": [
        "Too low! Go higher! 🚀",
        "Not quite. Try a bigger number! 📈",
        "Low guess! Reach for the stars! 🌟",
    ],
    "too_high": [
        "Too high! Lower it down! 🌊",
        "Almost there! Think smaller! 🐜",
        "Woah! That's high! Bring it back! 🛬",
    ],
    "correct": [
        "Spot on! You're a legend! 🏆",
        "Bingo! You nailed it! 🎯",
        "Correct! You're unstoppable! 🚀",
    ]
}

# User input section
guess = st.number_input("Enter your guess 👇", min_value=1, max_value=100, step=1)

# Buttons for actions
col1, col2 = st.columns(2)

with col1:
    if st.button("🎯 Submit Guess"):
        if guess < st.session_state.secret_number:
            st.session_state.attempts.append(guess)
            st.error(f"Wrong Guess: {random.choice(funny_replies['too_low'])}")
        elif guess > st.session_state.secret_number:
            st.session_state.attempts.append(guess)
            st.error(f"Wrong Guess: {random.choice(funny_replies['too_high'])}")
        else:
            st.session_state.attempts.append(guess)
            st.success(f"{random.choice(funny_replies['correct'])}")
            st.balloons()
            st.info(f"Secret Number was: **{st.session_state.secret_number}**")
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = []

with col2:
    if st.button("🔄 Reset Game"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = []
        st.success("Game has been reset! Guess again!")

# Show previous attempts
if st.session_state.attempts:
    st.markdown('<div class="attempts-box">', unsafe_allow_html=True)
    st.subheader("📜 Your Attempts:")
    st.write(st.session_state.attempts)
    st.markdown('</div>', unsafe_allow_html=True)
