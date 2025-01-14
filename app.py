
import streamlit as st
from myexperience.fileoperation import read, write, append
from myexperience.db.db_operations import select, inserttodb

st.title("File and Database Operations")

# File operations
st.subheader("File Operations")
filepath = st.text_input("Filepath")
content = st.text_area("Content")
if st.button("Write to File"):
    write(filepath, content)
    st.success("File written successfully!")

# Database operations
st.subheader("Database Operations")
query = st.text_area("SQL Query")
if st.button("Execute Query"):
    try:
        if query.strip().upper().startswith("SELECT"):
            result = select(query)
            st.write(result)
        else:
            inserttodb(query)
            st.success("Query executed successfully!")
    except Exception as e:
        st.error(f"Error: {e}")
