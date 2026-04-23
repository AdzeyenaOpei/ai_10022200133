import pandas as pd


def clean_csv(df):
    df = df.drop_duplicates()
    df = df.fillna("Not Available")
    df.columns = [col.strip() for col in df.columns]
    return df



def clean_text(text):
    text = text.replace(" ", " ")
    text = " ".join(text.split())
    return text