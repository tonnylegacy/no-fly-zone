import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="No-Fly Zone", page_icon="💸")
st.title("💸 No-Fly Zone")

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)

# Read existing data to show a summary (optional but cool)
existing_data = conn.read(worksheet="Sheet1", ttl=5) # ttl=5 means refresh every 5 seconds

with st.form("entry_form", clear_on_submit=True):
    amount = st.number_input("Amount (GHS)", min_value=0.0, step=1.0)
    category = st.selectbox("Where did it go?", ["Food/Water", "Business/Tech", "Vibes/AJ", "Transport", "Family", "Crypto DCA"])
    note = st.text_input("Short description")
    
    submit = st.form_submit_button("Log Transaction")

    if submit:
        if amount > 0:
            # Prepare the new row
            new_row = pd.DataFrame([{
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Amount": amount,
                "Category": category,
                "Description": note
            }])
            
            # Combine with existing data and update the sheet
            updated_df = pd.concat([existing_data, new_row], ignore_index=True)
            conn.update(worksheet="Sheet1", data=updated_df)
            
            st.success(f"✅ Logged {amount} GHS! Check your Google Sheet.")
            st.balloons()
        else:
            st.warning("Input a valid amount, bro.")

# Show the last 5 transactions so you know it's working
st.subheader("Recent Activity")
st.dataframe(existing_data.tail(5))
