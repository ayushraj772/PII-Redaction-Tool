from docx import Document

def read_docx(file):
    document = Document(file)

    text = []

    for para in document.paragraphs:
        if para.text.strip():
            text.append(para.text)

    return "\n".join(text)