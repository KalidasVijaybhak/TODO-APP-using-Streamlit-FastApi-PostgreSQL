import streamlit as st
import requests

st.set_page_config(page_title="Manage Your Task", layout="wide")
st.title("Manage Your Task")

API_URL = "http://localhost:8000"

# Input form for name and deadline
with st.form(key='input_form'):
    name = st.text_input("Task name:")
    dx = st.date_input("Deadline", value=None)
    date = str(dx)
    submit_button = st.form_submit_button(label='Add Task')

if submit_button:
    if name and date:
        response = requests.post(f"{API_URL}/add_entry", json={"name": name, "date": date})
        if response.status_code == 200:
            st.success("Entry added successfully!")
        else:
            st.error("Failed to add entry")

colx1, colx2 = st.columns([3, 3])

with colx1:
    st.subheader("Task List 📄")
    response = requests.get(f"{API_URL}/get_entries")
    if response.status_code == 200:
        entries = response.json()
        
        for entry in entries:
            with st.container(border=True):
                col1, col2, col3 = st.columns([3, 0.5, 0.5])
                with col1:
                    st.write(f"{entry['name']}")
                    st.write(f"{entry['date']}")
                with col2:
                    if st.button('❌', key=f'delete_{entry["id"]}'):
                        delete_response = requests.delete(f"{API_URL}/delete_entry/{entry['id']}")
                        if delete_response.status_code == 200:
                            st.rerun()
                        else:
                            st.error("Failed to delete entry")
                with col3:
                    if st.button('✅', key=f'complete_{entry["id"]}'):
                        complete_response = requests.post(f"{API_URL}/complete_entry/{entry['id']}")
                        if complete_response.status_code == 200:
                            st.success("Task completed successfully!")
                            st.rerun()
                        else:
                            st.error(f"Failed to complete entry: {complete_response.text}")

with colx2:
    st.subheader("Completed Tasks ✅")
    response = requests.get(f"{API_URL}/get_completed_entries")
    if response.status_code == 200:
        completed_entries = response.json()
        for entry in completed_entries:
            with st.container(border=True):
                col1, col2 = st.columns([3, 0.5])
                with col1:
                    st.write(f"{entry['name']}")
                    st.write(f"{entry['date']}")    
                with col2:
                    if st.button('❌', key=f'delete_completed_{entry["id"]}'):
                        delete_response = requests.delete(f"{API_URL}/delete_completed_entry/{entry['id']}")
                        if delete_response.status_code == 200:
                            st.rerun()
                        else:
                            st.error("Failed to delete completed entry")