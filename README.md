# 🔒 PII Redaction Tool

A Streamlit-based web application for detecting and anonymizing Personally Identifiable Information (PII) from DOCX documents using Regex, Microsoft Presidio, and Faker.

## Features

- Upload DOCX documents
- Extract text from DOCX
- Regex-based PII detection
- Microsoft Presidio PII detection
- Automatic anonymization using Faker
- Download redacted DOCX
- PII Statistics Dashboard
- PII Replacement Summary
- Evaluation Metrics (Precision, Recall, F1 Score)

## Technologies Used

- Python
- Streamlit
- Microsoft Presidio
- spaCy
- Faker
- python-docx
- Pandas

## Project Structure

```
PII-Redaction-Tool/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── doc_reader.py
│   ├── pii_detector.py
│   ├── presidio_detector.py
│   ├── anonymizer.py
│   ├── doc_writer.py
│   └── evaluation.py
│
├── input/
├── output/
└── docs/
```

## Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

## Evaluation Metrics

| Metric | Score |
|--------|-------|
| Precision | 0.96 |
| Recall | 0.94 |
| F1 Score | 0.95 |

## Future Improvements

- PDF Support
- OCR Support
- Better DOCX formatting preservation
- Multi-file processing

## Author

Ayush Raj
B.Tech Electronics and Communication Engineering
National Institute of Technology Agartala