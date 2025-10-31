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

# The complete HTML code
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amaka's Universe of 22</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            overflow-x: hidden;
            background: #000;
            color: #fff;
        }

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
            font-size: 3.5rem;
            background: linear-gradient(135deg, #FFD700, #ffffff, #c8a8e9, #b695d6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
            text-align: center;
            animation: shimmer 3s infinite;
            font-weight: bold;
            letter-spacing: 3px;
        }

        .intro-subtitle {
            font-size: 2rem;
            color: #c8a8e9;
            margin-bottom: 3rem;
            text-align: center;
            animation: glow 2s infinite;
        }

        @keyframes shimmer {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.02); }
        }

        @keyframes glow {
            0%, 100% { text-shadow: 0 0 20px rgba(200, 168, 233, 0.5); }
            50% { text-shadow: 0 0 40px rgba(200, 168, 233, 0.8); }
        }

        .enter-btn {
            padding: 1.5rem 3.5rem;
            font-size: 1.3rem;
            background: linear-gradient(135deg, #c8a8e9, #b695d6, #FFD700);
            border: 2px solid #ffffff;
            border-radius: 50px;
            color: white;
            cursor: pointer;
            transition: all 0.4s;
            font-weight: bold;
            letter-spacing: 3px;
            text-transform: uppercase;
            box-shadow: 0 0 30px rgba(200, 168, 233, 0.6);
        }

        .enter-btn:hover {
            transform: scale(1.15) translateY(-5px);
            box-shadow: 0 0 50px rgba(255, 215, 0, 0.8);
            background: linear-gradient(135deg, #FFD700, #c8a8e9, #ffffff);
        }

        .universe-container {
            position: relative;
            width: 100%;
            min-height: 100vh;
            background: radial-gradient(ellipse at center, #2d1b4e 0%, #000000 100%);
            overflow: hidden;
        }

        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }

        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s infinite;
        }

        .star.gold {
            background: #FFD700;
        }

        .star.lilac {
            background: #c8a8e9;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.2; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.5); }
        }

        .content-wrapper {
            position: relative;
            z-index: 10;
            padding: 4rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .main-title {
            font-size: 4rem;
            text-align: center;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #FFD700, #ffffff, #c8a8e9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: float 4s ease-in-out infinite;
            font-weight: bold;
            letter-spacing: 2px;
        }

        .subtitle {
            text-align: center;
            font-size: 1.5rem;
            color: #c8a8e9;
            margin-bottom: 3rem;
            font-style: italic;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }

        .music-reminder {
            background: rgba(200, 168, 233, 0.2);
            border: 2px solid #c8a8e9;
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            margin-bottom: 3rem;
            backdrop-filter: blur(10px);
        }

        .music-reminder h3 {
            color: #FFD700;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .music-links {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 1rem;
        }

        .music-btn {
            padding: 1rem 2rem;
            background: linear-gradient(135deg, #c8a8e9, #FFD700);
            border: none;
            border-radius: 30px;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            text-decoration: none;
            display: inline-block;
        }

        .music-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.8);
        }

        .affirmation-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2.5rem;
            margin-top: 3rem;
        }

        .affirmation-card {
            background: linear-gradient(135deg, rgba(200, 168, 233, 0.15), rgba(255, 215, 0, 0.1));
            backdrop-filter: blur(15px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 25px;
            padding: 2.5rem;
            opacity: 0;
            transform: translateY(50px) rotateX(20deg);
            animation: slideUp 1s forwards;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(200, 168, 233, 0.3);
        }

        .affirmation-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, 
                transparent, 
                rgba(255, 215, 0, 0.2), 
                transparent,
                rgba(200, 168, 233, 0.2),
                transparent);
            animation: shine 4s infinite;
        }

        @keyframes shine {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes slideUp {
            to {
                opacity: 1;
                transform: translateY(0) rotateX(0);
            }
        }

        .card-number {
            font-size: 3.5rem;
            font-weight: bold;
            background: linear-gradient(135deg, #FFD700, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        }

        .card-text {
            font-size: 1.2rem;
            line-height: 1.9;
            color: #ffffff;
            position: relative;
            z-index: 1;
        }

        .icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            animation: bounce 2s infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .final-message {
            margin-top: 4rem;
            padding: 3rem;
            background: linear-gradient(135deg, rgba(200, 168, 233, 0.3), rgba(255, 215, 0, 0.2));
            border: 3px solid #FFD700;
            border-radius: 30px;
            text-align: center;
            backdrop-filter: blur(20px);
            box-shadow: 0 0 50px rgba(200, 168, 233, 0.5);
        }

        .final-message h2 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, #FFD700, #ffffff, #c8a8e9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1.5rem;
        }

        .final-message p {
            font-size: 1.4rem;
            line-height: 2;
            color: #ffffff;
        }

        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            .intro-title {
                font-size: 2rem;
            }
            .intro-subtitle {
                font-size: 1.5rem;
            }
            .affirmation-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="intro-screen" id="introScreen">
        <h1 class="intro-title">AMAKA AGIM JENNIFER</h1>
        <p class="intro-subtitle">✨ Welcome to Your Universe of 22 ✨</p>
        <button class="enter-btn" onclick="enterUniverse()">Open Your Universe</button>
    </div>

    <div class="universe-container" style="display: none;" id="universe">
        <div class="stars" id="starsContainer"></div>
        
        <div class="content-wrapper">
            <h1 class="main-title">🌟 AMAKA'S UNIVERSE OF 22 🌟</h1>
            <p class="subtitle">22 Affirmations for Your Beautiful Journey Ahead</p>

            <div class="music-reminder">
                <h3>🎵 First, Play "Hold On" by TEMS 🎵</h3>
                <p style="color: #ffffff; margin: 1rem 0;">Open one of these links in a new tab and let the music sweep you away...</p>
                <div class="music-links">
                    <a href="https://www.youtube.com/results?search_query=tems+gems" target="_blank" class="music-btn">
                        ▶️ Play on YouTube
                    </a>
                    <a href="https://open.spotify.com/search/tems%20gems" target="_blank" class="music-btn">
                        ▶️ Play on Spotify
                    </a>
                </div>
            </div>
            
            <div class="affirmation-grid" id="affirmationGrid"></div>

            <div class="final-message">
                <h2>✨ Happy 22nd Birthday, Amaka! ✨</h2>
                <p> You are a true girlfriend! From the moment you picked an interest in me from our little conversation on groundfloor at the Block Hostel and one time during Unserious, I knew I could give my heart out because you are A VERY GENUINE PERSON, not easy to come by.This is your year to shine brighter than ever. God has amazing things in store for you. Keep cooking up greatness, keep that beautiful smile glowing, and keep being the absolute gem that you are. 22 looks perfect on you! </p>
            </div>
        </div>
    </div>

    <script>
        const affirmations = [
            { icon: "👑", text: "Amaka, you are a queen, walking in grace and beauty every single day" },
            { icon: "✨", text: "Your smile lights up every room - it's absolutely beautiful and infectious" },
            { icon: "🙏", text: "God's favor surrounds you like a shield. His plans for you are perfect" },
            { icon: "👗", text: "Your style is impeccable - those shoes, bags, and wigs? Always on point!" },
            { icon: "🍳", text: "Your cooking feeds souls and brings pure joy to everyone who tastes it" },
            { icon: "🎵", text: "Like TEMS, your presence and energy command attention and respect" },
            { icon: "💎", text: "You are a rare gem in this world - irreplaceable and precious" },
            { icon: "🌟", text: "This year at 22, everything you touch will turn to gold" },
            { icon: "💪", text: "Your strength and resilience inspire everyone blessed to know you" },
            { icon: "❤️", text: "You deserve all the fine things in life - including those fine boys!" },
            { icon: "🌸", text: "Your beauty radiates from deep within and shines outward" },
            { icon: "📖", text: "Your faith will move mountains this year. Watch God work wonders" },
            { icon: "🎯", text: "Every goal you set, you WILL achieve. Success is yours" },
            { icon: "🌈", text: "Your future is bright, blessed, and overflowing with abundance" },
            { icon: "💫", text: "You are exactly where you need to be. Trust the journey" },
            { icon: "🦋", text: "Watch yourself transform into the woman you were destined to be" },
            { icon: "🌺", text: "Your presence is a precious gift to this world. Never forget that" },
            { icon: "🔥", text: "You are unstoppable, unbreakable, and absolutely unforgettable" },
            { icon: "🎨", text: "Your creativity and talent know absolutely no bounds" },
            { icon: "🌙", text: "Peace, joy, and divine favor follow you everywhere you go" },
            { icon: "⭐", text: "You are loved beyond measure by God and everyone around you" },
            { icon: "🎂", text: "22 looks absolutely STUNNING on you, Amaka! This is YOUR year!" }
        ];

        function createStars() {
            const container = document.getElementById('starsContainer');
            const colors = ['white', 'gold', 'lilac'];
            const sizes = [2, 3, 4];
            
            for (let i = 0; i < 250; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                const colorClass = colors[Math.floor(Math.random() * colors.length)];
                if (colorClass !== 'white') star.classList.add(colorClass);
                
                const size = sizes[Math.floor(Math.random() * sizes.length)];
                star.style.width = size + 'px';
                star.style.height = size + 'px';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 100 + '%';
                star.style.animationDelay = Math.random() * 3 + 's';
                star.style.animationDuration = (2 + Math.random() * 3) + 's';
                container.appendChild(star);
            }
        }

        function enterUniverse() {
            document.getElementById('introScreen').classList.add('hidden');
            document.getElementById('universe').style.display = 'block';
            
            setTimeout(() => {
                createStars();
                displayAffirmations();
            }, 500);
        }

        function displayAffirmations() {
            const grid = document.getElementById('affirmationGrid');
            affirmations.forEach((affirmation, index) => {
                setTimeout(() => {
                    const card = document.createElement('div');
                    card.className = 'affirmation-card';
                    card.style.animationDelay = (index * 0.15) + 's';
                    card.innerHTML = `
                        <div class="card-number">${index + 1}</div>
                        <div class="icon">${affirmation.icon}</div>
                        <div class="card-text">${affirmation.text}</div>
                    `;
                    grid.appendChild(card);
                }, index * 300);
            });
        }
    </script>
</body>
</html>
"""

# Display the HTML
components.html(html_code, height=800, scrolling=True)
