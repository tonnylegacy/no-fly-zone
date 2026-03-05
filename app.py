import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# Page config for the mobile look
st.set_page_config(page_title="No-Fly Zone", page_icon="💸", layout="centered")

st.title("💸 No-Fly Zone")
st.subheader("Stop the leak, build the empire.")

# Establish Connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Form for data entry
with st.form("entry_form", clear_on_submit=True):
    amount = st.number_input("Amount (GHS)", min_value=0.0, step=1.0)
    category = st.selectbox("Where did it go?", [
        "Food/Water", 
        "Business/Tech", 
        "Vibes/AJ", 
        "Transport", 
        "Family Support", 
        "Crypto/Forex Invest"
    ])
    note = st.text_input("Short description (e.g., 'Data bundle')")
    
    submit = st.form_submit_button("Log Transaction")

    if submit:
        if amount > 0:
            # Read current data to append to it
            existing_data = conn.read(worksheet="Sheet1")
            
            # Create the new row
            new_row = pd.DataFrame([{
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Amount": amount,
                "Category": category,
                "Description": note
            }])
            
            # Update the Google Sheet
            updated_df = pd.concat([existing_data, new_row], ignore_index=True)
            conn.update(worksheet="Sheet1", data=updated_df)
            
            st.success(f"✅ {amount} GHS logged to {category}!")
            st.balloons()
        else:
            st.warning("You can't log 0 GHS, Tony. Stay sharp!")

# Show Recent History
st.divider()
st.subheader("Recent Activity")
try:
    data = conn.read(worksheet="Sheet1", ttl=5)
    st.dataframe(data.tail(5), use_container_width=True)
except:
    st.info("Log your first expense to see the history here!")
