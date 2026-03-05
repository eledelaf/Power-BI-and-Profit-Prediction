# Sales Performance Analysis & Profit Prediction

End-to-end analysis of 700 sales transactions across 5 countries, 6 products, and 5 customer segments (Sep 2013 – Dec 2014), answering key business questions about revenue, trends, product performance, and profitability — plus a **machine learning model** that predicts profit from pre-sale features.

## Key Findings

### Analysis
- **Paseo** is the top-selling product, leading both in revenue and units sold across all markets.
- Year-over-year revenue growth is positive when comparing the overlapping months (Sep–Dec) of 2013 vs 2014.
- Higher discount bands correlate with significantly lower profit margins — heavy discounting erodes profitability.
- A notable portion of transactions are loss-making, concentrated in specific product-segment combinations.

### Profit Prediction
- **Random Forest (R² = 0.92)** significantly outperforms Linear Regression (R² = 0.68) for profit prediction.
- **Units Sold** is the strongest predictor of profit, followed by Manufacturing Price and Sale Price.
- Discount Band has a visible impact — moving from "None" to "High" reduces expected profit.
- Features like Sales, COGS, Gross Sales, and Discounts were excluded to avoid data leakage.

## Dataset

| Detail | Value |
|--------|-------|
| Source | `Sample_data.xlsx` |
| Rows | 700 |
| Time Period | September 2013 – December 2014 |
| Countries | Germany, Canada, France, Mexico, USA |
| Products | Carretera, Paseo, Velo, VTT, Amarilla, Montana |
| Segments | Government, Midmarket, Channel Partners, Enterprise, Small Business |

**Columns:** Segment, Country, Product, Discount Band, Units Sold, Manufacturing Price, Sale Price, Gross Sales, Discounts, Sales, COGS, Profit, Date

## Project Structure

```
Power-BI-and-Profit-Prediction/
├── Sales_Performance_Analysis.ipynb   # EDA notebook (start here)
├── Profit_Prediction.ipynb            # ML notebook — Linear Regression vs Random Forest
├── Data_cleaning.py                   # Reusable data cleaning module
├── Sales_Performance_Analysis.py      # Original script version of the analysis
├── Sample_data.xlsx                   # Source dataset
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
└── README.md                          # This file
```

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Power-BI-and-Profit-Prediction.git
cd Power-BI-and-Profit-Prediction

# 2. Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Open the notebook
jupyter notebook Sales_Performance_Analysis.ipynb
```

## Technologies

- **Python 3** — pandas, numpy, matplotlib, seaborn, scikit-learn
- **Jupyter Notebook** — interactive analysis and visualization
- **scikit-learn** — Linear Regression, Random Forest, train/test split, metrics
- **openpyxl** — Excel file reading

## Future Work

- Interactive Power BI dashboard connected to this dataset
- Hyperparameter tuning to reduce Random Forest overfitting
- Additional models (Gradient Boosting, XGBoost) for comparison
