import streamlit as st
from datetime import datetime, timedelta
import time

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Happy Birthday ❤️", page_icon="🎂", layout="centered")

# --------------------------------------------------
# CUSTOM CSS (Romantic Dark Theme + Animations)
# --------------------------------------------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }

    .main {
        text-align: center;
    }

    .title {
        font-size: 52px;
        font-weight: 800;
        background: linear-gradient(90deg, #ff4b6e, #ff9a9e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 22px;
        color: #f1f1f1;
        margin-bottom: 30px;
    }

    .countdown {
        font-size: 28px;
        margin: 20px 0;
        font-weight: bold;
        color: #ff9a9e;
    }

    .love-box {
        background: rgba(255, 255, 255, 0.08);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        margin-top: 30px;
        font-size: 20px;
        min-height: 120px;
    }

    /* Glowing Image Frame */
    .photo-frame img {
        border-radius: 20px;
        box-shadow: 0 0 30px rgba(255, 75, 110, 0.8);
    }

    /* Floating hearts animation */
    .heart {
        position: fixed;
        bottom: -10px;
        font-size: 22px;
        animation: floatUp 8s linear infinite;
        opacity: 0.7;
    }

    @keyframes floatUp {
        0% { transform: translateY(0); opacity: 0.7; }
        100% { transform: translateY(-110vh); opacity: 0; }
    }

    .footer {
        margin-top: 60px;
        font-size: 14px;
        color: #cccccc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# AUTOPLAY BACKGROUND MUSIC
# --------------------------------------------------
st.markdown(
    """
    <audio autoplay loop>
        <source src="https://www.bensound.com/bensound-music/bensound-romantic.mp3" type="audio/mpeg">
    </audio>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# FLOATING HEARTS
# --------------------------------------------------
for i in range(20):
    st.markdown(
        f"<div class='heart' style='left:{i*5}%; animation-delay:{i*0.4}s;'>❤️</div>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("<div class='title'>Happy Birthday My Love 🎂❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Tonight is all about you ✨</div>", unsafe_allow_html=True)

# --------------------------------------------------
# COUNTDOWN TO MIDNIGHT (LIVE REFRESH)
# --------------------------------------------------
placeholder_timer = st.empty()

now = datetime.now()
midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
remaining = midnight - now

hours, remainder = divmod(int(remaining.total_seconds()), 3600)
minutes, seconds = divmod(remainder, 60)

placeholder_timer.markdown(
    f"<div class='countdown'>⏳ Countdown to 12:00 AM: {hours:02d}:{minutes:02d}:{seconds:02d}</div>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# PHOTO SECTION (Backend Image)
# Put your image in project folder as: photo.jpg
# --------------------------------------------------
st.markdown("### 📸 Our Favorite Memory")
st.markdown("<div class='photo-frame'>", unsafe_allow_html=True)
st.image("photo.jpeg", use_column_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# TYPEWRITER EFFECT MESSAGE
# --------------------------------------------------
st.markdown("### 💌 A Message For You")

message = (
    "You are the most beautiful part of my life. "
    "Every smile of yours makes my world brighter. "
    "I am so grateful to celebrate you tonight. "
    "I promise to love you endlessly. "
    "Happy Birthday, my forever. ❤️"
)

placeholder = st.empty()
typed_text = ""

for char in message:
    typed_text += char
    placeholder.markdown(f"<div class='love-box'>{typed_text}</div>", unsafe_allow_html=True)
    time.sleep(0.03)

# --------------------------------------------------
# SURPRISE BUTTON
# --------------------------------------------------
if st.button("Click for a Surprise 💖"):
    st.balloons()
    st.success("You are my today and all of my tomorrows. 💍✨")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
current_year = datetime.now().year
st.markdown(f"<div class='footer'>Made with infinite love ❤️ | {current_year}</div>", unsafe_allow_html=True)
