import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Amaka's Universe of 22",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit branding
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Dreamy Universe HTML
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amaka's Universe of 22</title>

    <!-- Royal fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            overflow-x: hidden;
            background: #000;
            color: #fff;
        }

        h1, h2, .intro-title, .main-title {
            font-family: 'Playfair Display', serif;
            letter-spacing: 1.5px;
        }

        /* Intro screen */
        .intro-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            background: radial-gradient(ellipse at center, #2d1b4e 0%, #000000 100%);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            transition: opacity 1.5s ease;
        }

        .intro-screen.hidden {
            opacity: 0;
            pointer-events: none;
        }

        .intro-title {
            font-size: 3.2rem;
            background: linear-gradient(135deg, #FFD700, #ffffff, #c8a8e9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            animation: shimmer 3s infinite;
            font-weight: 700;
            text-transform: uppercase;
        }

        .intro-subtitle {
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            color: #c8a8e9;
            margin-bottom: 3rem;
            text-align: center;
            animation: glow 2s infinite;
            font-style: italic;
        }

        @keyframes shimmer {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.9; transform: scale(1.03); }
        }

        @keyframes glow {
            0%, 100% { text-shadow: 0 0 20px rgba(200,168,233,0.5); }
            50% { text-shadow: 0 0 40px rgba(200,168,233,0.9); }
        }

        .enter-btn {
            padding: 1.2rem 2.8rem;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #c8a8e9, #FFD700);
            border: 2px solid #fff;
            border-radius: 50px;
            color: white;
            cursor: pointer;
            transition: all 0.4s ease;
            font-weight: bold;
            text-transform: uppercase;
            box-shadow: 0 0 25px rgba(200,168,233,0.6);
        }

        .enter-btn:hover {
            transform: scale(1.1) translateY(-4px);
            box-shadow: 0 0 40px rgba(255,215,0,0.8);
        }

        /* Universe */
        .universe-container {
            width: 100%;
            min-height: 100vh;
            background: radial-gradient(ellipse at center, #2d1b4e 0%, #000000 100%);
            overflow: hidden;
        }

        .stars {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            pointer-events: none;
        }

        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.3; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.5); }
        }

        .content-wrapper {
            position: relative;
            z-index: 10;
            padding: 3rem 1.5rem;
            max-width: 1100px;
            margin: auto;
        }

        .main-title {
            font-size: 3rem;
            text-align: center;
            background: linear-gradient(135deg, #FFD700, #ffffff, #c8a8e9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            animation: float 4s ease-in-out infinite;
            font-weight: 700;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }

        .subtitle {
            text-align: center;
            font-size: 1.3rem;
            color: #c8a8e9;
            font-style: italic;
            margin-bottom: 2rem;
        }

        /* Affirmation Cards */
        .affirmation-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .affirmation-card {
            background: linear-gradient(145deg, rgba(200,168,233,0.15), rgba(255,215,0,0.1));
            border: 1.5px solid rgba(255,255,255,0.3);
            border-radius: 25px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(200,168,233,0.25);
            text-align: center;
            backdrop-filter: blur(12px);
            transition: all 0.4s ease;
            animation: fadeIn 1s ease forwards;
        }

        .affirmation-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 0 40px rgba(255,215,0,0.4);
            border-color: rgba(255,215,0,0.6);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .card-number {
            font-size: 2rem;
            font-weight: bold;
            color: #FFD700;
            margin-bottom: 0.5rem;
        }

        .icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        .card-text {
            font-family: 'Playfair Display', serif;
            font-size: 1.1rem;
            color: #fff;
            line-height: 1.7;
        }

        .final-message {
            margin-top: 3rem;
            padding: 2rem;
            background: linear-gradient(135deg, rgba(200,168,233,0.2), rgba(255,215,0,0.15));
            border-radius: 25px;
            text-align: center;
            border: 2px solid rgba(255,215,0,0.5);
        }

        .final-message h2 {
            font-family: 'Playfair Display', serif;
            background: linear-gradient(135deg, #FFD700, #ffffff, #c8a8e9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2rem;
            margin-bottom: 1rem;
        }

        .final-message p {
            font-size: 1.1rem;
            color: #fff;
            line-height: 1.8;
        }

        @media (max-width: 768px) {
            .main-title { font-size: 2rem; }
            .intro-title { font-size: 2rem; }
            .affirmation-card { padding: 1.5rem; }
            .card-text { font-size: 1rem; }
        }
    </style>
</head>
<body>
    <div class="intro-screen" id="introScreen">
        <h1 class="intro-title">AMAKA AGIM JENNIFER</h1>
        <p class="intro-subtitle">✨ Welcome to Your Universe of 22 ✨</p>
        <button class="enter-btn" onclick="enterUniverse()">Open Your Universe</button>
    </div>

    <div class="universe-container" style="display:none;" id="universe">
        <div class="stars" id="starsContainer"></div>

        <div class="content-wrapper">
            <h1 class="main-title">🌟 Amaka’s Universe of 22 🌟</h1>
            <p class="subtitle">22 Affirmations for Your Beautiful Journey Ahead</p>

            <div class="affirmation-grid" id="affirmationGrid"></div>

            <div class="final-message">
                <h2>✨ Happy 22nd Birthday, Amaka! ✨</h2>
                <p>You are a true girlfriend! From the moment you picked an interest in me from our little conversation on groundfloor at the Block Hostel and one time during Unserious, I knew I could give my heart out because you are A VERY GENUINE PERSON, not easy to come by. This is your year to shine brighter than ever. God has amazing things in store for you. Keep cooking up greatness, keep that beautiful smile glowing, and keep being the absolute gem that you are. 22 looks perfect on you! 💜</p>
            </div>
        </div>
    </div>

    <script>
        const affirmations = [
            { icon: "👑", text: "Amaka, you are a queen, walking in grace and beauty every single day" },
            { icon: "✨", text: "Your smile lights up every room - it's absolutely beautiful and infectious" },
            { icon: "🙏", text: "God's favor surrounds you like a shield. His plans for you are perfect" },
            { icon: "💎", text: "You are a rare gem in this world - irreplaceable and precious" },
            { icon: "🌟", text: "This year at 22, everything you touch will turn to gold" },
            { icon: "💪", text: "Your strength and resilience inspire everyone blessed to know you" },
            { icon: "❤️", text: "You deserve all the fine things in life - including a FINE man both in beauty and character!" },
            { icon: "🌸", text: "Your beauty radiates from deep within and shines outward" },
            { icon: "📖", text: "Your faith will move mountains this year. Watch God work wonders" },
            { icon: "🎯", text: "Every goal you set, you WILL achieve. Success is yours" },
            { icon: "🌈", text: "Your future is bright, blessed, and overflowing with abundance" },
            { icon: "💫", text: "You are exactly where you need to be. Trust the journey" },
            { icon: "🦋", text: "Watch yourself transform into the woman you were destined to be" },
            { icon: "🌺", text: "Your presence is a precious gift to this world. Never forget that" },
            { icon: "🔥", text: "You are unstoppable, unbreakable, and unforgettable" },
            { icon: "🎨", text: "Your creativity and talent know absolutely no bounds" },
            { icon: "🌙", text: "Peace, joy, and divine favor follow you everywhere you go" },
            { icon: "⭐", text: "You are loved beyond measure by God" },
            { icon: "🎂", text: "22 looks absolutely STUNNING on you, Amaka! This is YOUR year!" }
        ];

        function createStars() {
            const container = document.getElementById('starsContainer');
            for (let i = 0; i < 200; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                const size = Math.random() * 3 + 1;
                star.style.width = star.style.height = size + 'px';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 100 + '%';
                star.style.animationDelay = Math.random() * 2 + 's';
                container.appendChild(star);
            }
        }

        function enterUniverse() {
            document.getElementById('introScreen').classList.add('hidden');
            document.getElementById('universe').style.display = 'block';
            setTimeout(() => {
                createStars();
                displayAffirmations();
            }, 600);
        }

        function displayAffirmations() {
            const grid = document.getElementById('affirmationGrid');
            affirmations.forEach((a, i) => {
                setTimeout(() => {
                    const card = document.createElement('div');
                    card.className = 'affirmation-card';
                    card.innerHTML = `
                        <div class="card-number">${i + 1}</div>
                        <div class="icon">${a.icon}</div>
                        <div class="card-text">${a.text}</div>
                    `;
                    grid.appendChild(card);
                }, i * 200);
            });
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=1000, scrolling=True)
