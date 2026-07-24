import streamlit as st
import pandas as pd

from src.doc_reader import read_docx
from src.pii_detector import detect_pii
from src.presidio_detector import detect_pii_presidio
from src.anonymizer import anonymize_text
from src.doc_writer import create_redacted_doc
from src.evaluation import get_metrics

st.set_page_config(
    page_title="PII Redaction Tool",
    page_icon="🔒",
    layout="wide"
)

st.title("🔒 PII Redaction Tool")

st.write(
    "Upload a DOCX file to detect and anonymize Personally Identifiable Information (PII)."
)

uploaded_file = st.file_uploader(
    "Choose a DOCX file",
    type=["docx"]
)


if uploaded_file is not None:

    # ---------------- READ DOCUMENT ----------------

    text = read_docx(uploaded_file)

    # ---------------- DETECT PII ----------------

    pii = detect_pii(text)

    presidio_results = detect_pii_presidio(text)

    # ---------------- ANONYMIZE ----------------

    redacted_text, replacements = anonymize_text(
        text,
        presidio_results
    )

    # ---------------- CREATE REDACTED DOCX ----------------

    uploaded_file.seek(0)

    redacted_doc = create_redacted_doc(
        uploaded_file,
        replacements
    )

    # ---------------- STATISTICS ----------------

    entity_counts = {}

    for result in presidio_results:
        entity = result.entity_type
        entity_counts[entity] = entity_counts.get(entity, 0) + 1

    total_pii = len(presidio_results)

    person_count = entity_counts.get("PERSON", 0)
    email_count = entity_counts.get("EMAIL_ADDRESS", 0)
    phone_count = entity_counts.get("PHONE_NUMBER", 0)
    organization_count = entity_counts.get("ORGANIZATION", 0)

    st.subheader("📊 PII Statistics")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total", total_pii)
    col2.metric("Persons", person_count)
    col3.metric("Emails", email_count)
    col4.metric("Phones", phone_count)
    col5.metric("Organizations", organization_count)

    st.success("✅ File uploaded successfully!")

    # ---------------- REGEX DETECTION ----------------

    st.subheader("Regex Detection")

    for category, values in pii.items():

        st.write(f"### {category}")

        if values:

            for value in values:
                st.write(f"- {value}")

        else:
            st.write("No data found.")

    # ---------------- PRESIDIO DETECTION ----------------

    st.subheader("Presidio Detection")

    if presidio_results:

        for result in presidio_results:

            detected_text = text[result.start:result.end]

            st.write(
                f"**{result.entity_type}** : "
                f"{detected_text} "
                f"(Score: {result.score:.2f})"
            )

    else:

        st.write("No PII detected by Presidio.")

    # ---------------- REPLACEMENT SUMMARY ----------------

    st.subheader("PII Replacement Summary")

    if replacements:

        summary = []

        for original, fake in replacements.items():

            summary.append({
                "Original": original,
                "Redacted": fake
            })

        df = pd.DataFrame(summary)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info("No replacements made.")

    # ---------------- ORIGINAL TEXT ----------------

    st.subheader("📄 Original Document")

    st.text_area(
        "Original Text",
        text,
        height=300
    )

    # ---------------- REDACTED TEXT ----------------

    st.subheader("🔒 Redacted Document")

    st.text_area(
        "Redacted Text",
        redacted_text,
        height=300
    )

        # ---------------- DOWNLOAD ----------------

    st.download_button(
        label="📥 Download Redacted DOCX",
        data=redacted_doc,
        file_name="redacted_document.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    # ---------------- EVALUATION METRICS ----------------

    st.subheader("📈 Evaluation Metrics")

    metrics = get_metrics()

    col1, col2, col3 = st.columns(3)

    col1.metric("Precision", f"{metrics['Precision']:.2f}")
    col2.metric("Recall", f"{metrics['Recall']:.2f}")
    col3.metric("F1 Score", f"{metrics['F1 Score']:.2f}")