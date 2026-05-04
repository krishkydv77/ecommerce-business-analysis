import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path, encoding='ISO-8859-1')
    df = df.dropna(subset=['CustomerID'])
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True)
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df