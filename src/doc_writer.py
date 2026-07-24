from docx import Document
from io import BytesIO


def create_redacted_doc(uploaded_file, replacements):
    """
    Create a redacted DOCX by replacing detected PII.
    Returns the document as BytesIO.
    """

    doc = Document(uploaded_file)

    for para in doc.paragraphs:

        text = para.text

        for original, fake_value in replacements.items():
            text = text.replace(original, fake_value)

        para.text = text

    output = BytesIO()
    doc.save(output)
    output.seek(0)

    return output