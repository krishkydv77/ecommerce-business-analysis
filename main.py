from src.data_cleaning import load_and_clean
from src.analysis import total_revenue
from src.visualization import (
    plot_monthly_sales,
    plot_top_countries,
    plot_top_products,
    plot_revenue_distribution
)
from src.rfm import create_rfm

df = load_and_clean('data/data.csv')

print("Total Revenue:", total_revenue(df))

# Visualizations
plot_monthly_sales(df)
plot_top_countries(df)
plot_top_products(df)
plot_revenue_distribution(df)

# RFM
rfm = create_rfm(df)
rfm.to_csv('outputs/rfm_output.csv')