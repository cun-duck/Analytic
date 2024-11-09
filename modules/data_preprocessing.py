# modules/data_preprocessing.py
import pandas as pd

def load_data(file):
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xls') or file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        return df
    except Exception:
        return None

def clean_data(df):
    df = df.dropna()
    df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]
    return df

def detect_common_columns(df):
    common_columns = {'tanggal': [], 'harga': [], 'nama': []}
    for col in df.columns:
        if 'tanggal' in col or 'date' in col:
            common_columns['tanggal'].append(col)
        elif 'harga' in col or 'price' in col:
            common_columns['harga'].append(col)
        elif 'nama' in col or 'name' in col:
            common_columns['nama'].append(col)
    return common_columns
