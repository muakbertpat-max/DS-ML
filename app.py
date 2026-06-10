import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.markdown(''':rainbow[Muakbert] ''')

st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("😁การทำความสะอาด"):
    st.switch_page("pages/clean_app_muak.py")
elif st.button("😘การทำความสะอาดและวิเคราะห์ข้อมูล"):
    st.switch_page("pages/clean_customers.py")    
elif st.button("😁การแปลงข้อมูล"):
    st.switch_page("pages/transform_app.py")
elif st.button("😁การวิเคราะห์ข้อมูลเชิงสำรวจ"):
    st.switch_page("pages/EDA_app.py")
elif st.button("😁clustering segment"):
    st.switch_page("pages/clustering_segment.py")
elif st.button("😁association items"):
    st.switch_page("pages/association_itemst.py")
