# Stock-Performance-Dash-Board

DashBorad-Visuals-**https://app.powerbi.com/links/wxYVkzRI5Q?ctid=16a0d960-ee74-4f56-a22a-19ae057918b2&pbi_source=linkShare**
This repositary allows you to view daily updated information on S&P 500 stock performance across different categories.
DashBorad Overview
Data Collection: Financial data is fetched using Python and the Yahoo Finance library.
Data Processing: The raw data is cleaned, aggregated, and modified using PostgreSQL SQL queries.
Data Visualization: The processed data is visualized in Power BI, showing insights such as top sectors, industries, stock types expensive vs penny stocks.


The goal of this project is to provide a **daily updated overview of the S&P 500 stock market performance** across different categories. 
It helps users quickly identify:
- Comparison between expensive and penny stocks
- Sectorweighate based on Mcap
- Overall index performance
- Total count of performing companies in each sector
- Lowprice and high return stocks
- Premium price and premium return stocks
- Sector wise analysis
- Top 5 Mcap comparison
- Top returns today
- Searching Specific stock performane based on client request.

By combining **Python for data fetching**, **SQL for data processing**, and **Power BI for visualization**, this project demonstrates a complete **data-to-insight workflow** that can be used for investment analysis or business intelligence reporting.

Reference View for BI

<img width="1116" height="703" alt="image" src="https://github.com/user-attachments/assets/dea0b4b0-484d-462e-9e1c-bc0decfea2d4" />

This project simulates sector-weighted returns for S&P 500 firms using market capitalization data.
It validates results against official benchmarks with a deviation of ±0.10%, demonstrating audit-grade accuracy.

🔧 Features
- ✅ Sector-level performance attribution
- 📊 Market cap-weighted return calculation
- 🧮 Benchmark comparison with S&P 500
- 🖥️ Visual dashboard of top-performing firms
- ⚙️ Python-based automation for data processin
🧠 Tools Used
- Python: pandas, numpy, yfinance
- SQL: For data extraction and transformation
- Power BI : For dashboard visualization
- Windows Task Scheduler: For automation setup
- 📊 Benchmark Validation
  My dashboard’s weighted returns closely match official S&P 500 sector returns. Here's a sample comparison from the official data and my dashborad view.
| Sector | My Return (%) | S&P 500 Return (%) | Deviation (%) | 
| Technology | 12.45 | 12.55 | -0.10 | 
| Healthcare | 8.32 | 8.30 | +0.02 | 
| Financials | 6.78 | 6.80 | -0.02 | 
| Consumer Goods | 9.10 | 9.15 | -0.05 | 










