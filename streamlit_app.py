import streamlit as st
from agents.symptom_agent import diagnose_symptoms
from agents.advice_agent import give_advice
from utils.helpers import generate_pdf

st.set_page_config(page_title="AI Healthcare Assistant", page_icon="🩺")

st.title("🩺 AI Healthcare Assistant")
st.write("Enter your symptoms below to get a likely diagnosis and lifestyle advice.")

symptoms = st.text_area("📝 Describe your symptoms:", height=200)

if st.button("Analyze"):
    if symptoms.strip() == "":
        st.warning("Please enter some symptoms to analyze.")
    else:
        with st.spinner("Analyzing your input..."):
            diagnosis = diagnose_symptoms(symptoms)
            advice = give_advice(diagnosis)

        st.subheader("🧠 Possible Condition:")
        st.success(diagnosis)

        st.subheader("💡 Suggested Lifestyle Advice:")
        st.info(advice)

        if st.button("📄 Download PDF Report"):
            pdf_path = generate_pdf(symptoms, diagnosis, advice)
            with open(pdf_path, "rb") as f:
                st.download_button("Download Report", f, file_name="healthcare_report.pdf")
