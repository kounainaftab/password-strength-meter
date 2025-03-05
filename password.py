#🔐 Project 02: Password Strength Meter
#📌 Objective
#Build a Password Strength Meter in Python that evaluates a user's password based on security rules. The program will:

#Analyze passwords based on length, character types, and patterns.
#Assign a strength score (Weak, Moderate, Strong).
#Provide feedback to improve weak passwords.
#Use control flow, type casting, strings, and functions.
#🔹 Requirements
#1. Password Strength Criteria
# strong password should:
#✅ Be at least 8 characters long
#✅ Contain uppercase & lowercase letters
#✅ Include at least one digit (0-9)
#✅ Have one special character (!@#$%^&*)

#2. Scoring System
#Weak (Score: 1-2) → Short, missing key elements
#Moderate (Score: 3-4) → Good but missing some security features
#Strong (Score: 5) → Meets all criteria
#3. Feedback System
#If the password is weak, suggest improvements.
#If the password is strong, display a success message.
#🔹 Additional Challenges
#Password Generator: Add a feature to suggest a strong password.
#User-Friendly Interface: Use Streamlit for a GUI version.
#Blacklist Common Passwords: Reject weak passwords like "password123".
#Custom Scoring Weights: Give different weights to complexity factors.
#🔹 Why This Assignment?
#✅ Uses Control Flow & Conditions
#✅ Applies String Manipulation & Regex
#✅ Teaches Security Best Practices
#✅ Prepares for Real-World Applications

#💡 Challenge yourself to build a better, more secure password checker!

import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Kounain Aftab", page_icon="🌘", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px; }
    .stButton button:hover { background-color: red; color:white; }
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔑 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1  # Increased score by 1
    else:
        feedback.append("❌ Password should be *at least 8 characters long*.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include *both uppercase (A-Z) and lowercase (a-z) letters*.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include *at least one number (0-9).*")

    # Special characters check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include *at least one special character (!@#$%^&).")

    return score, feedback

# User input
password = st.text_input("🔑 Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    # Strength message
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠ Moderate Password! Try adding more complexity.")
    else:
        st.error("❌ Weak Password! Improve your password strength.")
    
    
    for msg in feedback:
        st.write(msg)
