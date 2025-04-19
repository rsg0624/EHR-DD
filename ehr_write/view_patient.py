import streamlit as st
import json

def load_patient_data():
    with open("data/mock_patients.json", "r") as file:
        return json.load(file)

def render():
    st.header("Patient Overview")
    patient_id = st.text_input("Enter Patient ID")

    if not patient_id:
        return

    patients = load_patient_data()
    patient = next((p for p in patients if p["id"] == patient_id), None)

    if not patient:
        st.error("Patient not found.")
        return

    st.success(f"👤 {patient['name']} ({patient['age']} y/o, {patient['gender']})")

    # Chief Complaint
    st.subheader("📝 Chief Complaint")
    cc = st.session_state.get(f"{patient_id}_chief_complaint", None)
    if cc:
        st.markdown(f"> {cc}")
    else:
        st.info("Not recorded")

    # SOAP Notes
    st.subheader("🧪 SOAP Notes")
    soap = st.session_state.get(f"{patient_id}_soap", None)
    if soap:
        for key in ["Subjective", "Objective", "Assessment", "Plan"]:
            st.markdown(f"**{key}:**")
            st.markdown(f"> {soap.get(key, '')}")
    else:
        st.info("Not recorded")

    # Medications
    st.subheader("💊 Medication")
    meds = st.session_state.get(f"{patient_id}_meds", None)
    if meds:
        st.markdown(f"- **Medication**: {meds.get('Medication', '')}")
        st.markdown(f"- **Dosage**: {meds.get('Dosage', '')}")
        st.markdown(f"- **Frequency**: {meds.get('Frequency', '')}")
    else:
        st.info("Not recorded")

    # Referrals
    st.subheader("📋 Referral")
    ref = st.session_state.get(f"{patient_id}_referral", None)
    if ref:
        st.markdown(f"- **Specialist**: {ref.get('Specialist', '')}")
        st.markdown(f"- **Reason**: {ref.get('Reason', '')}")
    else:
        st.info("Not recorded")
