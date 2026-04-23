import pandas as pd
from pypdf import PdfReader


def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "

    return text