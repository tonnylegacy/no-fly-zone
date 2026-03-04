import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="No-Fly Zone Debug", page_icon="💸")
st.title("💸 No-Fly Zone: Debug Mode")

# --- DEBUG SECTION ---
with st.expander("🔍 Connection Debugger"):
    try:
        secret_url = st.secrets["connections"]["gsheets"]["spreadsheet"]
        st.write(f"✅ Secret URL found: `{secret_url}`")
    except Exception as e:
        st.error(f"❌ Could not find the Secret URL. Error: {e}")
# ---------------------

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    existing_data = conn.read(worksheet="Sheet1", ttl=5)
    st.success("✅ Connection Successful! The bridge is open.")
    st.dataframe(existing_data)
except Exception as e:
    st.error("❌ Still can't reach the Google Sheet.")
    st.info("Check if your tab name is exactly 'Sheet1' and the link in Secrets is correct.")
    st.exception(e) # This will show the full error for us to analyze
