def total_revenue(df):
    return df['TotalPrice'].sum()

def country_sales(df):
    return df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)

def top_products(df):
    return df.groupby('Description')['Quantity'].sum().sort_values(ascending=False)