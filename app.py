import re 
import streamlit as st

#style 
st.set_page_config(page_title= "-PASSWORD STRENGTH METER-", page_icon="⚙️", layout= "centered")
#css
st.markdown("""
<style>
    .main {text-align = center;}
    .stTextInput {width = 65% !important; margin: auto;}
    .stButton button {width:55%; background-color #ffa3ae; color: white; font-size: 15px;}
    .stButton button:hover { background-colour: #e86992;}
</style>
""", unsafe_allow_html=True)

st.title("Password Strength Generator 💻")
st.write("Enter your password to check the security level")

def check_strength(password):
    score= 0 
    feedback =[]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❗ Password must be 8 characters long ❗")
    if re.search(r"[A-Z]", password)and re.search(r"[a-z]", password):
        score +=1
    else:
        feedback.append("❗ password should include uppercase and lowercase ❗")
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else: 
        feedback.append("❗Password atleat have one sepecial character ❗")

    if score == 3:
        st.success("Your Password is secure 👍🏻")
    elif score == 2:
        st.info("Moderate Password ⚠️")
    else:
        st.error("❌ Weak Password ❌")
    
    if feedback:
        with st.expander("Improve Your Password"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password:", type="password",help="Ensure your password is strong 🛡️")

if st.button("Check strength"):
    if password:
        check_strength(password)
    else:
        st.warning("⚠️ Please enter the password ")
