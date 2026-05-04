import pandas as pd

def create_rfm(df):
    snapshot = df['InvoiceDate'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot - x.max()).days,
        'InvoiceNo': 'count',
        'TotalPrice': 'sum'
    })

    rfm.columns = ['Recency','Frequency','Monetary']
    return rfm