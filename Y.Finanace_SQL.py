# Importing Library
import psycopg2
import pandas as pd
import yfinance as yf
import numpy as np
import time

#Connecting with SQL

conn=psycopg2.connect(
    dbname="Stock_data",
    user="stock_analysis",
    password="Stock_INFO",
    host="localhost",
    port="5432"

)
cur=conn.cursor()

# creating table if not exist

cur.execute("""DROP TABLE if exists stock_base""")
conn.commit()
cur.execute("""
create table if not exists stock_base
(
id Serial Primary key,
ticker VARCHAR(120),
company_name TEXT,
sector TEXT,
industry TEXt,
country TEXT,
market_Cap BIGINT,
today_price FLOAT,
closing_price FLOAT,
yesturday_Price FLOAT,
price_Diff FLOAT,
percentage FLOAT
);""")
conn.commit()

#Truncating the table before updating the fresh data
cur.execute("TRUNCATE TABLE stock_base")
conn.commit()
# All the S and P 500 ticker for analysis.

tickers=["AAPL "," MSFT "," GOOG "," AMZN "," NVDA "," BRK-B "," META "," TSLA "," LLY "," V "," UNH "," JNJ "," XOM "," JPM "," WMT "," MA "," PG "," AVGO "," HD "," ORCL "," CVX "," MRK "," ABBV "," KO "," PEP "," COST "," ADBE "," BAC "," CSCO "," PFE "," TMO "," MCD "," ACN "," CRM "," CMCSA "," DHR "," LIN "," ABT "," NFLX "," AMD "," NKE "," TMUS "," DIS "," WFC "," TXN "," PM "," UPS "," MS "," COP "," AMGN "," CAT "," VZ "," UNP "," NEE "," INTC "," BA "," INTU "," BMY "," IBM "," LOW "," RTX "," HON "," QCOM "," GE "," SPGI "," AMAT "," AXP "," DE "," PLD "," LMT "," SBUX "," NOW "," BKNG "," ELV "," MDT "," SCHW "," GS "," SYK "," ADP "," TJX "," ISRG "," T "," BLK "," MDLZ "," GILD "," MMC "," VRTX "," ADI "," REGN "," LRCX "," CVS "," ETN "," ZTS "," SLB "," AMT "," CB "," CI "," C "," BDX "," PGR "," MO "," EOG "," SO "," BSX "," CME "," FI "," HCA "," ITW "," ATVI "," EQIX "," DUK "," MU "," SHW "," FDX "," AON "," KLAC "," PYPL "," NOC "," SNPS "," WM "," PANW "," ICE "," APD "," CHTR "," CSX "," CL "," GD "," HUM "," TGT "," MAR "," MNST "," MCO "," CDNS "," MPC "," MCK "," OXY "," ORLY "," USB "," EL "," ANET "," FCX "," PXD "," MMM "," EMR "," ROP "," ECL "," PH "," CMG "," PSX "," APH "," NXPI "," VTR "," CTAS "," PNC "," NSC "," PSA "," F "," HES "," AJG "," TDG "," VLO "," KDP "," STZ "," MET "," EW "," MSI "," RSG "," GM "," TT "," FTNT "," HSY "," CARR "," AZO "," SRE "," AFL "," ADM "," PCAR "," PAYX "," KMB "," CCI "," MCHP "," ODFL "," ADSK "," WELL "," WMB "," NUE "," CPRT "," KHC "," AIG "," MSCI "," DXCM "," GIS "," LVS "," AEP "," D "," ROST "," JCI "," O "," IDXX "," TEL "," COF "," EXC "," DHI "," HLT "," IQV "," ON "," KMI "," MRNA "," TFC "," DOW "," BIIB "," SPG "," TRV "," DLR "," ABC "," SYY "," YUM "," CTVA "," DG "," AME "," BKR "," HAL "," A "," GWW "," PCG "," CTSH "," DD "," CNC "," OTIS "," LHX "," BK "," KR "," AMP "," CEG "," PRU "," VRSK "," ROK "," LEN "," CMI "," PPG "," FAST "," FIS "," BF-B "," GPN "," XEL "," EA "," DVN "," CSGP "," LYB "," DLTR "," WBD "," GEHC "," URI "," ED "," HPQ "," NEM "," PEG "," VICI "," PWR "," OKE "," WST "," VMC "," ACGL "," ALL "," GLW "," WEC "," APTV "," AWK "," IR "," CDW "," ALGN "," FTV "," EXR "," DAL "," MLM "," FANG "," ILMN "," EIX "," MTD "," IT "," CBRE "," NDAQ "," AVB "," RCL "," ANSS "," ZBH "," RMD "," EQR "," TROW "," XYL "," SBAC "," TSCO "," EFX "," WY "," TTWO "," DFS "," KEYS "," MPWR "," WBA "," CHD "," MKC "," EBAY "," ULTA "," ES "," STE "," HIG "," HPE "," RJF "," DTE "," GPC "," STT "," CAH "," ALB "," HRL "," MTB "," K "," AEE "," BAX "," BR "," FICO "," CTRA "," WTW "," VRSN "," FE "," INVH "," BRO "," ETR "," HWM "," ARE "," WAB "," ROL "," NVR "," JBHT "," DOV "," CCL "," GRMN "," FSLR "," LYV "," FLT "," DRI "," LUV "," CLX "," TSN "," TDY "," LH "," TRGP "," PPL "," PFG "," RF "," MOH "," COO "," HOLX "," CNP "," ENPH "," STLD "," FITB "," PHM "," ATO "," BALL "," BBY "," EXPD "," IRM "," PAYC "," BG "," J "," MAA "," SWKS "," PTC "," CMS "," IEX "," FDS "," CINF "," IFF "," HBAN "," UAL "," MRO "," WAT "," WRB "," NTRS "," EXPE "," NTAP "," CBOE "," FOX "," OMC "," EQT "," TYL "," TER "," AKAM "," CF "," ESS "," EG "," DGX "," AXON "," MGM "," TXT "," SJM "," CAG "," INCY "," PODD "," AVY "," SNA "," AMCR "," RVTY "," LKQ "," ZBRA "," L "," EPAM "," SYF "," LW "," SWK "," TAP "," POOL "," APA "," VTRS "," STX "," DPZ "," NDSN "," PKG "," LDOS "," MOS "," TRMB "," BEN "," CFG "," KMX "," GEN "," EVRG "," CE "," LNT "," MAS "," CPB "," WDC "," UDR "," IPG "," MTCH "," TECH "," AES "," NWS "," IP "," KIM "," CPT "," JKHY "," HST "," CZR "," PEAK "," FMC "," BIO "," CHRW "," PNR "," NI "," CDAY "," WYNN "," GL "," REG "," AOS "," TFX "," CRL "," KEY "," HSIC "," EMN "," BXP "," AAL "," PARA "," QRVO "," ALLE "," MKTX "," BWA "," DVA "," FFIV "," SEDG "," ETSY "," JNPR "," PNW "," HAS "," HII "," BBWI "," NRG "," WRK "," CTLT "," RHI "," UHS "," XRAY "," FRT "," VFC "," RL "," AIZ "," WHR "," NCLH "," GNRC "," IVZ "," CMA "," MHK "," OGN "," ALK "," ZION "," SEE "," LNC "," NWL "," DXC "," AAP "," TPR"]
tickers = [ticker.strip() for ticker in tickers]
for symbol in tickers:
    try:
        tkr=yf.Ticker(symbol)
        info=tkr.info
        if not isinstance(info,dict):
            raise ValueError(f"Invalid info data returned for {symbol}:{info}")
        hist=tkr.history(period="1mo")
        if hist.empty:
            raise ValueError(f"{symbol}: No data found, possibly delisted.")


        today_price=info.get("currentPrice")
        close_price=hist["Close"].iloc[-1] if len(hist) >=1 else None
        yesturday_price=hist["Close"].iloc[-2] if len(hist) >1 else None

        # converting numpy types to native

        def safe_round(val):
            if isinstance(val,np.generic):
                return val.item()
            return round(float(val),1) if val is not None else None

        today_price=safe_round(today_price)
        close_price=safe_round(close_price)
        yesturday_price=safe_round(yesturday_price)

        today_price=round(today_price,2) if today_price is not None else None
        close_price=round(close_price,2) if close_price is not None else None
        yesturday_price=round(yesturday_price,2) if yesturday_price is not None else None
        price_diff=None
        percentage_change=None
        market_cap=None

        if today_price is not None and yesturday_price is not None:
                      price_diff=round(today_price-yesturday_price,2)
                      percentage_change=round(((today_price-yesturday_price)/yesturday_price )*100,2)
                      market_cap=info.get("marketCap")
                      market_cap=int(market_cap) if market_cap is not None else None

        #inserting data into PostgreSql Table

        cur.execute("""INSERT INTO stock_base

                    (ticker,company_name,sector,industry,country,market_cap,today_price,closing_price,yesturday_price,price_diff,percentage)
                     VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
                    (
                    symbol,
                    info.get("longName"),
                    info.get("sector"),
                    info.get("industry"),
                    info.get("country"),
                    info.get("marketCap"),
                    today_price,
                    close_price,
                    yesturday_price,
                    price_diff,
                    percentage_change))
        
        conn.commit()
        time.sleep(0.1)

    except Exception as Error:
        print(f"Error for {symbol}:{Error}")
        conn.rollback()
        time.sleep(1.5)
                   
                    
