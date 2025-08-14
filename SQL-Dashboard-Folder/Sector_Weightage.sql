select sector,sum(market_cap) from Stock_base
where company_name is not null
group by sector
ORDER  BY sum(market_cap) DESC
