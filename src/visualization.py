import matplotlib.pyplot as plt
import seaborn as sns

# 1. Monthly Sales Trend
def plot_monthly_sales(df):
    df['Month'] = df['InvoiceDate'].dt.month
    monthly = df.groupby('Month')['TotalPrice'].sum()
    
    plt.figure()
    monthly.plot(marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.savefig('outputs/plots/monthly_sales.png')
    plt.close()


# 2. Top 10 Countries by Revenue
def plot_top_countries(df):
    top_countries = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
    
    plt.figure()
    top_countries.plot(kind='bar')
    plt.title('Top 10 Countries by Revenue')
    plt.xlabel('Country')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.savefig('outputs/plots/top_countries.png')
    plt.close()


# 3. Top 10 Products
def plot_top_products(df):
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    
    plt.figure()
    top_products.plot(kind='bar')
    plt.title('Top 10 Products')
    plt.xlabel('Product')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=90)
    plt.savefig('outputs/plots/top_products.png')
    plt.close()


# 4. Revenue Distribution (Important for Insight)
def plot_revenue_distribution(df):
    plt.figure()
    sns.histplot(df['TotalPrice'], bins=50)
    plt.title('Revenue Distribution')
    plt.xlabel('Transaction Value')
    plt.ylabel('Frequency')
    plt.savefig('outputs/plots/revenue_distribution.png')
    plt.close()