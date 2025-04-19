import streamlit as st
import json

def load_patient_data():
    with open("data/mock_patients.json", "r") as file:
        return json.load(file)

def render():
    st.header("Write Chief Complaints")
    patient_id = st.text_input("Patient ID")
    if patient_id:
        patients = load_patient_data()
        patient = next((p for p in patients if p["id"] == patient_id), None)
        if patient:
            st.success(f"Patient Found: {patient['name']} ({patient['age']} y/o, {patient['gender']})")
            complaint = st.text_area("Chief Complaint")
            if st.button("Submit Complaint"):
                st.session_state[f"{patient_id}_chief_complaint"] = complaint
                st.success(f"Complaint for {patient['name']} submitted.")
        else:
            st.error("Patient ID not found.")