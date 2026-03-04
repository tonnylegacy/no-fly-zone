import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config for that Mobile App feel
st.set_page_config(page_title="No-Fly Zone", page_icon="💸", layout="centered")

st.title("💸 No-Fly Zone")
st.subheader("Stop the leak, build the empire.")

# Simple Form
with st.form("entry_form", clear_on_submit=True):
    amount = st.number_input("Amount (GHS)", min_value=0.0, step=1.0)
    category = st.selectbox("Where did it go?", ["Food/Water", "Business/Tech", "Vibes/AJ", "Transport", "Family", "Crypto DCA"])
    note = st.text_input("Short description (e.g., 'Data bundle', 'Lunch')")
    
    submit = st.form_submit_button("Log Transaction")

    if submit:
        if amount > 0:
            st.success(f"✅ Logged {amount} GHS to {category}!")
            st.balloons() # Just for that 'app' feel
        else:
            st.warning("You can't log 0 GHS, bro. Be real!")

st.info("Next step: We'll connect this to a Google Sheet so your data actually saves!")
