import streamlit as st
import random

st.set_page_config(page_title="I am Sorry Nishi Bubu. Be My Valentine My Mainu❤️", page_icon="❤️", layout="centered")

# --- Custom CSS for styling ---
st.markdown(
    """
    <style>
    .main {
        text-align: center;
    }
    .big-text {
        font-size: 40px;
        font-weight: bold;
        color: #ff4b6e;
        margin-bottom: 30px;
    }
    .footer {
        margin-top: 50px;
        font-size: 14px;
        color: grey;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='big-text'>Will You Be My Valentine? 💖</div>", unsafe_allow_html=True)

# Session state to control button movement
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

col1, col2 = st.columns(2)

with col1:
    if st.button("Yes 💘"):
        st.balloons()
        st.success("Yay!!! ❤️ You just made my day!")
        st.markdown("### 💍 Forever starts now 💞")

with col2:
    if st.button("No 😢"):
        st.session_state.no_clicks += 1
        responses = [
            "Are you sure? 🥺",
            "Think again... 💭",
            "I'll bring chocolates 🍫",
            "Pretty please? 💐",
            "Last chance! 😅"
        ]
        st.warning(random.choice(responses))

st.markdown("<div class='footer'>Made by Kushal with ❤️ using Streamlit</div>", unsafe_allow_html=True)
