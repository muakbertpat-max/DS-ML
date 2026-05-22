import streamlit as st

st.set_page_config(
    page_title="Boot Camp DS & ML",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
    color: #1f2937;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #374151;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0px 15px 35px rgba(0,0,0,0.12);
}

.card-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 10px;
}

.card-desc {
    font-size: 16px;
    color: #6b7280;
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<div class='main-title'>🚀 Boot Camp: Data Science & Machine Learning</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>7 Day Intensive Hands-on Workshop</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.info("📘 **Day 1:** การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

# ---------- Cards ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">💰 Discount Calculator</div>
        <div class="card-desc">
            คำนวณส่วนลดตามยอดซื้อ<br>
            ฝึก Logic & Condition
        </div>
    """, unsafe_allow_html=True)
    if st.button("เข้าใช้งาน 💰"):
        st.switch_page("pages/app1_discount_calc.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🧹 Data Cleaning</div>
        <div class="card-desc">
            ล้างข้อมูล Missing / Duplicate<br>
            พื้นฐานที่ Data Scientist ต้องรู้
        </div>
    """, unsafe_allow_html=True)
    if st.button("เข้าใช้งาน 🧹"):
        st.switch_page("pages/clean_app_muak.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">📊 Data Analysis</div>
        <div class="card-desc">
            ทำความสะอาด + วิเคราะห์ข้อมูล<br>
            พร้อม Insight เบื้องต้น
        </div>
    """, unsafe_allow_html=True)
    if st.button("เข้าใช้งาน 📊"):
        st.switch_page("pages/clean_customers.py")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><center>👨‍💻 Happy Coding | Learn by Doing</center>", unsafe_allow_html=True)
``
