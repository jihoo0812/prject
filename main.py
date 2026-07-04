import streamlit as st

st.set_page_config(page_title="나를 소개합니다", page_icon="👋", layout="centered")

# 기본 스타일 (style.css 대신 인라인으로 적용)
st.markdown("""
<style>
.profile-img {
    display: block;
    margin: 0 auto 1rem auto;
    border-radius: 50%;
    width: 150px;
}
header {
    text-align: center;
    margin-bottom: 2rem;
}
.subtitle {
    color: #666;
    font-size: 1.1rem;
}
section {
    margin-bottom: 1.5rem;
}
footer {
    text-align: center;
    color: #999;
    margin-top: 3rem;
    font-size: 0.85rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<header>
    <img src="https://via.placeholder.com/150" alt="프로필 사진" class="profile-img">
    <h1>안녕하세요, 전지후입니다 👋</h1>
    <p class="subtitle">새로운 도전을 즐기는 주니어 개발자</p>
</header>
""", unsafe_allow_html=True)

# About Me
st.markdown("""
<section class="about">
    <h2>About Me</h2>
    <p>컴퓨터 공학을 전공하고 있으며, 웹 기술을 통해 사람들의 문제를 해결하는 것에 관심이 많습니다. 최근에는 React와 Node.js를 깊게 공부하고 있습니다.</p>
</section>
""", unsafe_allow_html=True)

# Skills
st.markdown("""
<section class="skills">
    <h2>Skills</h2>
    <ul>
        <li>HTML / CSS / JavaScript</li>
        <li>Git & GitHub</li>
        <li>Python</li>
    </ul>
</section>
""", unsafe_allow_html=True)

# Contact
st.markdown("""
<section class="contact">
    <h2>Contact</h2>
    <p>📧 Email: email@example.com</p>
    <p>💻 GitHub: <a href="https://github.com/내아이디" target="_blank">github.com/내아이디</a></p>
</section>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer>
    <p>&copy; 2026 전지후. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)
